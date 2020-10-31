from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.time import time


# noinspection PyPep8Naming
class PractitionerRole_AvailableTime:
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
                StructField("daysOfWeek", ArrayType(code.get_schema()), True),
                StructField("allDay", BooleanType(), True),
                StructField("availableStartTime", time.get_schema(), True),
                StructField("availableEndTime", time.get_schema(), True),
            ]
        )

        return schema
