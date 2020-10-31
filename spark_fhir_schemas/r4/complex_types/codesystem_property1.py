from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class CodeSystem_Property1:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.coding import Coding
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
                StructField("valueCode", StringType(), True),
                StructField(
                    "valueCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField("valueString", StringType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField("valueDecimal", IntegerType(), True),
            ]
        )

        return schema
