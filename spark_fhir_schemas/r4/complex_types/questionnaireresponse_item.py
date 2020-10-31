from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class QuestionnaireResponse_Item:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.questionnaireresponse_answer import QuestionnaireResponse_Answer
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
                StructField("linkId", StringType(), True),
                StructField(
                    "definition", uri.get_schema(recursion_depth + 1), True
                ),
                StructField("text", StringType(), True),
                StructField(
                    "answer",
                    ArrayType(
                        QuestionnaireResponse_Answer.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "item",
                    ArrayType(
                        QuestionnaireResponse_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
