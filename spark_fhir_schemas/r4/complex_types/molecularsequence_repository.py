from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri


# noinspection PyPep8Naming
class MolecularSequence_Repository:
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
                StructField("type", StringType(), True),
                StructField("url", uri.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("datasetId", StringType(), True),
                StructField("variantsetId", StringType(), True),
                StructField("readsetId", StringType(), True),
            ]
        )

        return schema
