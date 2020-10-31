from pyspark.sql.types import ArrayType, IntegerType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class Immunization_ProtocolApplied:
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
                StructField("series", StringType(), True),
                StructField("authority", Reference.get_schema(), True),
                StructField(
                    "targetDisease", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("doseNumberPositiveInt", IntegerType(), True),
                StructField("doseNumberString", StringType(), True),
                StructField("seriesDosesPositiveInt", IntegerType(), True),
                StructField("seriesDosesString", StringType(), True),
            ]
        )

        return schema
