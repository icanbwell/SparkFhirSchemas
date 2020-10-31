from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.url import url
from spark_fhir_schemas.r4.complex_types.code import code


# noinspection PyPep8Naming
class Subscription_Channel:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("type", StringType(), True),
                StructField("endpoint", url.get_schema(), True),
                StructField("payload", code.get_schema(), True),
                StructField("header", ArrayType(StringType()), True),
            ]
        )

        return schema
