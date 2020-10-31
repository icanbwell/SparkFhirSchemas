from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Task_Restriction:
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
                StructField("repetitions", positiveInt.get_schema(), True),
                StructField("period", Period.get_schema(), True),
                StructField(
                    "recipient", ArrayType(Reference.get_schema()), True
                ),
            ]
        )

        return schema
