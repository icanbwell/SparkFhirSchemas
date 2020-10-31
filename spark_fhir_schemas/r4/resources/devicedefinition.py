from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.devicedefinition_udideviceidentifier import DeviceDefinition_UdiDeviceIdentifier
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.devicedefinition_devicename import DeviceDefinition_DeviceName
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.devicedefinition_specialization import DeviceDefinition_Specialization
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.productshelflife import ProductShelfLife
from spark_fhir_schemas.r4.resources.prodcharacteristic import ProdCharacteristic
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.devicedefinition_capability import DeviceDefinition_Capability
from spark_fhir_schemas.r4.resources.devicedefinition_property import DeviceDefinition_Property
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.contactpoint import ContactPoint
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.annotation import Annotation
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.devicedefinition_material import DeviceDefinition_Material


class DeviceDefinition:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("udiDeviceIdentifier",ArrayType(DeviceDefinition_UdiDeviceIdentifier.get_schema()), True),
                StructField("manufacturerString", StringType(), True),
                StructField("manufacturerReference", Reference.get_schema(), True),
                StructField("deviceName",ArrayType(DeviceDefinition_DeviceName.get_schema()), True),
                StructField("modelNumber", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("specialization",ArrayType(DeviceDefinition_Specialization.get_schema()), True),
                StructField("version",ArrayType(string.get_schema()), True),
                StructField("safety",ArrayType(CodeableConcept.get_schema()), True),
                StructField("shelfLifeStorage",ArrayType(ProductShelfLife.get_schema()), True),
                StructField("physicalCharacteristics", ProdCharacteristic.get_schema(), True),
                StructField("languageCode",ArrayType(CodeableConcept.get_schema()), True),
                StructField("capability",ArrayType(DeviceDefinition_Capability.get_schema()), True),
                StructField("property",ArrayType(DeviceDefinition_Property.get_schema()), True),
                StructField("owner", Reference.get_schema(), True),
                StructField("contact",ArrayType(ContactPoint.get_schema()), True),
                StructField("url", uri.get_schema(), True),
                StructField("onlineInformation", uri.get_schema(), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("parentDevice", Reference.get_schema(), True),
                StructField("material",ArrayType(DeviceDefinition_Material.get_schema()), True),]
        )

        return schema
