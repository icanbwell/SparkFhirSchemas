from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TestScript_Metadata:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.testscript_link import TestScript_Link
        from spark_fhir_schemas.r4.complex_types.testscript_capability import TestScript_Capability
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
                    "link",
                    ArrayType(TestScript_Link.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "capability",
                    ArrayType(
                        TestScript_Capability.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
