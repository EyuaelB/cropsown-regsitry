from typing import Optional

from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema,
    G2PGeoSchema,
    G2PRegisterHistorySchema,
    G2PGeoHistorySchema,
    G2PIntakeFormSchemaBase,
)
from ..models.enums import LifecycleStageEnum


class G2PSchemaCropSown:

    farmer_uuid: Optional[str] = None
    farmer_id: Optional[str] = None
    fayda_fan_id: Optional[str] = None
    farmer_name: Optional[str] = None
    land_uuid: Optional[str] = None
    status: Optional[str] = None
    production_year: Optional[str] = None
    lifecycle_stage: Optional[LifecycleStageEnum] = None
    surveyor_name: Optional[str] = None
    surveyor_mobile_number: Optional[str] = None
    supervisor_name: Optional[str] = None
    supervisor_mobile_number: Optional[str] = None


class G2PRegisterSchemaCropSown(G2PRegisterBaseSchema, G2PGeoSchema, G2PSchemaCropSown):
    """
    Schema for Crop Sown Record register.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema.
    Attributes inherited from G2PSchemaCropSown are specific to the Crop Sown Record domain.
    """


class G2PRegisterHistorySchemaCropSown(G2PRegisterHistorySchema, G2PGeoHistorySchema):
    """
    Schema for Crop Sown Record history.
    Inherits fields from G2PRegisterHistorySchema, G2PGeoHistorySchema.
    """


class G2PIntakeFormSchemaCropSown(G2PIntakeFormSchemaBase, G2PRegisterBaseSchema, G2PGeoSchema, G2PSchemaCropSown):
    """
    Schema for Crop Sown Record intake form.
    Inherits fields from G2PRegisterBaseSchema, G2PGeoSchema.
    Attributes inherited from G2PSchemaCropSown are specific to the Crop Sown Record domain and are included in the intake form schema for data collection.
    """
