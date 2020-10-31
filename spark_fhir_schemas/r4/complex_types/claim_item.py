from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.address import Address
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.money import Money
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.claim_detail import Claim_Detail


# noinspection PyPep8Naming
class Claim_Item:
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
                StructField("sequence", positiveInt.get_schema(), True),
                StructField(
                    "careTeamSequence", ArrayType(positiveInt.get_schema()),
                    True
                ),
                StructField(
                    "diagnosisSequence", ArrayType(positiveInt.get_schema()),
                    True
                ),
                StructField(
                    "procedureSequence", ArrayType(positiveInt.get_schema()),
                    True
                ),
                StructField(
                    "informationSequence", ArrayType(positiveInt.get_schema()),
                    True
                ),
                StructField("revenue", CodeableConcept.get_schema(), True),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField(
                    "productOrService", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "modifier", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "programCode", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("servicedDate", StringType(), True),
                StructField("servicedPeriod", Period.get_schema(), True),
                StructField(
                    "locationCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField("locationAddress", Address.get_schema(), True),
                StructField("locationReference", Reference.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("unitPrice", Money.get_schema(), True),
                StructField("factor", decimal.get_schema(), True),
                StructField("net", Money.get_schema(), True),
                StructField("udi", ArrayType(Reference.get_schema()), True),
                StructField("bodySite", CodeableConcept.get_schema(), True),
                StructField(
                    "subSite", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "encounter", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "detail", ArrayType(Claim_Detail.get_schema()), True
                ),
            ]
        )

        return schema
