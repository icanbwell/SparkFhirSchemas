from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.examplescenario_process import ExampleScenario_Process
from spark_fhir_schemas.r4.complex_types.examplescenario_operation import ExampleScenario_Operation
from spark_fhir_schemas.r4.complex_types.examplescenario_alternative import ExampleScenario_Alternative


# noinspection PyPep8Naming
class ExampleScenario_Step:
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
                    "process", ArrayType(ExampleScenario_Process.get_schema()),
                    True
                ),
                StructField("pause", BooleanType(), True),
                StructField(
                    "operation", ExampleScenario_Operation.get_schema(), True
                ),
                StructField(
                    "alternative",
                    ArrayType(ExampleScenario_Alternative.get_schema()), True
                ),
            ]
        )

        return schema
