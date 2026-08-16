#!/usr/bin/env bash
# Build every crop sown image, tag them all with one version, optionally push.
#
#   ./scripts/build-images.sh              # build + tag 0.1.0
#   ./scripts/build-images.sh 0.2.0        # build + tag 0.2.0
#   ./scripts/build-images.sh 0.2.0 --push # ... and push to the registry
#
# `docker compose build` alone changes nothing that is running: the containers
# keep their old image until recreated, and a node that already cached this tag
# will not re-pull it. Reusing a tag is therefore only safe if every consumer is
# recreated (compose) or pinned by digest (kubernetes) — the digests printed at
# the end are what to pin.
set -euo pipefail
cd "$(dirname "$0")/.."

VERSION="${1:-0.1.0}"
PUSH="${2:-}"
NAMESPACE="${IMAGE_NAMESPACE:-eyuaelb}"

# compose service -> local image -> published repository
SERVICES="migrate db-seed staff-ui partner-api celery-worker dashboard-ui"
MAP="
staff-api:cropsown-staff-api
partner-api:cropsown-partner-api
celery:cropsown-celery
db-seed:cropsown-db-seed
staff-ui:cropsown-staff-ui
dashboard-ui:crop-dashboard
"

echo "==> building ($SERVICES)"
docker compose build $SERVICES

echo "==> tagging ${NAMESPACE}/*:${VERSION}"
for entry in $MAP; do
  local_name="openg2p-cropsown-registry-${entry%%:*}-local:dev"
  remote="${NAMESPACE}/${entry##*:}:${VERSION}"
  docker tag "$local_name" "$remote"
  printf '    %-46s <- %s\n' "$remote" "$local_name"
done

if [ "$PUSH" = "--push" ]; then
  echo "==> pushing"
  for entry in $MAP; do
    docker push "${NAMESPACE}/${entry##*:}:${VERSION}"
  done

  echo "==> digests (pin these in kubernetes)"
  for entry in $MAP; do
    remote="${NAMESPACE}/${entry##*:}:${VERSION}"
    digest=$(docker inspect --format '{{index .RepoDigests 0}}' "$remote" 2>/dev/null || echo "unknown")
    printf '    %s\n' "$digest"
  done
else
  echo "==> not pushed (re-run with: $0 $VERSION --push)"
fi
