from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.time import time
from spark_fhir_schemas.r4.resources.unsignedint import unsignedInt


class Timing_Repeat:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
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
                StructField("dayOfWeek",ArrayType(code.get_schema()), True),
                StructField("timeOfDay",ArrayType(time.get_schema()), True),
                StructField("when",ArrayType(None.get_schema()), True),
                StructField("offset", unsignedInt.get_schema(), True),]
        )

        return schema
