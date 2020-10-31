from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.period import Period


class HumanName:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("use", StringType(), True),
                StructField("text", StringType(), True),
                StructField("family", StringType(), True),
                StructField("given",ArrayType(string.get_schema()), True),
                StructField("prefix",ArrayType(string.get_schema()), True),
                StructField("suffix",ArrayType(string.get_schema()), True),
                StructField("period", Period.get_schema(), True),
            ]
        )

        return schema
