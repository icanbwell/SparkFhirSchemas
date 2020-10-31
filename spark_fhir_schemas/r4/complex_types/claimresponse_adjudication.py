from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.decimal import decimal


# noinspection PyPep8Naming
class ClaimResponse_Adjudication:
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
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("reason", CodeableConcept.get_schema(), True),
                StructField("amount", Money.get_schema(), True),
                StructField("value", decimal.get_schema(), True),
            ]
        )

        return schema
