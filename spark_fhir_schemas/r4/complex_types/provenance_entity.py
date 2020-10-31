from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.provenance_agent import Provenance_Agent


# noinspection PyPep8Naming
class Provenance_Entity:
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
                StructField("role", StringType(), True),
                StructField("what", Reference.get_schema(), True),
                StructField(
                    "agent", ArrayType(Provenance_Agent.get_schema()), True
                ),
            ]
        )

        return schema
