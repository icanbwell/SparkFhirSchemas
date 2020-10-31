from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ObservationDefinition_QuantitativeDetails:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.integer import integer
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
                    "customaryUnit",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "unit", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "conversionFactor",
                    decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "decimalPrecision",
                    integer.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
