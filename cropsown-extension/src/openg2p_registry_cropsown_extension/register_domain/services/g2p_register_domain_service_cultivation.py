import logging
from datetime import date

from openg2p_registry_core.services import G2PRegisterDomainService

from .domain_validation_utils import as_float, parse_date, validation_error

_logger = logging.getLogger("g2p-register-domain-service")


class G2PRegisterDomainServiceCultivation(G2PRegisterDomainService):
    async def validate_domain_attributes(self, records: list[dict]):
        for record in records:
            self._validate_actual_planted_date(record)
            self._validate_actual_crop_area(record)

    def _validate_actual_planted_date(self, record: dict) -> None:
        planted_date = parse_date(record.get("actual_planted_date"))
        if planted_date is not None and planted_date > date.today():
            validation_error("actual_planted_date must not be in the future")

    def _validate_actual_crop_area(self, record: dict) -> None:
        crop_area = as_float(record.get("actual_crop_area"))
        if crop_area is not None and crop_area <= 0:
            validation_error("actual_crop_area must be greater than zero when provided")

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for cultivation")

        keys = [
            "functional_record_id",
            "land_uuid",
            "season",
            "commodity",
            "crop_variety",
            "crop_category",
            "land_prep_method",
            "cultivation_type",
            "cropping_system",
            "actual_crop_area",
            "actual_seed_class",
            "actual_seed_source",
            "actual_fertilizer_type",
            "water_source",
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
        _logger.info("Constructing record name for cultivation")

        keys = ["commodity", "land_prep_method", "actual_crop_area"]
        record_name = []
        if extra:
            record_name.extend(str(item).strip() for item in extra if str(item).strip())
        record_name.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(record_name).strip()
