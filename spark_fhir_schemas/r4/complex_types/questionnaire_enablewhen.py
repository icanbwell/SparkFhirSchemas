from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Questionnaire_EnableWhen:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                StructField("question", StringType(), True),
                StructField("operator", StringType(), True),
                StructField("answerBoolean", BooleanType(), True),
                StructField("answerDecimal", IntegerType(), True),
                StructField("answerInteger", IntegerType(), True),
                StructField("answerDate", StringType(), True),
                StructField("answerDateTime", StringType(), True),
                StructField("answerTime", StringType(), True),
                StructField("answerString", StringType(), True),
                StructField(
                    "answerCoding", Coding.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "answerQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "answerReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
