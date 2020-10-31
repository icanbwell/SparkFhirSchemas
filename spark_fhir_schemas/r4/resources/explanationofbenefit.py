from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.explanationofbenefit_related import ExplanationOfBenefit_Related
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.explanationofbenefit_payee import ExplanationOfBenefit_Payee
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.explanationofbenefit_careteam import ExplanationOfBenefit_CareTeam
from spark_fhir_schemas.r4.resources.explanationofbenefit_supportinginfo import ExplanationOfBenefit_SupportingInfo
from spark_fhir_schemas.r4.resources.explanationofbenefit_diagnosis import ExplanationOfBenefit_Diagnosis
from spark_fhir_schemas.r4.resources.explanationofbenefit_procedure import ExplanationOfBenefit_Procedure
from spark_fhir_schemas.r4.resources.positiveint import positiveInt
from spark_fhir_schemas.r4.resources.explanationofbenefit_insurance import ExplanationOfBenefit_Insurance
from spark_fhir_schemas.r4.resources.explanationofbenefit_accident import ExplanationOfBenefit_Accident
from spark_fhir_schemas.r4.resources.explanationofbenefit_item import ExplanationOfBenefit_Item
from spark_fhir_schemas.r4.resources.explanationofbenefit_additem import ExplanationOfBenefit_AddItem
from spark_fhir_schemas.r4.resources.explanationofbenefit_adjudication import ExplanationOfBenefit_Adjudication
from spark_fhir_schemas.r4.resources.explanationofbenefit_total import ExplanationOfBenefit_Total
from spark_fhir_schemas.r4.resources.explanationofbenefit_payment import ExplanationOfBenefit_Payment
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.attachment import Attachment
from spark_fhir_schemas.r4.resources.explanationofbenefit_processnote import ExplanationOfBenefit_ProcessNote
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.explanationofbenefit_benefitbalance import ExplanationOfBenefit_BenefitBalance


class ExplanationOfBenefit:
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
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("status", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subType", CodeableConcept.get_schema(), True),
                StructField("use", code.get_schema(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("billablePeriod", Period.get_schema(), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("enterer", Reference.get_schema(), True),
                StructField("insurer", Reference.get_schema(), True),
                StructField("provider", Reference.get_schema(), True),
                StructField("priority", CodeableConcept.get_schema(), True),
                StructField("fundsReserveRequested", CodeableConcept.get_schema(), True),
                StructField("fundsReserve", CodeableConcept.get_schema(), True),
                StructField("related",ArrayType(ExplanationOfBenefit_Related.get_schema()), True),
                StructField("prescription", Reference.get_schema(), True),
                StructField("originalPrescription", Reference.get_schema(), True),
                StructField("payee", ExplanationOfBenefit_Payee.get_schema(), True),
                StructField("referral", Reference.get_schema(), True),
                StructField("facility", Reference.get_schema(), True),
                StructField("claim", Reference.get_schema(), True),
                StructField("claimResponse", Reference.get_schema(), True),
                StructField("outcome", code.get_schema(), True),
                StructField("disposition", StringType(), True),
                StructField("preAuthRef",ArrayType(string.get_schema()), True),
                StructField("preAuthRefPeriod",ArrayType(Period.get_schema()), True),
                StructField("careTeam",ArrayType(ExplanationOfBenefit_CareTeam.get_schema()), True),
                StructField("supportingInfo",ArrayType(ExplanationOfBenefit_SupportingInfo.get_schema()), True),
                StructField("diagnosis",ArrayType(ExplanationOfBenefit_Diagnosis.get_schema()), True),
                StructField("procedure",ArrayType(ExplanationOfBenefit_Procedure.get_schema()), True),
                StructField("precedence", positiveInt.get_schema(), True),
                StructField("insurance",ArrayType(ExplanationOfBenefit_Insurance.get_schema()), True),
                StructField("accident", ExplanationOfBenefit_Accident.get_schema(), True),
                StructField("item",ArrayType(ExplanationOfBenefit_Item.get_schema()), True),
                StructField("addItem",ArrayType(ExplanationOfBenefit_AddItem.get_schema()), True),
                StructField("adjudication",ArrayType(ExplanationOfBenefit_Adjudication.get_schema()), True),
                StructField("total",ArrayType(ExplanationOfBenefit_Total.get_schema()), True),
                StructField("payment", ExplanationOfBenefit_Payment.get_schema(), True),
                StructField("formCode", CodeableConcept.get_schema(), True),
                StructField("form", Attachment.get_schema(), True),
                StructField("processNote",ArrayType(ExplanationOfBenefit_ProcessNote.get_schema()), True),
                StructField("benefitPeriod", Period.get_schema(), True),
                StructField("benefitBalance",ArrayType(ExplanationOfBenefit_BenefitBalance.get_schema()), True),]
        )

        return schema
