from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ExampleScenario_Process:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.examplescenario_step import ExampleScenario_Step
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
                StructField("title", StringType(), True),
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "preConditions", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "postConditions", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "step",
                    ArrayType(
                        ExampleScenario_Step.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
