import logging
import re
from datetime import date

from openg2p_registry_core.services import G2PRegisterDomainService

from .domain_validation_utils import as_int, validation_error

_logger = logging.getLogger("g2p-register-domain-service")


_MOBILE_NUMBER_PATTERN = re.compile(r"^\+?[0-9][0-9\- ]{5,19}$")

class G2PRegisterDomainServiceCropSown(G2PRegisterDomainService):
    async def validate_domain_attributes(self, records: list[dict]):
        for record in records:
            self._validate_production_year(record)
            self._validate_mobile_number(record, "surveyor_mobile_number")
            self._validate_mobile_number(record, "supervisor_mobile_number")

    def _validate_production_year(self, record: dict) -> None:
        year = as_int(record.get("production_year"))
        if year is not None and year > date.today().year:
            validation_error("production_year must not be in the future")

    def _validate_mobile_number(self, record: dict, field: str) -> None:
        value = record.get(field)
        if value is None or str(value).strip() == "":
            return
        if not _MOBILE_NUMBER_PATTERN.match(str(value).strip()):
            validation_error(f"{field} is not a valid mobile number")

    def construct_search_text(self, payload: dict, extra: list[str] = None) -> str:
        _logger.info("Constructing search text for crop sown record")

        keys = [
            "functional_record_id",
            "farmer_name",
            "farmer_id",
            "fayda_fan_id",
            "land_uuid",
            "status",
            "production_year",
            "lifecycle_stage",
            "surveyor_name",
            "supervisor_name",
            "latitude",
            "longitude",
            "address_line_1",
            "address_line_2",
            "country_code",
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
        _logger.info("Constructing record name for crop sown record")

        keys = ["farmer_name", "production_year"]
        record_name = []
        if extra:
            record_name.extend(str(item).strip() for item in extra if str(item).strip())
        record_name.extend(
            str(payload.get(key) or "").strip()
            for key in keys
            if str(payload.get(key) or "").strip()
        )

        return " ".join(record_name).strip()
