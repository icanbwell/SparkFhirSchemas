from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class HumanName:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.period import Period
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("use", StringType(), True),
                StructField("text", StringType(), True),
                StructField("family", StringType(), True),
                StructField("given", ArrayType(StringType()), True),
                StructField("prefix", ArrayType(StringType()), True),
                StructField("suffix", ArrayType(StringType()), True),
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
