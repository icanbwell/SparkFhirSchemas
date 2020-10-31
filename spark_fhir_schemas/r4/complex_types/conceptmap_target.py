from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ConceptMap_Target:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.conceptmap_dependson import ConceptMap_DependsOn
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
                StructField("equivalence", StringType(), True),
                StructField("comment", StringType(), True),
                StructField(
                    "dependsOn",
                    ArrayType(
                        ConceptMap_DependsOn.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "product",
                    ArrayType(
                        ConceptMap_DependsOn.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
