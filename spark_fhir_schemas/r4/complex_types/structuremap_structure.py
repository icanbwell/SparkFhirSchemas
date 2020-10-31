from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.canonical import canonical


# noinspection PyPep8Naming
class StructureMap_Structure:
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
                StructField("url", canonical.get_schema(), True),
                StructField("mode", StringType(), True),
                StructField("alias", StringType(), True),
                StructField("documentation", StringType(), True),
            ]
        )

        return schema
