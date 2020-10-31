from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_precisionestimate import EffectEvidenceSynthesis_PrecisionEstimate


# noinspection PyPep8Naming
class EffectEvidenceSynthesis_EffectEstimate:
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
                StructField("description", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField(
                    "variantState", CodeableConcept.get_schema(), True
                ),
                StructField("value", decimal.get_schema(), True),
                StructField(
                    "unitOfMeasure", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "precisionEstimate",
                    ArrayType(
                        EffectEvidenceSynthesis_PrecisionEstimate.get_schema()
                    ), True
                ),
            ]
        )

        return schema
