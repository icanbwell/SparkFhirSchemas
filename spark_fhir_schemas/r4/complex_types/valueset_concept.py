from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.valueset_designation import ValueSet_Designation


# noinspection PyPep8Naming
class ValueSet_Concept:
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
                StructField("code", code.get_schema(), True),
                StructField("display", StringType(), True),
                StructField(
                    "designation",
                    ArrayType(ValueSet_Designation.get_schema()), True
                ),
            ]
        )

        return schema
