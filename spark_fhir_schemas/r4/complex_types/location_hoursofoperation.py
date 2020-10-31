from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Location_HoursOfOperation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.time import time
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
                StructField(
                    "daysOfWeek",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
                StructField("allDay", BooleanType(), True),
                StructField(
                    "openingTime", time.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "closingTime", time.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
