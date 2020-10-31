from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.device_udicarrier import Device_UdiCarrier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.device_devicename import Device_DeviceName
from spark_fhir_schemas.r4.complex_types.device_specialization import Device_Specialization
from spark_fhir_schemas.r4.complex_types.device_version import Device_Version
from spark_fhir_schemas.r4.complex_types.device_property import Device_Property
from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
from spark_fhir_schemas.r4.complex_types.annotation import Annotation


# noinspection PyPep8Naming
class Device:
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
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("definition", Reference.get_schema(), True),
                StructField(
                    "udiCarrier", ArrayType(Device_UdiCarrier.get_schema()),
                    True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "statusReason", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("distinctIdentifier", StringType(), True),
                StructField("manufacturer", StringType(), True),
                StructField("manufactureDate", dateTime.get_schema(), True),
                StructField("expirationDate", dateTime.get_schema(), True),
                StructField("lotNumber", StringType(), True),
                StructField("serialNumber", StringType(), True),
                StructField(
                    "deviceName", ArrayType(Device_DeviceName.get_schema()),
                    True
                ),
                StructField("modelNumber", StringType(), True),
                StructField("partNumber", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField(
                    "specialization",
                    ArrayType(Device_Specialization.get_schema()), True
                ),
                StructField(
                    "version", ArrayType(Device_Version.get_schema()), True
                ),
                StructField(
                    "property", ArrayType(Device_Property.get_schema()), True
                ),
                StructField("patient", Reference.get_schema(), True),
                StructField("owner", Reference.get_schema(), True),
                StructField(
                    "contact", ArrayType(ContactPoint.get_schema()), True
                ),
                StructField("location", Reference.get_schema(), True),
                StructField("url", uri.get_schema(), True),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField(
                    "safety", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("parent", Reference.get_schema(), True),
            ]
        )

        return schema
