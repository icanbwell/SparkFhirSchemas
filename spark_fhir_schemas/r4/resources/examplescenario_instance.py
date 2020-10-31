from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.examplescenario_version import ExampleScenario_Version
from spark_fhir_schemas.r4.resources.examplescenario_containedinstance import ExampleScenario_ContainedInstance


class ExampleScenario_Instance:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("resourceId", StringType(), True),
                StructField("resourceType", code.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("description", markdown.get_schema(), True),
                StructField("version",ArrayType(ExampleScenario_Version.get_schema()), True),
                StructField("containedInstance",ArrayType(ExampleScenario_ContainedInstance.get_schema()), True),]
        )

        return schema
