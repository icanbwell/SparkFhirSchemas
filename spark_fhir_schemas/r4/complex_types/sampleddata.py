from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SampledData:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
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
                    "origin", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "period", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "lowerLimit", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "upperLimit", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dimensions", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("data", StringType(), True),
            ]
        )

        return schema
