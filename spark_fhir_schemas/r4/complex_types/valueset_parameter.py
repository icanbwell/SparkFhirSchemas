from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ValueSet_Parameter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
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
                StructField("valueString", StringType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueDecimal", IntegerType(), True),
                StructField("valueUri", StringType(), True),
                StructField("valueCode", StringType(), True),
                StructField("valueDateTime", StringType(), True),
            ]
        )

        return schema
