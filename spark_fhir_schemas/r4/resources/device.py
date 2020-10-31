from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Device:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.device_udicarrier import Device_UdiCarrier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.device_devicename import Device_DeviceName
        from spark_fhir_schemas.r4.complex_types.device_specialization import Device_Specialization
        from spark_fhir_schemas.r4.complex_types.device_version import Device_Version
        from spark_fhir_schemas.r4.complex_types.device_property import Device_Property
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "definition", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "udiCarrier",
                    ArrayType(
                        Device_UdiCarrier.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "statusReason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("distinctIdentifier", StringType(), True),
                StructField("manufacturer", StringType(), True),
                StructField(
                    "manufactureDate",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "expirationDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("lotNumber", StringType(), True),
                StructField("serialNumber", StringType(), True),
                StructField(
                    "deviceName",
                    ArrayType(
                        Device_DeviceName.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("modelNumber", StringType(), True),
                StructField("partNumber", StringType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "specialization",
                    ArrayType(
                        Device_Specialization.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "version",
                    ArrayType(Device_Version.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "property",
                    ArrayType(Device_Property.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "owner", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contact",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "safety",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "parent", Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
