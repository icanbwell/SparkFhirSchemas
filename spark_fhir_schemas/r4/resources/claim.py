from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.claim_related import Claim_Related
from spark_fhir_schemas.r4.complex_types.claim_payee import Claim_Payee
from spark_fhir_schemas.r4.complex_types.claim_careteam import Claim_CareTeam
from spark_fhir_schemas.r4.complex_types.claim_supportinginfo import Claim_SupportingInfo
from spark_fhir_schemas.r4.complex_types.claim_diagnosis import Claim_Diagnosis
from spark_fhir_schemas.r4.complex_types.claim_procedure import Claim_Procedure
from spark_fhir_schemas.r4.complex_types.claim_insurance import Claim_Insurance
from spark_fhir_schemas.r4.complex_types.claim_accident import Claim_Accident
from spark_fhir_schemas.r4.complex_types.claim_item import Claim_Item
from spark_fhir_schemas.r4.complex_types.money import Money


# noinspection PyPep8Naming
class Claim:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("status", code.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subType", CodeableConcept.get_schema(), True),
                StructField("use", StringType(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("billablePeriod", Period.get_schema(), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("enterer", Reference.get_schema(), True),
                StructField("insurer", Reference.get_schema(), True),
                StructField("provider", Reference.get_schema(), True),
                StructField("priority", CodeableConcept.get_schema(), True),
                StructField(
                    "fundsReserve", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "related", ArrayType(Claim_Related.get_schema()), True
                ),
                StructField("prescription", Reference.get_schema(), True),
                StructField(
                    "originalPrescription", Reference.get_schema(), True
                ),
                StructField("payee", Claim_Payee.get_schema(), True),
                StructField("referral", Reference.get_schema(), True),
                StructField("facility", Reference.get_schema(), True),
                StructField(
                    "careTeam", ArrayType(Claim_CareTeam.get_schema()), True
                ),
                StructField(
                    "supportingInfo",
                    ArrayType(Claim_SupportingInfo.get_schema()), True
                ),
                StructField(
                    "diagnosis", ArrayType(Claim_Diagnosis.get_schema()), True
                ),
                StructField(
                    "procedure", ArrayType(Claim_Procedure.get_schema()), True
                ),
                StructField(
                    "insurance", ArrayType(Claim_Insurance.get_schema()), True
                ),
                StructField("accident", Claim_Accident.get_schema(), True),
                StructField("item", ArrayType(Claim_Item.get_schema()), True),
                StructField("total", Money.get_schema(), True),
            ]
        )

        return schema
