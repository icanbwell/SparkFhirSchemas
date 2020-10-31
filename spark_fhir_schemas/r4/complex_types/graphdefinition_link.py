from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class GraphDefinition_Link:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.graphdefinition_target import GraphDefinition_Target
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
                StructField("path", StringType(), True),
                StructField("sliceName", StringType(), True),
                StructField(
                    "min", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("max", StringType(), True),
                StructField("description", StringType(), True),
                StructField(
                    "target",
                    ArrayType(
                        GraphDefinition_Target.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
