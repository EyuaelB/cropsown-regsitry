#!/usr/bin/env bash
# Redeploy the crop sown registry onto a cluster, pulling freshly pushed images.
#
# Run this ON THE CLUSTER BOX (the one with kubectl access), not on the build
# machine.
#
#   ./k8s-redeploy.sh diagnose      # why is db-seed failing? read this first
#   ./k8s-redeploy.sh images        # point every deployment at the new digests
#   ./k8s-redeploy.sh reseed --yes  # DROP the registry database and seed it again
#   ./k8s-redeploy.sh status        # what is running now
#
# `reseed` destroys all registry data. It is gated behind --yes and is only
# appropriate on a non-production cluster.
#
# Why a reseed is usually the fix: the seed SQL is written as plain INSERTs, so
# running it a second time over an already-seeded database fails on duplicate
# keys. A job that succeeded once and now errors on every retry is the signature
# of that. Recreating the database also picks up schema changes (the `season`
# column added for the REG/S1/2026/… ids) without a hand-written migration.
set -euo pipefail

NS="${NAMESPACE:-crop}"
RELEASE="${RELEASE:-cropsown-registry}"
PG_POD="${PG_POD:-commons-postgresql-0}"
PG_USER="${PG_USER:-postgres}"
DB_NAME="${DB_NAME:-cropsown_registry}"
# The application connects as its own role, not as postgres. A recreated
# database must be owned by that role or the API can read but not write.
DB_OWNER="${DB_OWNER:-cropsown_registry_user}"

# Digests, not tags: the 0.1.0 tag is reused between builds, so a node that has
# already cached it will not pull the new bytes. These come from the push.
STAFF_API=eyuaelb/cropsown-staff-api@sha256:bcd9e8104ae124178539f1c2a8cdb254e2db34b4e6cf07cab44484ddfd26f049
PARTNER_API=eyuaelb/cropsown-partner-api@sha256:e59e68d4421707dc8aff364979ce635d8dc84dc6f9267b19ca0a2bc222cbb7da
CELERY=eyuaelb/cropsown-celery@sha256:24d5b25b3141b023b3edc597214088b9c720d99b57e8b7575761d3f9d9ba037b
DB_SEED=eyuaelb/cropsown-db-seed@sha256:3bf29e0fbca9a23f8cfd2553c541580482659474a063c769e31f5aa6c0f57a45
STAFF_UI=eyuaelb/cropsown-staff-ui@sha256:bd1f754679dfd7ee6dc845fb6905b5bde2fe15aa5a77bdb651d4b4d2b76bae9f

k() { kubectl -n "$NS" "$@"; }

pg() {
  # -q so psql notices do not drown the output; the password comes from the
  # pod's own environment rather than being passed on the command line.
  k exec "$PG_POD" -- env PGPASSWORD="$(pg_password)" \
    psql -U "$PG_USER" -d "${2:-postgres}" -v ON_ERROR_STOP=1 -q -c "$1"
}

pg_password() {
  k get secret commons-postgresql -o jsonpath='{.data.postgres-password}' 2>/dev/null | base64 -d ||
    k exec "$PG_POD" -- printenv POSTGRES_PASSWORD
}

case "${1:-status}" in

diagnose)
  echo "── failed db-seed pods ─────────────────────────────────────────────"
  for p in $(k get pods -l job-name --no-headers 2>/dev/null | awk '$3=="Error"{print $1}'); do
    echo "── $p"
    k logs "$p" --tail=40 || true
  done
  echo
  echo "── celery-beat (crash looping) ─────────────────────────────────────"
  k logs "deploy/${RELEASE}-celery-beat-producer" --previous --tail=30 2>/dev/null || true
  echo
  echo "── does the registry database have the season column? ──────────────"
  pg "SELECT column_name FROM information_schema.columns
       WHERE table_name='g2p_register_crop_sowns' AND column_name='season';" "$DB_NAME" || true
  ;;

images)
  echo "==> pointing deployments at the pushed digests"
  # Name the container. `*=` also rewrites INIT containers, which replaced the
  # postgres-checker (a psql client) with the app image and left every pod stuck
  # in PodInitializing on `pg_isready: not found`.
  k set image "deploy/${RELEASE}-staff-portal-api"      "staff-portal-api=$STAFF_API"
  k set image "deploy/${RELEASE}-partner-api"           "partner-api=$PARTNER_API"
  k set image "deploy/${RELEASE}-celery-worker"         "celery-worker=$CELERY"
  k set image "deploy/${RELEASE}-celery-beat-producer"  "celery-beat-producer=$CELERY"
  k set image "deploy/${RELEASE}-staff-portal-ui"       "staff-portal-ui=$STAFF_UI"

  for d in staff-portal-api partner-api celery-worker staff-portal-ui; do
    k rollout status "deploy/${RELEASE}-${d}" --timeout=5m || true
  done
  ;;

reseed)
  [ "${2:-}" = "--yes" ] || { echo "refusing: this DROPs $DB_NAME. re-run with --yes"; exit 1; }

  echo "==> scaling the writers down so nothing reconnects mid-drop"
  for d in staff-portal-api partner-api celery-worker celery-beat-producer; do
    k scale "deploy/${RELEASE}-${d}" --replicas=0 || true
  done
  k wait --for=delete pod -l "app.kubernetes.io/instance=${RELEASE}" --timeout=120s 2>/dev/null || true

  echo "==> dropping and recreating $DB_NAME"
  # Sessions must be evicted first or DROP DATABASE blocks on them.
  pg "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='${DB_NAME}' AND pid <> pg_backend_pid();"
  pg "DROP DATABASE IF EXISTS \"${DB_NAME}\";"
  pg "CREATE DATABASE \"${DB_NAME}\" OWNER \"${DB_OWNER}\";"
  # Postgres 15+ no longer grants CREATE on public to everyone, so the owner is
  # made explicit on the schema too.
  pg "GRANT ALL ON SCHEMA public TO \"${DB_OWNER}\";" "${DB_NAME}"
  pg "ALTER SCHEMA public OWNER TO \"${DB_OWNER}\";" "${DB_NAME}"

  echo "==> bringing the API back: it runs the migrations on start, which"
  echo "    recreates the schema (including the season column)"
  k set image "deploy/${RELEASE}-staff-portal-api" "*=$STAFF_API"
  k scale "deploy/${RELEASE}-staff-portal-api" --replicas=1
  k rollout status "deploy/${RELEASE}-staff-portal-api" --timeout=10m

  echo "==> re-running the seed job with the new image"
  # A completed Job is immutable, so it is replaced rather than patched.
  job=$(k get job -o name | grep db-seed | head -1)
  if [ -n "$job" ]; then
    k get "$job" -o json \
      | python3 -c "
import json,sys
d = json.load(sys.stdin)
for f in ('selector','uid','resourceVersion','creationTimestamp','ownerReferences'):
    d['metadata'].pop(f, None); d['spec'].pop(f, None)
d['spec']['template']['metadata'].pop('labels', None)
d['spec'].pop('selector', None)
d['status'] = {}
for c in d['spec']['template']['spec']['containers']:
    c['image'] = '${DB_SEED}'
print(json.dumps(d))" \
      | k replace --force -f -
    k wait --for=condition=complete "$job" --timeout=15m ||
      k logs "$job" --tail=60
  else
    echo "!! no db-seed job found — run: helm upgrade $RELEASE ... to recreate it"
  fi

  echo "==> scaling the rest back up"
  for d in partner-api celery-worker celery-beat-producer; do
    k scale "deploy/${RELEASE}-${d}" --replicas=1 || true
  done
  ;;

status)
  k get pods | grep -E "NAME|${RELEASE}"
  echo
  echo "── images in use ───────────────────────────────────────────────────"
  k get deploy -o custom-columns=NAME:.metadata.name,IMAGE:.spec.template.spec.containers[0].image |
    grep -E "NAME|${RELEASE}"
  ;;

*)
  sed -n '2,20p' "$0"
  ;;
esac
