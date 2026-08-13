from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PGeoSchema,
    G2PRegisterHistorySchema,
    G2PGeoHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import AgroEcologicalZoneEnum


class G2PSchemaCluster:

    cluster_name: Optional[str] = None
    cluster_status: Optional[str] = None
    agro_ecological_zone: Optional[AgroEcologicalZoneEnum] = None
    season: Optional[str] = None
    commodity: Optional[str] = None
    sub_kebele: Optional[str] = None
    cluster_area_hectare: Optional[float] = None
    number_of_smallholders: Optional[int] = None
    participant_farmers: Optional[int] = None
    collected_land: Optional[float] = None
    collected_quintal: Optional[float] = None
    water_source: Optional[str] = None


class G2PRegisterSchemaCluster(G2PRegisterBaseSchema, G2PGeoSchema, G2PSchemaCluster):
    """
    Schema for Cluster Information register.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema.
    Attributes inherited from G2PSchemaCluster are specific to the Cluster Information domain.
    """


class G2PRegisterHistorySchemaCluster(G2PRegisterHistorySchema, G2PGeoHistorySchema):
    """
    Schema for Cluster Information history.
    Inherits fields from G2PRegisterHistorySchema, G2PGeoHistorySchema.
    """


class G2PIntakeFormSchemaCluster(G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PGeoSchema, G2PSchemaCluster):
    """
    Schema for Cluster Information intake form.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema.
    Attributes inherited from G2PSchemaCluster are specific to the Cluster Information domain and are included in the intake form schema for data collection.
    """
