"""CROP_SOWN_RECORDS — the root register and the hub of the ERD.

Every crop line (planning, cultivation, sowing, production, harvesting,
infestation, cluster) links straight back to this record; the ERD draws no
intermediate level.

The farmer is **identified, not owned**: this registry is not the system of
record for farmers, so the record carries their identifiers — and mirrors the
Fayda FAN into the platform's `link_foundational_id`, which exists for exactly
this "belongs to a person held elsewhere" case.

The land is **described here, not registered separately**. Land is not a
register of its own: a crop sown record covers exactly one plot, and that
plot's attributes (and its geometry, via the geo/geo-shape mixins) sit flat on
this record. `land_uuid` is generated here and never typed — it stays the
stable key every crop line references, but it now names a plot described by
this record rather than a row in a separate land register. `land_id` is the
human one an operator reads off a certificate (e.g. OR/01/02/003/00001).
"""

import uuid

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoShape,
    G2PGeoHistory, G2PGeoShapeHistory
)
from sqlalchemy import Boolean, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServiceCropSown
from .enums import LandSizeUnitEnum, LifecycleStageEnum


class G2PCropSown:

    # ── Farmer (identified, held in the farmer registry) ──────────────────────
    farmer_uuid: Mapped[str] = mapped_column(String, nullable=True)
    farmer_id: Mapped[str] = mapped_column(String, nullable=True)
    fayda_fan_id: Mapped[str] = mapped_column(String, nullable=True)
    farmer_name: Mapped[str] = mapped_column(String, nullable=True)
    farmer_odk_ack_id: Mapped[str] = mapped_column(String, nullable=True)

    # ── Land (flat: the plot this record covers, not a register of its own) ───
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

    # ── Record lifecycle & field staff ────────────────────────────────────────
    status: Mapped[str] = mapped_column(String, nullable=True)                # Attribute lookup (APPROVAL_STATUS)
    production_year: Mapped[str] = mapped_column(String, nullable=True)
    lifecycle_stage: Mapped[LifecycleStageEnum] = mapped_column(String, nullable=True)  # LifecycleStageEnum
    surveyor_name: Mapped[str] = mapped_column(String, nullable=True)
    surveyor_mobile_number: Mapped[str] = mapped_column(String, nullable=True)
    supervisor_name: Mapped[str] = mapped_column(String, nullable=True)
    supervisor_mobile_number: Mapped[str] = mapped_column(String, nullable=True)


# All Register classes should have the prefix G2PRegister
class G2PRegisterCropSown(G2PRegister, G2PGeo, G2PGeoShape, G2PCropSown):
    __tablename__ = "g2p_register_crop_sowns"

    def get_search_text_fields(self) -> str:
        """Return crop sown fields used to build search_text."""
        return G2PRegisterDomainServiceCropSown().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return crop sown record_name from domain service implementation."""
        return G2PRegisterDomainServiceCropSown().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryCropSown(G2PRegisterHistory, G2PGeoHistory, G2PGeoShapeHistory, G2PCropSown):
    __tablename__ = "g2p_register_history_crop_sowns"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormCropSown(G2PIntakeForm, G2PRegister, G2PGeo, G2PGeoShape, G2PCropSown):
    __tablename__ = "g2p_intake_form_crop_sowns"

    def get_search_text_fields(self) -> str:
        """Return crop sown fields used to build search_text."""
        return G2PRegisterDomainServiceCropSown().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return crop sown record_name from domain service implementation."""
        return G2PRegisterDomainServiceCropSown().construct_record_name(self.to_dict())
