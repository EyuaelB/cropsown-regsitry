from datetime import date
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

    is_plot_not_registered: Optional[bool] = None
    temporary_land_id: Optional[str] = None
    sync_id: Optional[str] = None
    start_gc: Optional[date] = None
    start_month: Optional[int] = None
    start_day: Optional[int] = None
    end_gc: Optional[date] = None
    end_month: Optional[int] = None
    end_day: Optional[int] = None
    cluster_id: Optional[str] = None
    cluster_area_timad: Optional[float] = None
    gps_location: Optional[str] = None
    cluster_plan: Optional[float] = None
    cluster_collected_land: Optional[float] = None
    cluster_collected_quintal: Optional[float] = None
    cluster_participant_farmers: Optional[int] = None
    collected_land_quintal: Optional[float] = None
    collected_by_combiner: Optional[float] = None
    actual_cluster_plan: Optional[float] = None
    actual_cluster_collected_land: Optional[float] = None
    actual_cluster_collected_quintal: Optional[float] = None
    actual_cluster_participant_farmers: Optional[int] = None
    actual_collected_land: Optional[float] = None
    actual_collected_land_quintal: Optional[float] = None
    actual_collected_by_combiner: Optional[float] = None
    is_actual: Optional[bool] = None
    land_id: Optional[str] = None
    is_land_registered: Optional[bool] = None
    ownership_type: Optional[str] = None
    soil_fertility_type: Optional[str] = None
    plot_category: Optional[str] = None
    land_area: Optional[float] = None
    unit: Optional[str] = None
    sub_kebele: Optional[str] = None
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
