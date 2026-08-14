"""Cultivation / Land Preparation lines — a child of CROP_SOWN_RECORDS.

The ERD links every crop line straight to the crop sown record, so this register
sits directly under CropSown with no intermediate land/sowing level; the plot it
applies to is named by `land_uuid` (the stable generated key, not shown in
the UI) and carries the operator-facing `land_id` alongside it.
"""

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from sqlalchemy import Date, Integer, Numeric, String, select
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServiceCultivation
from .enums import CroppingSystemEnum, SeedClassEnum, SeedSourceEnum


class G2PCultivation:

    land_uuid: Mapped[str] = mapped_column(String, nullable=True)
    land_id: Mapped[str] = mapped_column(String, nullable=True)
    season: Mapped[str] = mapped_column(String, nullable=True)                # Attribute lookup (CROP_SEASON)
    commodity: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (CROP_COMMODITY)
    crop_variety: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (CROP_VARIETY)
    crop_category: Mapped[str] = mapped_column(String, nullable=True)         # Attribute lookup (CROP_CATEGORY)
    land_prep_method: Mapped[str] = mapped_column(String, nullable=True)      # Attribute lookup (LAND_PREP_METHOD)
    cultivation_type: Mapped[str] = mapped_column(String, nullable=True)      # Attribute lookup (MACHINERY)
    cropping_system: Mapped[CroppingSystemEnum] = mapped_column(String, nullable=True) # CroppingSystemEnum
    actual_planted_date: Mapped[str] = mapped_column(Date, nullable=True)
    actual_crop_area: Mapped[float] = mapped_column(Numeric, nullable=True)
    actual_growth_duration_days: Mapped[int] = mapped_column(Integer, nullable=True)
    actual_seed_class: Mapped[SeedClassEnum] = mapped_column(String, nullable=True) # SeedClassEnum
    actual_seed_source: Mapped[SeedSourceEnum] = mapped_column(String, nullable=True) # SeedSourceEnum
    actual_seed_qty: Mapped[float] = mapped_column(Numeric, nullable=True)
    actual_fertilizer_type: Mapped[str] = mapped_column(String, nullable=True) # Attribute lookup (FERTILIZER_TYPE)
    actual_fertilizer_qty: Mapped[float] = mapped_column(Numeric, nullable=True)
    water_source: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (WATER_SOURCE)
    remark: Mapped[str] = mapped_column(String, nullable=True)


# All Register classes should have the prefix G2PRegister
class G2PRegisterCultivation(G2PRegister, G2PCultivation):
    __tablename__ = "g2p_register_cultivations"

    def get_search_text_fields(self) -> str:
        """Return cultivation / land preparation fields used to build search_text."""
        return G2PRegisterDomainServiceCultivation().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return cultivation / land preparation record_name from domain service implementation."""
        return G2PRegisterDomainServiceCultivation().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryCultivation(G2PRegisterHistory, G2PCultivation):
    __tablename__ = "g2p_register_history_cultivations"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormCultivation(G2PIntakeForm, G2PRegister, G2PCultivation):
    __tablename__ = "g2p_intake_form_cultivations"

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
        """Return cultivation / land preparation fields used to build search_text."""
        return G2PRegisterDomainServiceCultivation().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return cultivation / land preparation record_name from domain service implementation."""
        return G2PRegisterDomainServiceCultivation().construct_record_name(self.to_dict())
