from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.timing_repeat import Timing_Repeat
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class Timing:
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
                StructField("event", ArrayType(dateTime.get_schema()), True),
                StructField("repeat", Timing_Repeat.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),
            ]
        )

        return schema
