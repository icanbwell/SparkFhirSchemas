from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.base64binary import base64Binary
from spark_fhir_schemas.r4.complex_types.url import url
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
from spark_fhir_schemas.r4.complex_types.datetime import dateTime


# noinspection PyPep8Naming
class Attachment:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("contentType", code.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("data", base64Binary.get_schema(), True),
                StructField("url", url.get_schema(), True),
                StructField("size", unsignedInt.get_schema(), True),
                StructField("hash", base64Binary.get_schema(), True),
                StructField("title", StringType(), True),
                StructField("creation", dateTime.get_schema(), True),
            ]
        )

        return schema
