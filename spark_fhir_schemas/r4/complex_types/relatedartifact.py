from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class RelatedArtifact:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.simple_types.url import url
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
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
                StructField("type", StringType(), True),
                StructField("label", StringType(), True),
                StructField("display", StringType(), True),
                StructField(
                    "citation", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField("url", url.get_schema(recursion_depth + 1), True),
                StructField(
                    "document", Attachment.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "resource", canonical.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
