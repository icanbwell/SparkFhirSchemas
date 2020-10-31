from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.explanationofbenefit_adjudication import ExplanationOfBenefit_Adjudication


# noinspection PyPep8Naming
class ExplanationOfBenefit_SubDetail1:
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
                    "productOrService", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "modifier", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("unitPrice", Money.get_schema(), True),
                StructField("factor", decimal.get_schema(), True),
                StructField("net", Money.get_schema(), True),
                StructField(
                    "noteNumber", ArrayType(positiveInt.get_schema()), True
                ),
                StructField(
                    "adjudication",
                    ArrayType(ExplanationOfBenefit_Adjudication.get_schema()),
                    True
                ),
            ]
        )

        return schema
