from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.base64binary import base64Binary
from spark_fhir_schemas.r4.complex_types.auditevent_detail import AuditEvent_Detail


# noinspection PyPep8Naming
class AuditEvent_Entity:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("what", Reference.get_schema(), True),
                StructField("type", Coding.get_schema(), True),
                StructField("role", Coding.get_schema(), True),
                StructField("lifecycle", Coding.get_schema(), True),
                StructField(
                    "securityLabel", ArrayType(Coding.get_schema()), True
                ),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField("query", base64Binary.get_schema(), True),
                StructField(
                    "detail", ArrayType(AuditEvent_Detail.get_schema()), True
                ),
            ]
        )

        return schema
