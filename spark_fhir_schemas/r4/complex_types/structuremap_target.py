from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.structuremap_parameter import StructureMap_Parameter


# noinspection PyPep8Naming
class StructureMap_Target:
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
                StructField("context", id.get_schema(), True),
                StructField("contextType", StringType(), True),
                StructField("element", StringType(), True),
                StructField("variable", id.get_schema(), True),
                StructField("listRuleId", id.get_schema(), True),
                StructField("transform", StringType(), True),
                StructField(
                    "parameter",
                    ArrayType(StructureMap_Parameter.get_schema()), True
                ),
            ]
        )

        return schema
