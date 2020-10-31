from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Timing_Repeat:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.time import time
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    "boundsDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "boundsRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "boundsPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "count", positiveInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "countMax", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "duration", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "durationMax", decimal.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("durationUnit", StringType(), True),
                StructField(
                    "frequency", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "frequencyMax",
                    positiveInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "period", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "periodMax", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField("periodUnit", StringType(), True),
                StructField(
                    "dayOfWeek",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "timeOfDay",
                    ArrayType(time.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "offset", unsignedInt.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
