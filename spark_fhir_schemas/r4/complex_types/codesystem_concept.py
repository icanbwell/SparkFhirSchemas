from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class CodeSystem_Concept:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.codesystem_designation import CodeSystem_Designation
        from spark_fhir_schemas.r4.complex_types.codesystem_property1 import CodeSystem_Property1
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
                    "code", code.get_schema(recursion_depth + 1), True
                ),
                StructField("display", StringType(), True),
                StructField("definition", StringType(), True),
                StructField(
                    "designation",
                    ArrayType(
                        CodeSystem_Designation.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "property",
                    ArrayType(
                        CodeSystem_Property1.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "concept",
                    ArrayType(
                        CodeSystem_Concept.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
