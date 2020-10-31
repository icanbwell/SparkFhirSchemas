from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.examplescenario_step import ExampleScenario_Step


# noinspection PyPep8Naming
class ExampleScenario_Process:
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
                StructField("title", StringType(), True),
                StructField("description", markdown.get_schema(), True),
                StructField("preConditions", markdown.get_schema(), True),
                StructField("postConditions", markdown.get_schema(), True),
                StructField(
                    "step", ArrayType(ExampleScenario_Step.get_schema()), True
                ),
            ]
        )

        return schema
