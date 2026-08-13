"""Harvest lines — a child of CROP_SOWN_RECORDS.

The ERD links every crop line straight to the crop sown record, so this register
sits directly under CropSown with no intermediate land/sowing level; the land it
applies to is named by `land_uuid`.
"""

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from sqlalchemy import Date, Numeric, String, select
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServiceHarvest
from .enums import CropMaturityStatusEnum


class G2PHarvest:

    land_uuid: Mapped[str] = mapped_column(String, nullable=True)
    commodity: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (CROP_COMMODITY)
    crop_maturity_status: Mapped[CropMaturityStatusEnum] = mapped_column(String, nullable=True) # CropMaturityStatusEnum
    harvest_date: Mapped[str] = mapped_column(Date, nullable=True)
    area_harvested: Mapped[float] = mapped_column(Numeric, nullable=True)
    qty_harvested: Mapped[float] = mapped_column(Numeric, nullable=True)
    post_harvest_loss_pct: Mapped[float] = mapped_column(Numeric, nullable=True)
    qty_stored: Mapped[float] = mapped_column(Numeric, nullable=True)
    qty_sold: Mapped[float] = mapped_column(Numeric, nullable=True)
    yield_per_ha: Mapped[float] = mapped_column(Numeric, nullable=True)
    harvested_by: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (MACHINERY)


# All Register classes should have the prefix G2PRegister
class G2PRegisterHarvest(G2PRegister, G2PHarvest):
    __tablename__ = "g2p_register_harvests"

    def get_search_text_fields(self) -> str:
        """Return harvest fields used to build search_text."""
        return G2PRegisterDomainServiceHarvest().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return harvest record_name from domain service implementation."""
        return G2PRegisterDomainServiceHarvest().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHarvest(G2PRegisterHistory, G2PHarvest):
    __tablename__ = "g2p_register_history_harvests"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormHarvest(G2PIntakeForm, G2PRegister, G2PHarvest):
    __tablename__ = "g2p_intake_form_harvests"

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
        """Return harvest fields used to build search_text."""
        return G2PRegisterDomainServiceHarvest().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return harvest record_name from domain service implementation."""
        return G2PRegisterDomainServiceHarvest().construct_record_name(self.to_dict())
