from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code


# noinspection PyPep8Naming
class Coding:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("system", uri.get_schema(), True),
                StructField("version", StringType(), True),
                StructField("code", code.get_schema(), True),
                StructField("display", StringType(), True),
                StructField("userSelected", BooleanType(), True),
            ]
        )

        return schema
