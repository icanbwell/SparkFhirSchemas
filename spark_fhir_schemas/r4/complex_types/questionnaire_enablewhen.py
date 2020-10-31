from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Questionnaire_EnableWhen:
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
                StructField("question", StringType(), True),
                StructField("operator", StringType(), True),
                StructField("answerBoolean", BooleanType(), True),
                StructField("answerDecimal", IntegerType(), True),
                StructField("answerInteger", IntegerType(), True),
                StructField("answerDate", StringType(), True),
                StructField("answerDateTime", StringType(), True),
                StructField("answerTime", StringType(), True),
                StructField("answerString", StringType(), True),
                StructField("answerCoding", Coding.get_schema(), True),
                StructField("answerQuantity", Quantity.get_schema(), True),
                StructField("answerReference", Reference.get_schema(), True),
            ]
        )

        return schema
