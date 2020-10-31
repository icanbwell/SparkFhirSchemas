from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TestScript_Assert:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.id import id
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
                StructField("label", StringType(), True),
                StructField("description", StringType(), True),
                StructField("direction", StringType(), True),
                StructField("compareToSourceId", StringType(), True),
                StructField("compareToSourceExpression", StringType(), True),
                StructField("compareToSourcePath", StringType(), True),
                StructField(
                    "contentType", code.get_schema(recursion_depth + 1), True
                ),
                StructField("expression", StringType(), True),
                StructField("headerField", StringType(), True),
                StructField("minimumId", StringType(), True),
                StructField("navigationLinks", BooleanType(), True),
                StructField("operator", StringType(), True),
                StructField("path", StringType(), True),
                StructField("requestMethod", StringType(), True),
                StructField("requestURL", StringType(), True),
                StructField(
                    "resource", code.get_schema(recursion_depth + 1), True
                ),
                StructField("response", StringType(), True),
                StructField("responseCode", StringType(), True),
                StructField(
                    "sourceId", id.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "validateProfileId", id.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("value", StringType(), True),
                StructField("warningOnly", BooleanType(), True),
            ]
        )
        return schema
