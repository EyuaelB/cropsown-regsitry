"""REGISTER_LAND — the land a crop sown record is worked on.

Its own root register, as the ERD draws it: independent of any one crop sown
record, which merely points at it by `land_uuid`.

Two identifiers on purpose:
  * `land_uuid` is generated here and never typed — it is the stable key the
    crop sown record and every crop line reference;
  * `land_id` is the human one an operator reads off a certificate
    (e.g. OR/01/02/003/00001).
"""

import uuid

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoShape,
    G2PGeoHistory, G2PGeoShapeHistory
)
from sqlalchemy import Boolean, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServiceLand
from .enums import LandSizeUnitEnum


class G2PLand:

    land_uuid: Mapped[str] = mapped_column(
        String, nullable=True, index=True, default=lambda: str(uuid.uuid4())
    )
    land_id: Mapped[str] = mapped_column(String, nullable=True)
    is_land_registered: Mapped[bool] = mapped_column(Boolean, nullable=True)
    ownership_type: Mapped[str] = mapped_column(String, nullable=True)        # Attribute lookup (OWNERSHIP_TYPE)
    soil_fertility_type: Mapped[str] = mapped_column(String, nullable=True)   # Attribute lookup (SOIL_FERTILITY)
    plot_category: Mapped[str] = mapped_column(String, nullable=True)         # Attribute lookup (PLOT_CATEGORY)
    land_area: Mapped[float] = mapped_column(Numeric, nullable=True)
    unit: Mapped[LandSizeUnitEnum] = mapped_column(String, nullable=True)     # LandSizeUnitEnum
    sub_kebele: Mapped[str] = mapped_column(String, nullable=True)


# All Register classes should have the prefix G2PRegister
class G2PRegisterLand(G2PRegister, G2PGeo, G2PGeoShape, G2PLand):
    __tablename__ = "g2p_register_lands"

    def get_search_text_fields(self) -> str:
        """Return land fields used to build search_text."""
        return G2PRegisterDomainServiceLand().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return land record_name from domain service implementation."""
        return G2PRegisterDomainServiceLand().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryLand(G2PRegisterHistory, G2PGeoHistory, G2PGeoShapeHistory, G2PLand):
    __tablename__ = "g2p_register_history_lands"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormLand(G2PIntakeForm, G2PRegister, G2PGeo, G2PGeoShape, G2PLand):
    __tablename__ = "g2p_intake_form_lands"

    def get_search_text_fields(self) -> str:
        """Return land fields used to build search_text."""
        return G2PRegisterDomainServiceLand().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return land record_name from domain service implementation."""
        return G2PRegisterDomainServiceLand().construct_record_name(self.to_dict())
