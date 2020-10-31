from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string


class Bundle_Request:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("method", StringType(), True),
                StructField("url", uri.get_schema(), True),
                StructField("ifNoneMatch", StringType(), True),
                StructField("ifModifiedSince", instant.get_schema(), True),
                StructField("ifMatch", StringType(), True),
                StructField("ifNoneExist", StringType(), True),]
        )

        return schema
