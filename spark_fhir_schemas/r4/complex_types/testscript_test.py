from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.testscript_action1 import TestScript_Action1


# noinspection PyPep8Naming
class TestScript_Test:
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
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField(
                    "action", ArrayType(TestScript_Action1.get_schema()), True
                ),
            ]
        )

        return schema
