from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PGeoSchema,
    G2PGeoShapeSchema,
    G2PRegisterHistorySchema,
    G2PGeoHistorySchema,
    G2PGeoShapeHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import LandSizeUnitEnum


class G2PSchemaLand:

    land_uuid: Optional[str] = None
    land_id: Optional[str] = None
    is_land_registered: Optional[bool] = None
    ownership_type: Optional[str] = None
    soil_fertility_type: Optional[str] = None
    plot_category: Optional[str] = None
    land_area: Optional[float] = None
    unit: Optional[LandSizeUnitEnum] = None
    sub_kebele: Optional[str] = None


class G2PRegisterSchemaLand(G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema, G2PSchemaLand):
    """
    Schema for Land register.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema.
    Attributes inherited from G2PSchemaLand are specific to the Land domain.
    """


class G2PRegisterHistorySchemaLand(G2PRegisterHistorySchema, G2PGeoHistorySchema, G2PGeoShapeHistorySchema):
    """
    Schema for Land history.
    Inherits fields from G2PRegisterHistorySchema, G2PGeoHistorySchema, G2PGeoShapeHistorySchema.
    """


class G2PIntakeFormSchemaLand(G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema, G2PSchemaLand):
    """
    Schema for Land intake form.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema.
    Attributes inherited from G2PSchemaLand are specific to the Land domain and are included in the intake form schema for data collection.
    """
