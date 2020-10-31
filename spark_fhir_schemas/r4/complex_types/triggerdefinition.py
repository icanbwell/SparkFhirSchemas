from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TriggerDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
        from spark_fhir_schemas.r4.complex_types.expression import Expression
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("type", StringType(), True),
                StructField("name", StringType(), True),
                StructField(
                    "timingTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "timingReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("timingDate", StringType(), True),
                StructField("timingDateTime", StringType(), True),
                StructField(
                    "data",
                    ArrayType(DataRequirement.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "condition", Expression.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
