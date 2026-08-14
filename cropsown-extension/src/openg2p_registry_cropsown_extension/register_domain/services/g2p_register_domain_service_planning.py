import logging
from datetime import date

from openg2p_registry_core.services import G2PRegisterDomainService

from .domain_validation_utils import as_float, parse_date, validation_error

_logger = logging.getLogger("g2p-register-domain-service")


class G2PRegisterDomainServicePlanning(G2PRegisterDomainService):
    async def validate_domain_attributes(self, records: list[dict]):
        for record in records:
            self._validate_planned_area(record)
            self._validate_planned_date(record)
        self._validate_no_duplicate_commodity_season(records)

    def _validate_planned_area(self, record: dict) -> None:
        planned_area = as_float(record.get("planned_area"))
        if planned_area is not None and planned_area <= 0:
            validation_error("planned_area must be greater than zero when provided")

    def _validate_planned_date(self, record: dict) -> None:
        planned_date = parse_date(record.get("planned_date"))
        if planned_date is not None and planned_date.year > date.today().year + 1:
            validation_error("planned_date must not be more than one season ahead")

    def _validate_no_duplicate_commodity_season(self, records: list[dict]) -> None:
        seen: set[tuple[str, str, str]] = set()
        for record in records:
            commodity = str(record.get("commodity") or "").strip()
            season = str(record.get("season") or "").strip()
            land = str(record.get("land_uuid") or "").strip()
            if not commodity:
                continue
            key = (commodity, season, land)
            if key in seen:
                validation_error(
                    "Duplicate commodity entries for the same season and land are not allowed"
                )
            seen.add(key)

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for planning")

        keys = [
            "functional_record_id",
            "land_uuid",
            "land_id",
            "season",
            "commodity",
            "crop_variety",
            "crop_category",
            "local_name",
            "scientific_name",
            "plot_category",
            "cropping_system",
            "planned_area",
            "seed_class",
            "seed_source",
            "planned_fertilizer_type",
            "water_source",
            "cluster_status",
        ]
        search_text = []
        if extra:
            search_text.extend(str(item).strip() for item in extra if str(item).strip())
        search_text.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(search_text).strip()

    def construct_record_name(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing record name for planning")

        keys = ["commodity", "season", "planned_area"]
        record_name = []
        if extra:
            record_name.extend(str(item).strip() for item in extra if str(item).strip())
        record_name.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(record_name).strip()
