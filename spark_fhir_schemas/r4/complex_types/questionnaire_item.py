from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Questionnaire_Item:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.questionnaire_enablewhen import Questionnaire_EnableWhen
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.questionnaire_answeroption import Questionnaire_AnswerOption
        from spark_fhir_schemas.r4.complex_types.questionnaire_initial import Questionnaire_Initial
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                StructField(
                    "code", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("prefix", StringType(), True),
                StructField("text", StringType(), True),
                StructField("type", StringType(), True),
                StructField(
                    "enableWhen",
                    ArrayType(
                        Questionnaire_EnableWhen.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("enableBehavior", StringType(), True),
                StructField("required", BooleanType(), True),
                StructField("repeats", BooleanType(), True),
                StructField("readOnly", BooleanType(), True),
                StructField(
                    "maxLength", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "answerValueSet",
                    canonical.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "answerOption",
                    ArrayType(
                        Questionnaire_AnswerOption.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "initial",
                    ArrayType(
                        Questionnaire_Initial.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "item",
                    ArrayType(
                        Questionnaire_Item.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
