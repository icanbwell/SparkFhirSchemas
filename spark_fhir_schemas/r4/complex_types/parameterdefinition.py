from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.canonical import canonical


# noinspection PyPep8Naming
class ParameterDefinition:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("name", code.get_schema(), True),
                StructField("use", code.get_schema(), True),
                StructField("min", integer.get_schema(), True),
                StructField("max", StringType(), True),
                StructField("documentation", StringType(), True),
                StructField("type", code.get_schema(), True),
                StructField("profile", canonical.get_schema(), True),
            ]
        )

        return schema
