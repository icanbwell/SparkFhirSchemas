from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.questionnaireresponse_answer import QuestionnaireResponse_Answer
from spark_fhir_schemas.r4.complex_types.questionnaireresponse_item import QuestionnaireResponse_Item


class QuestionnaireResponse_Item:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("linkId", StringType(), True),
                StructField("definition", uri.get_schema(), True),
                StructField("text", StringType(), True),
                StructField("answer",ArrayType(QuestionnaireResponse_Answer.get_schema()), True),
                StructField("item",ArrayType(QuestionnaireResponse_Item.get_schema()), True),
            ]
        )

        return schema
