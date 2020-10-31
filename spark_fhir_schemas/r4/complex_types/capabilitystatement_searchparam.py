from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.markdown import markdown


# noinspection PyPep8Naming
class CapabilityStatement_SearchParam:
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
                StructField("definition", canonical.get_schema(), True),
                StructField("type", StringType(), True),
                StructField("documentation", markdown.get_schema(), True),
            ]
        )

        return schema
