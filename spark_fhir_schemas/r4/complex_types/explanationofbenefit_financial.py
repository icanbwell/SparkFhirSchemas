from pyspark.sql.types import ArrayType, IntegerType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.money import Money


# noinspection PyPep8Naming
class ExplanationOfBenefit_Financial:
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
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("allowedUnsignedInt", IntegerType(), True),
                StructField("allowedString", StringType(), True),
                StructField("allowedMoney", Money.get_schema(), True),
                StructField("usedUnsignedInt", IntegerType(), True),
                StructField("usedMoney", Money.get_schema(), True),
            ]
        )

        return schema
