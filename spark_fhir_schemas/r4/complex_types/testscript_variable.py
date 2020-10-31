from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TestScript_Variable:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.id import id
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
                StructField("name", StringType(), True),
                StructField("defaultValue", StringType(), True),
                StructField("description", StringType(), True),
                StructField("expression", StringType(), True),
                StructField("headerField", StringType(), True),
                StructField("hint", StringType(), True),
                StructField("path", StringType(), True),
                StructField(
                    "sourceId", id.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
