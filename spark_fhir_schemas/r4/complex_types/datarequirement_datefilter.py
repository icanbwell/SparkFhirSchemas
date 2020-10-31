from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.duration import Duration


# noinspection PyPep8Naming
class DataRequirement_DateFilter:
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
                StructField("path", StringType(), True),
                StructField("searchParam", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField("valuePeriod", Period.get_schema(), True),
                StructField("valueDuration", Duration.get_schema(), True),
            ]
        )

        return schema
