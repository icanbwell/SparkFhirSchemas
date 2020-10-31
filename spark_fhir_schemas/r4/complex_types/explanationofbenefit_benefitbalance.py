from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.explanationofbenefit_financial import ExplanationOfBenefit_Financial


# noinspection PyPep8Naming
class ExplanationOfBenefit_BenefitBalance:
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
                StructField("excluded", BooleanType(), True),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField("network", CodeableConcept.get_schema(), True),
                StructField("unit", CodeableConcept.get_schema(), True),
                StructField("term", CodeableConcept.get_schema(), True),
                StructField(
                    "financial",
                    ArrayType(ExplanationOfBenefit_Financial.get_schema()),
                    True
                ),
            ]
        )

        return schema
