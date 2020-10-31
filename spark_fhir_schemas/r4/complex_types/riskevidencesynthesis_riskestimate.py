from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class RiskEvidenceSynthesis_RiskEstimate:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.riskevidencesynthesis_precisionestimate import RiskEvidenceSynthesis_PrecisionEstimate
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "value", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "unitOfMeasure",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "denominatorCount",
                    integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "numeratorCount", integer.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "precisionEstimate",
                    ArrayType(
                        RiskEvidenceSynthesis_PrecisionEstimate.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
