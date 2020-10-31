from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.instant import instant
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList


# noinspection PyPep8Naming
class Bundle_Response:
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
                StructField("status", StringType(), True),
                StructField("location", uri.get_schema(), True),
                StructField("etag", StringType(), True),
                StructField("lastModified", instant.get_schema(), True),
                StructField("outcome", ResourceList.get_schema(), True),
            ]
        )

        return schema
