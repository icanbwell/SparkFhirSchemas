from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.period import Period


class Address:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("use", StringType(), True),
                StructField("type", StringType(), True),
                StructField("text", StringType(), True),
                StructField("line",ArrayType(string.get_schema()), True),
                StructField("city", StringType(), True),
                StructField("district", StringType(), True),
                StructField("state", StringType(), True),
                StructField("postalCode", StringType(), True),
                StructField("country", StringType(), True),
                StructField("period", Period.get_schema(), True),]
        )

        return schema
