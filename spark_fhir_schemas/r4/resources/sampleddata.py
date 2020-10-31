from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.string import string


class SampledData:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("origin", Quantity.get_schema(), True),
                StructField("period", decimal.get_schema(), True),
                StructField("factor", decimal.get_schema(), True),
                StructField("lowerLimit", decimal.get_schema(), True),
                StructField("upperLimit", decimal.get_schema(), True),
                StructField("dimensions", positiveInt.get_schema(), True),
                StructField("data", StringType(), True),]
        )

        return schema
