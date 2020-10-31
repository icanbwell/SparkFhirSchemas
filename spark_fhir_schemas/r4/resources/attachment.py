from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.base64binary import base64Binary
from spark_fhir_schemas.r4.resources.url import url
from spark_fhir_schemas.r4.resources.unsignedint import unsignedInt
from spark_fhir_schemas.r4.resources.base64binary import base64Binary
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.datetime import dateTime


class Attachment:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("contentType", code.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("data", base64Binary.get_schema(), True),
                StructField("url", url.get_schema(), True),
                StructField("size", unsignedInt.get_schema(), True),
                StructField("hash", base64Binary.get_schema(), True),
                StructField("title", StringType(), True),
                StructField("creation", dateTime.get_schema(), True),]
        )

        return schema
