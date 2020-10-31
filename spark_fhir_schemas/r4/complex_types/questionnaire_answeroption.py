from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Questionnaire_AnswerOption:
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
                StructField("valueInteger", IntegerType(), True),
                StructField("valueDate", StringType(), True),
                StructField("valueTime", StringType(), True),
                StructField("valueString", StringType(), True),
                StructField("valueCoding", Coding.get_schema(), True),
                StructField("valueReference", Reference.get_schema(), True),
                StructField("initialSelected", BooleanType(), True),
            ]
        )

        return schema
