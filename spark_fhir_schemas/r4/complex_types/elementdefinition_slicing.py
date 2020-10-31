from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.elementdefinition_discriminator import ElementDefinition_Discriminator


# noinspection PyPep8Naming
class ElementDefinition_Slicing:
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
                    "discriminator",
                    ArrayType(ElementDefinition_Discriminator.get_schema()),
                    True
                ),
                StructField("description", StringType(), True),
                StructField("ordered", BooleanType(), True),
                StructField("rules", StringType(), True),
            ]
        )

        return schema
