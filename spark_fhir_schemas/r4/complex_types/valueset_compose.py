from pyspark.sql.types import ArrayType, BooleanType, DateType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.valueset_include import ValueSet_Include


# noinspection PyPep8Naming
class ValueSet_Compose:
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
                StructField("lockedDate", DateType(), True),
                StructField("inactive", BooleanType(), True),
                StructField(
                    "include", ArrayType(ValueSet_Include.get_schema()), True
                ),
                StructField(
                    "exclude", ArrayType(ValueSet_Include.get_schema()), True
                ),
            ]
        )

        return schema
