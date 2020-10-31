from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.canonical import canonical


# noinspection PyPep8Naming
class TestScript_Capability:
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
                StructField("required", BooleanType(), True),
                StructField("validated", BooleanType(), True),
                StructField("description", StringType(), True),
                StructField("origin", ArrayType(integer.get_schema()), True),
                StructField("destination", integer.get_schema(), True),
                StructField("link", ArrayType(uri.get_schema()), True),
                StructField("capabilities", canonical.get_schema(), True),
            ]
        )

        return schema
