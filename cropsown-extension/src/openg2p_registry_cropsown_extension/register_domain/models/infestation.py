"""Infestation Incident lines — a child of CROP_SOWN_RECORDS.

The ERD links every crop line straight to the crop sown record, so this register
sits directly under CropSown with no intermediate land/sowing level; the plot it
applies to is named by `land_uuid` (the stable generated key, not shown in
the UI) and carries the operator-facing `land_id` alongside it.
"""

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from sqlalchemy import Date, Numeric, String, select
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServiceInfestation
from .enums import GrowthStageEnum, SeverityLevelEnum


class G2PInfestation:

    land_uuid: Mapped[str] = mapped_column(String, nullable=True)
    land_id: Mapped[str] = mapped_column(String, nullable=True)
    commodity: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (CROP_COMMODITY)
    growth_stage: Mapped[GrowthStageEnum] = mapped_column(String, nullable=True) # GrowthStageEnum
    infestation_type: Mapped[str] = mapped_column(String, nullable=True)      # Attribute lookup (INFESTATION_TYPE)
    pest_name: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (PEST)
    weed_name: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (WEED)
    disease_name: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (CROP_DISEASE)
    chemical_used: Mapped[str] = mapped_column(String, nullable=True)         # Attribute lookup (AGRO_CHEMICAL)
    severity_level: Mapped[SeverityLevelEnum] = mapped_column(String, nullable=True) # SeverityLevelEnum
    estimated_damage_pct: Mapped[float] = mapped_column(Numeric, nullable=True)
    observation_date: Mapped[str] = mapped_column(Date, nullable=True)
    geo_tagged_photo_document_id: Mapped[str] = mapped_column(String, nullable=True)
    action_taken: Mapped[str] = mapped_column(String, nullable=True)


# All Register classes should have the prefix G2PRegister
class G2PRegisterInfestation(G2PRegister, G2PInfestation):
    __tablename__ = "g2p_register_infestations"

    def get_search_text_fields(self) -> str:
        """Return infestation incident fields used to build search_text."""
        return G2PRegisterDomainServiceInfestation().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return infestation incident record_name from domain service implementation."""
        return G2PRegisterDomainServiceInfestation().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryInfestation(G2PRegisterHistory, G2PInfestation):
    __tablename__ = "g2p_register_history_infestations"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormInfestation(G2PIntakeForm, G2PRegister, G2PInfestation):
    __tablename__ = "g2p_intake_form_infestations"

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
        """Return infestation incident fields used to build search_text."""
        return G2PRegisterDomainServiceInfestation().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return infestation incident record_name from domain service implementation."""
        return G2PRegisterDomainServiceInfestation().construct_record_name(self.to_dict())
