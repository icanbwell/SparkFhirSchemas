from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ObservationDefinition_QualifiedInterval:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
                StructField("category", StringType(), True),
                StructField(
                    "range", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "context", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "appliesTo",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("gender", StringType(), True),
                StructField(
                    "age", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "gestationalAge", Range.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("condition", StringType(), True),
            ]
        )

        return schema
