from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.period import Period


# noinspection PyPep8Naming
class Address:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("use", StringType(), True),
                StructField("type", StringType(), True),
                StructField("text", StringType(), True),
                StructField("line", ArrayType(StringType()), True),
                StructField("city", StringType(), True),
                StructField("district", StringType(), True),
                StructField("state", StringType(), True),
                StructField("postalCode", StringType(), True),
                StructField("country", StringType(), True),
                StructField("period", Period.get_schema(), True),
            ]
        )

        return schema
