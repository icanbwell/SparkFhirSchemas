from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TestScript_Capability:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
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
                StructField("required", BooleanType(), True),
                StructField("validated", BooleanType(), True),
                StructField("description", StringType(), True),
                StructField(
                    "origin",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "destination", integer.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "link", ArrayType(uri.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "capabilities", canonical.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
