from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.ratio import Ratio


# noinspection PyPep8Naming
class MedicinalProductIngredient_ReferenceStrength:
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
                StructField("substance", CodeableConcept.get_schema(), True),
                StructField("strength", Ratio.get_schema(), True),
                StructField("strengthLowLimit", Ratio.get_schema(), True),
                StructField("measurementPoint", StringType(), True),
                StructField(
                    "country", ArrayType(CodeableConcept.get_schema()), True
                ),
            ]
        )

        return schema
