from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class AuditEvent_Entity:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.simple_types.base64binary import base64Binary
        from spark_fhir_schemas.r4.complex_types.auditevent_detail import AuditEvent_Detail
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "what", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "type", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "role", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "lifecycle", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "securityLabel",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField(
                    "query", base64Binary.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "detail",
                    ArrayType(
                        AuditEvent_Detail.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
