from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class DataRequirement_DateFilter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("path", StringType(), True),
                StructField("searchParam", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
