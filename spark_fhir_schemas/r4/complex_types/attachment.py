from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Attachment:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.base64binary import base64Binary
        from spark_fhir_schemas.r4.simple_types.url import url
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
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
                    "contentType", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "data", base64Binary.get_schema(recursion_depth + 1), True
                ),
                StructField("url", url.get_schema(recursion_depth + 1), True),
                StructField(
                    "size", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "hash", base64Binary.get_schema(recursion_depth + 1), True
                ),
                StructField("title", StringType(), True),
                StructField(
                    "creation", dateTime.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
