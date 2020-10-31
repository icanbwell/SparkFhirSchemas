from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.questionnaire_enablewhen import Questionnaire_EnableWhen
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.questionnaire_answeroption import Questionnaire_AnswerOption
from spark_fhir_schemas.r4.complex_types.questionnaire_initial import Questionnaire_Initial


# noinspection PyPep8Naming
class Questionnaire_Item:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("linkId", StringType(), True),
                StructField("definition", uri.get_schema(), True),
                StructField("code", ArrayType(Coding.get_schema()), True),
                StructField("prefix", StringType(), True),
                StructField("text", StringType(), True),
                StructField("type", StringType(), True),
                StructField(
                    "enableWhen",
                    ArrayType(Questionnaire_EnableWhen.get_schema()), True
                ),
                StructField("enableBehavior", StringType(), True),
                StructField("required", BooleanType(), True),
                StructField("repeats", BooleanType(), True),
                StructField("readOnly", BooleanType(), True),
                StructField("maxLength", integer.get_schema(), True),
                StructField("answerValueSet", canonical.get_schema(), True),
                StructField(
                    "answerOption",
                    ArrayType(Questionnaire_AnswerOption.get_schema()), True
                ),
                StructField(
                    "initial", ArrayType(Questionnaire_Initial.get_schema()),
                    True
                ),
                StructField(
                    "item", ArrayType(Questionnaire_Item.get_schema()), True
                ),
            ]
        )

        return schema
