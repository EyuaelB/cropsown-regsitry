from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PRegisterHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import CroppingSystemEnum, SeedClassEnum, SeedSourceEnum


class G2PSchemaPlanning:

    land_uuid: Optional[str] = None
    land_id: Optional[str] = None
    season: Optional[str] = None
    commodity: Optional[str] = None
    crop_variety: Optional[str] = None
    crop_category: Optional[str] = None
    local_name: Optional[str] = None
    scientific_name: Optional[str] = None
    plot_category: Optional[str] = None
    cropping_system: Optional[CroppingSystemEnum] = None
    planned_date: Optional[date] = None
    planned_area: Optional[float] = None
    growth_duration_days: Optional[int] = None
    expected_yield: Optional[float] = None
    seed_class: Optional[SeedClassEnum] = None
    seed_source: Optional[SeedSourceEnum] = None
    planned_seed_qty: Optional[float] = None
    planned_fertilizer_type: Optional[str] = None
    planned_fertilizer_qty: Optional[float] = None
    planned_labor: Optional[int] = None
    water_source: Optional[str] = None
    cluster_status: Optional[str] = None


class G2PRegisterSchemaPlanning(G2PRegisterBaseSchema, G2PSchemaPlanning):
    """
    Schema for Crop Planning register.
    Inherits fields from G2PRegisterBaseSchema.
    Attributes inherited from G2PSchemaPlanning are specific to the Crop Planning domain.
    """


class G2PRegisterHistorySchemaPlanning(G2PRegisterHistorySchema):
    """
    Schema for Crop Planning history.
    Inherits fields from G2PRegisterHistorySchema.
    """


class G2PIntakeFormSchemaPlanning(G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PSchemaPlanning):
    """
    Schema for Crop Planning intake form.
    Inherits fields from G2PRegisterBaseSchema.
    Attributes inherited from G2PSchemaPlanning are specific to the Crop Planning domain and are included in the intake form schema for data collection.
    """
