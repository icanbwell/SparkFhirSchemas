from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.time import time
from spark_fhir_schemas.r4.complex_types.time import time


class HealthcareService_AvailableTime:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("daysOfWeek",ArrayType(None.get_schema()), True),
                StructField("allDay", BooleanType(), True),
                StructField("availableStartTime", time.get_schema(), True),
                StructField("availableEndTime", time.get_schema(), True),
            ]
        )

        return schema
