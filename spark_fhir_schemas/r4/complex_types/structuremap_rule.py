from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class StructureMap_Rule:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.structuremap_source import StructureMap_Source
        from spark_fhir_schemas.r4.complex_types.structuremap_target import StructureMap_Target
        from spark_fhir_schemas.r4.complex_types.structuremap_dependent import StructureMap_Dependent
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
                StructField("name", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "source",
                    ArrayType(
                        StructureMap_Source.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "target",
                    ArrayType(
                        StructureMap_Target.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "rule",
                    ArrayType(
                        StructureMap_Rule.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "dependent",
                    ArrayType(
                        StructureMap_Dependent.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("documentation", StringType(), True),
            ]
        )

        return schema
