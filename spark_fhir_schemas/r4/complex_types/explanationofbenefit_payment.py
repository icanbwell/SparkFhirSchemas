from pyspark.sql.types import ArrayType, DateType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ExplanationOfBenefit_Payment:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
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
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "adjustment", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "adjustmentReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("date", DateType(), True),
                StructField(
                    "amount", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
