from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.url import url


# noinspection PyPep8Naming
class ImplementationGuide_Resource1:
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
                StructField("reference", Reference.get_schema(), True),
                StructField("exampleBoolean", BooleanType(), True),
                StructField("exampleCanonical", StringType(), True),
                StructField("relativePath", url.get_schema(), True),
            ]
        )

        return schema
