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
from ..models.enums import LandSizeUnitEnum, LifecycleStageEnum


class G2PSchemaCropSown:

    # Farmer (identified, held in the farmer registry)
    farmer_uuid: Optional[str] = None
    farmer_id: Optional[str] = None
    fayda_fan_id: Optional[str] = None
    farmer_name: Optional[str] = None
    farmer_odk_ack_id: Optional[str] = None

    # Land — flat on the crop sown record; not a register of its own
    land_uuid: Optional[str] = None
    land_id: Optional[str] = None
    is_land_registered: Optional[bool] = None
    ownership_type: Optional[str] = None
    soil_fertility_type: Optional[str] = None
    plot_category: Optional[str] = None
    land_area: Optional[float] = None
    unit: Optional[LandSizeUnitEnum] = None
    sub_kebele: Optional[str] = None

    # Record lifecycle & field staff
    status: Optional[str] = None
    production_year: Optional[str] = None
    lifecycle_stage: Optional[LifecycleStageEnum] = None
    surveyor_name: Optional[str] = None
    surveyor_mobile_number: Optional[str] = None
    supervisor_name: Optional[str] = None
    supervisor_mobile_number: Optional[str] = None


class G2PRegisterSchemaCropSown(G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema, G2PSchemaCropSown):
    """
    Schema for Crop Sown Record register.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema.
    Attributes inherited from G2PSchemaCropSown are specific to the Crop Sown Record domain,
    and include the land attributes of the single plot the record covers.
    """


class G2PRegisterHistorySchemaCropSown(G2PRegisterHistorySchema, G2PGeoHistorySchema, G2PGeoShapeHistorySchema):
    """
    Schema for Crop Sown Record history.
    Inherits fields from G2PRegisterHistorySchema, G2PGeoHistorySchema, G2PGeoShapeHistorySchema.
    """


class G2PIntakeFormSchemaCropSown(G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema, G2PSchemaCropSown):
    """
    Schema for Crop Sown Record intake form.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema, G2PGeoShapeSchema.
    Attributes inherited from G2PSchemaCropSown are specific to the Crop Sown Record domain and are included in the intake form schema for data collection.
    """
