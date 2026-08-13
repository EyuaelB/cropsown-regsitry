from datetime import date
from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PRegisterHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import SeedClassEnum, SowingStatusEnum


class G2PSchemaSowing:

    land_uuid: Optional[str] = None
    season: Optional[str] = None
    commodity: Optional[str] = None
    crop_variety: Optional[str] = None
    crop_category: Optional[str] = None
    sowing_status: Optional[SowingStatusEnum] = None
    area_sown: Optional[float] = None
    sowing_date: Optional[date] = None
    seed_class: Optional[SeedClassEnum] = None
    actual_seed_qty: Optional[float] = None
    fertilizer_type: Optional[str] = None
    fertilizer_qty: Optional[float] = None
    cultivated_by: Optional[str] = None
    cluster_status: Optional[str] = None
    has_pest_disease: Optional[bool] = None


class G2PRegisterSchemaSowing(G2PRegisterBaseSchema, G2PSchemaSowing):
    """
    Schema for Sowing register.
    Inherits fields from G2PRegisterBaseSchema.
    Attributes inherited from G2PSchemaSowing are specific to the Sowing domain.
    """


class G2PRegisterHistorySchemaSowing(G2PRegisterHistorySchema):
    """
    Schema for Sowing history.
    Inherits fields from G2PRegisterHistorySchema.
    """


class G2PIntakeFormSchemaSowing(G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PSchemaSowing):
    """
    Schema for Sowing intake form.
    Inherits fields from G2PRegisterBaseSchema.
    Attributes inherited from G2PSchemaSowing are specific to the Sowing domain and are included in the intake form schema for data collection.
    """
