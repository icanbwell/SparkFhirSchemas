from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.uri import uri


class Expression:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("description", StringType(), True),
                StructField("name", id.get_schema(), True),
                StructField("language", StringType(), True),
                StructField("expression", StringType(), True),
                StructField("reference", uri.get_schema(), True),]
        )

        return schema
