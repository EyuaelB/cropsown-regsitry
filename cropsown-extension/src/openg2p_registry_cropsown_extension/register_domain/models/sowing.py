"""Sowing lines — a child of CROP_SOWN_RECORDS.

The ERD links every crop line straight to the crop sown record, so this register
sits directly under CropSown with no intermediate land/sowing level; the land it
applies to is named by `land_uuid`.
"""

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from sqlalchemy import Boolean, Date, Numeric, String, select
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServiceSowing
from .enums import SeedClassEnum, SowingStatusEnum


class G2PSowing:

    land_uuid: Mapped[str] = mapped_column(String, nullable=True)
    season: Mapped[str] = mapped_column(String, nullable=True)                # Attribute lookup (CROP_SEASON)
    commodity: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (CROP_COMMODITY)
    crop_variety: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (CROP_VARIETY)
    crop_category: Mapped[str] = mapped_column(String, nullable=True)         # Attribute lookup (CROP_CATEGORY)
    sowing_status: Mapped[SowingStatusEnum] = mapped_column(String, nullable=True) # SowingStatusEnum
    area_sown: Mapped[float] = mapped_column(Numeric, nullable=True)
    sowing_date: Mapped[str] = mapped_column(Date, nullable=True)
    seed_class: Mapped[SeedClassEnum] = mapped_column(String, nullable=True)  # SeedClassEnum
    actual_seed_qty: Mapped[float] = mapped_column(Numeric, nullable=True)
    fertilizer_type: Mapped[str] = mapped_column(String, nullable=True)       # Attribute lookup (FERTILIZER_TYPE)
    fertilizer_qty: Mapped[float] = mapped_column(Numeric, nullable=True)
    cultivated_by: Mapped[str] = mapped_column(String, nullable=True)         # Attribute lookup (MACHINERY)
    cluster_status: Mapped[str] = mapped_column(String, nullable=True)        # Attribute lookup (CLUSTER_STATUS)
    has_pest_disease: Mapped[bool] = mapped_column(Boolean, nullable=True)


# All Register classes should have the prefix G2PRegister
class G2PRegisterSowing(G2PRegister, G2PSowing):
    __tablename__ = "g2p_register_sowings"

    def get_search_text_fields(self) -> str:
        """Return sowing fields used to build search_text."""
        return G2PRegisterDomainServiceSowing().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return sowing record_name from domain service implementation."""
        return G2PRegisterDomainServiceSowing().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistorySowing(G2PRegisterHistory, G2PSowing):
    __tablename__ = "g2p_register_history_sowings"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormSowing(G2PIntakeForm, G2PRegister, G2PSowing):
    __tablename__ = "g2p_intake_form_sowings"

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
        """Return sowing fields used to build search_text."""
        return G2PRegisterDomainServiceSowing().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return sowing record_name from domain service implementation."""
        return G2PRegisterDomainServiceSowing().construct_record_name(self.to_dict())
