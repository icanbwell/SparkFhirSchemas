from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ContactPoint:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
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
                StructField("system", StringType(), True),
                StructField("value", StringType(), True),
                StructField("use", StringType(), True),
                StructField(
                    "rank", positiveInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
