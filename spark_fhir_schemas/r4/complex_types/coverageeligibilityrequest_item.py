from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_diagnosis import CoverageEligibilityRequest_Diagnosis


# noinspection PyPep8Naming
class CoverageEligibilityRequest_Item:
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
                    "supportingInfoSequence",
                    ArrayType(positiveInt.get_schema()), True
                ),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField(
                    "productOrService", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "modifier", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("provider", Reference.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("unitPrice", Money.get_schema(), True),
                StructField("facility", Reference.get_schema(), True),
                StructField(
                    "diagnosis",
                    ArrayType(
                        CoverageEligibilityRequest_Diagnosis.get_schema()
                    ), True
                ),
                StructField("detail", ArrayType(Reference.get_schema()), True),
            ]
        )

        return schema
