from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.riskevidencesynthesis_precisionestimate import RiskEvidenceSynthesis_PrecisionEstimate


# noinspection PyPep8Naming
class RiskEvidenceSynthesis_RiskEstimate:
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
                StructField("value", decimal.get_schema(), True),
                StructField(
                    "unitOfMeasure", CodeableConcept.get_schema(), True
                ),
                StructField("denominatorCount", integer.get_schema(), True),
                StructField("numeratorCount", integer.get_schema(), True),
                StructField(
                    "precisionEstimate",
                    ArrayType(
                        RiskEvidenceSynthesis_PrecisionEstimate.get_schema()
                    ), True
                ),
            ]
        )

        return schema
