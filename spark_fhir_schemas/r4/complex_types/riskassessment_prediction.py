from pyspark.sql.types import ArrayType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class RiskAssessment_Prediction:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.period import Period
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
                StructField(
                    "outcome", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("probabilityDecimal", IntegerType(), True),
                StructField(
                    "probabilityRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "qualitativeRisk",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "relativeRisk", decimal.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "whenPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "whenRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField("rationale", StringType(), True),
            ]
        )

        return schema
