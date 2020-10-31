from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ClaimResponse_Error:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
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
                StructField(
                    "itemSequence",
                    positiveInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "detailSequence",
                    positiveInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subDetailSequence",
                    positiveInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
