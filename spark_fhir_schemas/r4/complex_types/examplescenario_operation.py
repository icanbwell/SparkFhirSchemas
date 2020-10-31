from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.examplescenario_containedinstance import ExampleScenario_ContainedInstance


# noinspection PyPep8Naming
class ExampleScenario_Operation:
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
                StructField("number", StringType(), True),
                StructField("type", StringType(), True),
                StructField("name", StringType(), True),
                StructField("initiator", StringType(), True),
                StructField("receiver", StringType(), True),
                StructField("description", markdown.get_schema(), True),
                StructField("initiatorActive", BooleanType(), True),
                StructField("receiverActive", BooleanType(), True),
                StructField(
                    "request", ExampleScenario_ContainedInstance.get_schema(),
                    True
                ),
                StructField(
                    "response", ExampleScenario_ContainedInstance.get_schema(),
                    True
                ),
            ]
        )

        return schema
