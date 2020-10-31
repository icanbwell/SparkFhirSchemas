from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.testscript_operation import TestScript_Operation
from spark_fhir_schemas.r4.complex_types.testscript_assert import TestScript_Assert


# noinspection PyPep8Naming
class TestScript_Action1:
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
                StructField(
                    "operation", TestScript_Operation.get_schema(), True
                ),
                StructField("assert", TestScript_Assert.get_schema(), True),
            ]
        )

        return schema
