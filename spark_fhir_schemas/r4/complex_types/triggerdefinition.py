from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
from spark_fhir_schemas.r4.complex_types.expression import Expression


# noinspection PyPep8Naming
class TriggerDefinition:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("type", StringType(), True),
                StructField("name", StringType(), True),
                StructField("timingTiming", Timing.get_schema(), True),
                StructField("timingReference", Reference.get_schema(), True),
                StructField("timingDate", StringType(), True),
                StructField("timingDateTime", StringType(), True),
                StructField(
                    "data", ArrayType(DataRequirement.get_schema()), True
                ),
                StructField("condition", Expression.get_schema(), True),
            ]
        )

        return schema
