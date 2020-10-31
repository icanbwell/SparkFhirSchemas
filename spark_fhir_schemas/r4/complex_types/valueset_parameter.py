from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension


# noinspection PyPep8Naming
class ValueSet_Parameter:
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
                StructField("valueString", StringType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueDecimal", IntegerType(), True),
                StructField("valueUri", StringType(), True),
                StructField("valueCode", StringType(), True),
                StructField("valueDateTime", StringType(), True),
            ]
        )

        return schema
