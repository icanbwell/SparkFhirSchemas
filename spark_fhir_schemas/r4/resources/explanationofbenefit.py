from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ExplanationOfBenefit:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_related import ExplanationOfBenefit_Related
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_payee import ExplanationOfBenefit_Payee
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_careteam import ExplanationOfBenefit_CareTeam
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_supportinginfo import ExplanationOfBenefit_SupportingInfo
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_diagnosis import ExplanationOfBenefit_Diagnosis
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_procedure import ExplanationOfBenefit_Procedure
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_insurance import ExplanationOfBenefit_Insurance
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_accident import ExplanationOfBenefit_Accident
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_item import ExplanationOfBenefit_Item
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_additem import ExplanationOfBenefit_AddItem
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_adjudication import ExplanationOfBenefit_Adjudication
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_total import ExplanationOfBenefit_Total
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_payment import ExplanationOfBenefit_Payment
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_processnote import ExplanationOfBenefit_ProcessNote
        from spark_fhir_schemas.r4.complex_types.explanationofbenefit_benefitbalance import ExplanationOfBenefit_BenefitBalance
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "subType", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("use", code.get_schema(recursion_depth + 1), True),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "billablePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "insurer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "provider", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "priority",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fundsReserveRequested",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fundsReserve",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "related",
                    ArrayType(
                        ExplanationOfBenefit_Related.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "prescription", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "originalPrescription",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "payee",
                    ExplanationOfBenefit_Payee.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "referral", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "facility", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "claim", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "claimResponse", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "outcome", code.get_schema(recursion_depth + 1), True
                ),
                StructField("disposition", StringType(), True),
                StructField("preAuthRef", ArrayType(StringType()), True),
                StructField(
                    "preAuthRefPeriod",
                    ArrayType(Period.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "careTeam",
                    ArrayType(
                        ExplanationOfBenefit_CareTeam.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "supportingInfo",
                    ArrayType(
                        ExplanationOfBenefit_SupportingInfo.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "diagnosis",
                    ArrayType(
                        ExplanationOfBenefit_Diagnosis.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "procedure",
                    ArrayType(
                        ExplanationOfBenefit_Procedure.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "precedence", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "insurance",
                    ArrayType(
                        ExplanationOfBenefit_Insurance.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "accident",
                    ExplanationOfBenefit_Accident.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "item",
                    ArrayType(
                        ExplanationOfBenefit_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "addItem",
                    ArrayType(
                        ExplanationOfBenefit_AddItem.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "adjudication",
                    ArrayType(
                        ExplanationOfBenefit_Adjudication.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "total",
                    ArrayType(
                        ExplanationOfBenefit_Total.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "payment",
                    ExplanationOfBenefit_Payment.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "formCode",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "form", Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "processNote",
                    ArrayType(
                        ExplanationOfBenefit_ProcessNote.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "benefitPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "benefitBalance",
                    ArrayType(
                        ExplanationOfBenefit_BenefitBalance.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
