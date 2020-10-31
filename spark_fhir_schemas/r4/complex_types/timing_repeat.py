from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.duration import Duration
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.time import time
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt


# noinspection PyPep8Naming
class Timing_Repeat:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("boundsDuration", Duration.get_schema(), True),
                StructField("boundsRange", Range.get_schema(), True),
                StructField("boundsPeriod", Period.get_schema(), True),
                StructField("count", positiveInt.get_schema(), True),
                StructField("countMax", positiveInt.get_schema(), True),
                StructField("duration", decimal.get_schema(), True),
                StructField("durationMax", decimal.get_schema(), True),
                StructField("durationUnit", StringType(), True),
                StructField("frequency", positiveInt.get_schema(), True),
                StructField("frequencyMax", positiveInt.get_schema(), True),
                StructField("period", decimal.get_schema(), True),
                StructField("periodMax", decimal.get_schema(), True),
                StructField("periodUnit", StringType(), True),
                StructField("dayOfWeek", ArrayType(code.get_schema()), True),
                StructField("timeOfDay", ArrayType(time.get_schema()), True),
                StructField("offset", unsignedInt.get_schema(), True),
            ]
        )

        return schema
