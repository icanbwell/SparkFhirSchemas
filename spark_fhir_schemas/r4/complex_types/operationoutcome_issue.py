from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class OperationOutcome_Issue:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
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
                StructField("severity", StringType(), True),
                StructField("code", StringType(), True),
                StructField(
                    "details", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("diagnostics", StringType(), True),
                StructField("location", ArrayType(StringType()), True),
                StructField("expression", ArrayType(StringType()), True),
            ]
        )

        return schema
