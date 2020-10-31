from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt


# noinspection PyPep8Naming
class SampledData:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("origin", Quantity.get_schema(), True),
                StructField("period", decimal.get_schema(), True),
                StructField("factor", decimal.get_schema(), True),
                StructField("lowerLimit", decimal.get_schema(), True),
                StructField("upperLimit", decimal.get_schema(), True),
                StructField("dimensions", positiveInt.get_schema(), True),
                StructField("data", StringType(), True),
            ]
        )

        return schema
