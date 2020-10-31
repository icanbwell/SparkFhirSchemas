from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class ClaimResponse_Insurance:
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
                StructField("sequence", positiveInt.get_schema(), True),
                StructField("focal", BooleanType(), True),
                StructField("coverage", Reference.get_schema(), True),
                StructField("businessArrangement", StringType(), True),
                StructField("claimResponse", Reference.get_schema(), True),
            ]
        )

        return schema
