"""Crop Planning lines — a child of CROP_SOWN_RECORDS.

The ERD links every crop line straight to the crop sown record, so this register
sits directly under CropSown with no intermediate land/sowing level; the plot it
applies to is named by `land_uuid` (the stable generated key, not shown in
the UI) and carries the operator-facing `land_id` alongside it.
"""

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from sqlalchemy import Date, Integer, Numeric, String, select
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServicePlanning
from .enums import CroppingSystemEnum, SeedClassEnum, SeedSourceEnum


class G2PPlanning:

    land_uuid: Mapped[str] = mapped_column(String, nullable=True)
    land_id: Mapped[str] = mapped_column(String, nullable=True)
    season: Mapped[str] = mapped_column(String, nullable=True)                # Attribute lookup (CROP_SEASON)
    commodity: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (CROP_COMMODITY)
    crop_variety: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (CROP_VARIETY)
    crop_category: Mapped[str] = mapped_column(String, nullable=True)         # Attribute lookup (CROP_CATEGORY)
    local_name: Mapped[str] = mapped_column(String, nullable=True)
    scientific_name: Mapped[str] = mapped_column(String, nullable=True)
    plot_category: Mapped[str] = mapped_column(String, nullable=True)         # Attribute lookup (PLOT_CATEGORY)
    cropping_system: Mapped[CroppingSystemEnum] = mapped_column(String, nullable=True) # CroppingSystemEnum
    planned_date: Mapped[str] = mapped_column(Date, nullable=True)
    planned_area: Mapped[float] = mapped_column(Numeric, nullable=True)
    growth_duration_days: Mapped[int] = mapped_column(Integer, nullable=True)
    expected_yield: Mapped[float] = mapped_column(Numeric, nullable=True)
    seed_class: Mapped[SeedClassEnum] = mapped_column(String, nullable=True)  # SeedClassEnum
    seed_source: Mapped[SeedSourceEnum] = mapped_column(String, nullable=True) # SeedSourceEnum
    planned_seed_qty: Mapped[float] = mapped_column(Numeric, nullable=True)
    planned_fertilizer_type: Mapped[str] = mapped_column(String, nullable=True) # Attribute lookup (FERTILIZER_TYPE)
    planned_fertilizer_qty: Mapped[float] = mapped_column(Numeric, nullable=True)
    planned_labor: Mapped[int] = mapped_column(Integer, nullable=True)
    water_source: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (WATER_SOURCE)
    cluster_status: Mapped[str] = mapped_column(String, nullable=True)        # Attribute lookup (CLUSTER_STATUS)


# All Register classes should have the prefix G2PRegister
class G2PRegisterPlanning(G2PRegister, G2PPlanning):
    __tablename__ = "g2p_register_plannings"

    def get_search_text_fields(self) -> str:
        """Return crop planning fields used to build search_text."""
        return G2PRegisterDomainServicePlanning().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return crop planning record_name from domain service implementation."""
        return G2PRegisterDomainServicePlanning().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryPlanning(G2PRegisterHistory, G2PPlanning):
    __tablename__ = "g2p_register_history_plannings"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormPlanning(G2PIntakeForm, G2PRegister, G2PPlanning):
    __tablename__ = "g2p_intake_form_plannings"

    async def get_link_internal_record_id(self, session):
        from .crop_sown import G2PIntakeFormCropSown
        result = await session.execute(
            select(G2PIntakeFormCropSown).where(
                G2PIntakeFormCropSown.submission_id == self.submission_id
            )
        )
        crop_sown = result.scalars().first()
        if crop_sown:
            self.link_internal_record_id = crop_sown.internal_record_id

    def get_search_text_fields(self) -> str:
        """Return crop planning fields used to build search_text."""
        return G2PRegisterDomainServicePlanning().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return crop planning record_name from domain service implementation."""
        return G2PRegisterDomainServicePlanning().construct_record_name(self.to_dict())
