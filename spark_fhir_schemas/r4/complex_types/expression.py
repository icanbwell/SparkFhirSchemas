from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.uri import uri


# noinspection PyPep8Naming
class Expression:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("description", StringType(), True),
                StructField("name", id.get_schema(), True),
                StructField("language", StringType(), True),
                StructField("expression", StringType(), True),
                StructField("reference", uri.get_schema(), True),
            ]
        )

        return schema
