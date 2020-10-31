from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code


# noinspection PyPep8Naming
class Count:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("value", decimal.get_schema(), True),
                StructField("comparator", StringType(), True),
                StructField("unit", StringType(), True),
                StructField("system", uri.get_schema(), True),
                StructField("code", code.get_schema(), True),
            ]
        )

        return schema
