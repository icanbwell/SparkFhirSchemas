from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.id import id


# noinspection PyPep8Naming
class TestScript_Variable:
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
                StructField("defaultValue", StringType(), True),
                StructField("description", StringType(), True),
                StructField("expression", StringType(), True),
                StructField("headerField", StringType(), True),
                StructField("hint", StringType(), True),
                StructField("path", StringType(), True),
                StructField("sourceId", id.get_schema(), True),
            ]
        )

        return schema
