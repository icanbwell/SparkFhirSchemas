from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.base64binary import base64Binary
from spark_fhir_schemas.r4.resources.string import string


class Device_UdiCarrier:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("deviceIdentifier", StringType(), True),
                StructField("issuer", uri.get_schema(), True),
                StructField("jurisdiction", uri.get_schema(), True),
                StructField("carrierAIDC", base64Binary.get_schema(), True),
                StructField("carrierHRF", StringType(), True),
                StructField("entryType", StringType(), True),]
        )

        return schema
