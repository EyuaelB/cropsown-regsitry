from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PRegisterHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import CroppingSystemEnum, SeedClassEnum, SeedSourceEnum


class G2PSchemaCultivation:

    land_uuid: Optional[str] = None
    season: Optional[str] = None
    commodity: Optional[str] = None
    crop_variety: Optional[str] = None
    crop_category: Optional[str] = None
    land_prep_method: Optional[str] = None
    cultivation_type: Optional[str] = None
    cropping_system: Optional[CroppingSystemEnum] = None
    actual_planted_date: Optional[date] = None
    actual_crop_area: Optional[float] = None
    actual_growth_duration_days: Optional[int] = None
    actual_seed_class: Optional[SeedClassEnum] = None
    actual_seed_source: Optional[SeedSourceEnum] = None
    actual_seed_qty: Optional[float] = None
    actual_fertilizer_type: Optional[str] = None
    actual_fertilizer_qty: Optional[float] = None
    water_source: Optional[str] = None
    remark: Optional[str] = None


class G2PRegisterSchemaCultivation(G2PRegisterBaseSchema, G2PSchemaCultivation):
    """
    Schema for Cultivation / Land Preparation register.
    Inherits fields from G2PRegisterBaseSchema.
    Attributes inherited from G2PSchemaCultivation are specific to the Cultivation / Land Preparation domain.
    """


class G2PRegisterHistorySchemaCultivation(G2PRegisterHistorySchema):
    """
    Schema for Cultivation / Land Preparation history.
    Inherits fields from G2PRegisterHistorySchema.
    """


class G2PIntakeFormSchemaCultivation(G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PSchemaCultivation):
    """
    Schema for Cultivation / Land Preparation intake form.
    Inherits fields from G2PRegisterBaseSchema.
    Attributes inherited from G2PSchemaCultivation are specific to the Cultivation / Land Preparation domain and are included in the intake form schema for data collection.
    """
