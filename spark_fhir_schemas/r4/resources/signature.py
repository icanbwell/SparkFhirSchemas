from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.base64binary import base64Binary


class Signature:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("type",ArrayType(Coding.get_schema()), True),
                StructField("when", instant.get_schema(), True),
                StructField("who", Reference.get_schema(), True),
                StructField("onBehalfOf", Reference.get_schema(), True),
                StructField("targetFormat", code.get_schema(), True),
                StructField("sigFormat", code.get_schema(), True),
                StructField("data", base64Binary.get_schema(), True),]
        )

        return schema
