"""Cluster Information lines — a child of CROP_SOWN_RECORDS.

The ERD links every crop line straight to the crop sown record, so this register
sits directly under CropSown with no intermediate land/sowing level; the land it
applies to is named by `land_uuid`.
"""

from openg2p_registry_core.models.g2p_intake_form import G2PIntakeForm
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory, G2PGeo, G2PGeoHistory
from sqlalchemy import Integer, Numeric, String, select
from sqlalchemy.orm import Mapped, mapped_column

from ..services import G2PRegisterDomainServiceCluster
from .enums import AgroEcologicalZoneEnum


class G2PCluster:

    cluster_name: Mapped[str] = mapped_column(String, nullable=True)
    cluster_status: Mapped[str] = mapped_column(String, nullable=True)        # Attribute lookup (CLUSTER_STATUS)
    agro_ecological_zone: Mapped[AgroEcologicalZoneEnum] = mapped_column(String, nullable=True) # AgroEcologicalZoneEnum
    season: Mapped[str] = mapped_column(String, nullable=True)                # Attribute lookup (CROP_SEASON)
    commodity: Mapped[str] = mapped_column(String, nullable=True)             # Attribute lookup (CROP_COMMODITY)
    sub_kebele: Mapped[str] = mapped_column(String, nullable=True)
    cluster_area_hectare: Mapped[float] = mapped_column(Numeric, nullable=True)
    number_of_smallholders: Mapped[int] = mapped_column(Integer, nullable=True)
    participant_farmers: Mapped[int] = mapped_column(Integer, nullable=True)
    collected_land: Mapped[float] = mapped_column(Numeric, nullable=True)
    collected_quintal: Mapped[float] = mapped_column(Numeric, nullable=True)
    water_source: Mapped[str] = mapped_column(String, nullable=True)          # Attribute lookup (WATER_SOURCE)


# All Register classes should have the prefix G2PRegister
class G2PRegisterCluster(G2PRegister, G2PGeo, G2PCluster):
    __tablename__ = "g2p_register_clusters"

    def get_search_text_fields(self) -> str:
        """Return cluster information fields used to build search_text."""
        return G2PRegisterDomainServiceCluster().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return cluster information record_name from domain service implementation."""
        return G2PRegisterDomainServiceCluster().construct_record_name(self.to_dict())


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryCluster(G2PRegisterHistory, G2PGeoHistory, G2PCluster):
    __tablename__ = "g2p_register_history_clusters"


# All Intake Form classes should have the prefix G2PIntakeForm
class G2PIntakeFormCluster(G2PIntakeForm, G2PRegister, G2PGeo, G2PCluster):
    __tablename__ = "g2p_intake_form_clusters"

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
        """Return cluster information fields used to build search_text."""
        return G2PRegisterDomainServiceCluster().construct_search_text(self.to_dict())

    def get_record_name_fields(self) -> str:
        """Return cluster information record_name from domain service implementation."""
        return G2PRegisterDomainServiceCluster().construct_record_name(self.to_dict())
