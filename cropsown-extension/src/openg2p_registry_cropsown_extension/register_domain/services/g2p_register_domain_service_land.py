import logging

from openg2p_registry_core.services import G2PRegisterDomainService

from .domain_validation_utils import as_float, validation_error

_logger = logging.getLogger("g2p-register-domain-service")


class G2PRegisterDomainServiceLand(G2PRegisterDomainService):
    async def validate_domain_attributes(self, records: list[dict]):
        for record in records:
            self._validate_land_area(record)
        self._validate_no_duplicate_land_id(records)

    def _validate_land_area(self, record: dict) -> None:
        land_area = as_float(record.get("land_area"))
        if land_area is not None and land_area <= 0:
            validation_error("land_area must be greater than zero when provided")

    def _validate_no_duplicate_land_id(self, records: list[dict]) -> None:
        """land_uuid is generated, so the identifier worth guarding is land_id."""
        seen: set[str] = set()
        for record in records:
            value = record.get("land_id")
            if value is None or str(value).strip() == "":
                continue
            normalized = str(value).strip()
            if normalized in seen:
                validation_error("Duplicate land_id entries are not allowed")
            seen.add(normalized)

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for land")

        keys = [
            "functional_record_id",
            "land_uuid",
            "land_id",
            "ownership_type",
            "soil_fertility_type",
            "plot_category",
            "land_area",
            "unit",
            "sub_kebele",
            "latitude",
            "longitude",
            "address_line_1",
            "address_line_2",
            "postal_code",
            "country_code",
            "shape_type",
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
        _logger.info("Constructing record name for land")

        keys = ["land_id", "land_area", "unit"]
        record_name = []
        if extra:
            record_name.extend(str(item).strip() for item in extra if str(item).strip())
        record_name.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(record_name).strip()
