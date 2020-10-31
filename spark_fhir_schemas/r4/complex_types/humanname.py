from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.period import Period


# noinspection PyPep8Naming
class HumanName:
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
                StructField("text", StringType(), True),
                StructField("family", StringType(), True),
                StructField("given", ArrayType(StringType()), True),
                StructField("prefix", ArrayType(StringType()), True),
                StructField("suffix", ArrayType(StringType()), True),
                StructField("period", Period.get_schema(), True),
            ]
        )

        return schema
