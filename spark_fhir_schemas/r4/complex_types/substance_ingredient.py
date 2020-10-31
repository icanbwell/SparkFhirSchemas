from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Substance_Ingredient:
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
                StructField("quantity", Ratio.get_schema(), True),
                StructField(
                    "substanceCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "substanceReference", Reference.get_schema(), True
                ),
            ]
        )

        return schema
