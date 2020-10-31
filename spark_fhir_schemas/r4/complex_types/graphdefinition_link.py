from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.graphdefinition_target import GraphDefinition_Target


# noinspection PyPep8Naming
class GraphDefinition_Link:
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
                StructField("path", StringType(), True),
                StructField("sliceName", StringType(), True),
                StructField("min", integer.get_schema(), True),
                StructField("max", StringType(), True),
                StructField("description", StringType(), True),
                StructField(
                    "target", ArrayType(GraphDefinition_Target.get_schema()),
                    True
                ),
            ]
        )

        return schema
