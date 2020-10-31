from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier


# noinspection PyPep8Naming
class SubstanceNucleicAcid_Linkage:
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
                StructField("connectivity", StringType(), True),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("residueSite", StringType(), True),
            ]
        )

        return schema
