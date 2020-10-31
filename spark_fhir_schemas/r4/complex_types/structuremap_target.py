from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class StructureMap_Target:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.structuremap_parameter import StructureMap_Parameter
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
                    "context", id.get_schema(recursion_depth + 1), True
                ),
                StructField("contextType", StringType(), True),
                StructField("element", StringType(), True),
                StructField(
                    "variable", id.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "listRuleId", id.get_schema(recursion_depth + 1), True
                ),
                StructField("transform", StringType(), True),
                StructField(
                    "parameter",
                    ArrayType(
                        StructureMap_Parameter.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
