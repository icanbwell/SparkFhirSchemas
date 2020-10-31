from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.reference import Reference


class Questionnaire_EnableWhen:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
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
                StructField("answerReference", Reference.get_schema(), True),]
        )

        return schema
