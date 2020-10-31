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
        """
        This resource provides: the claim details; adjudication details from the
        processing of a Claim; and optionally account balance information, for
        informing the subscriber of the benefits provided.


        resourceType: This is a ExplanationOfBenefit resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: A unique identifier assigned to this explanation of benefit.

        status: The status of the resource instance.

        type: The category of claim, e.g. oral, pharmacy, vision, institutional,
            professional.

        subType: A finer grained suite of claim type codes which may convey additional
            information such as Inpatient vs Outpatient and/or a specialty service.

        use: A code to indicate whether the nature of the request is: to request
            adjudication of products and services previously rendered; or requesting
            authorization and adjudication for provision in the future; or requesting the
            non-binding adjudication of the listed products and services which could be
            provided in the future.

        patient: The party to whom the professional services and/or products have been supplied
            or are being considered and for whom actual for forecast reimbursement is
            sought.

        billablePeriod: The period for which charges are being submitted.

        created: The date this resource was created.

        enterer: Individual who created the claim, predetermination or preauthorization.

        insurer: The party responsible for authorization, adjudication and reimbursement.

        provider: The provider which is responsible for the claim, predetermination or
            preauthorization.

        priority: The provider-required urgency of processing the request. Typical values
            include: stat, routine deferred.

        fundsReserveRequested: A code to indicate whether and for whom funds are to be reserved for future
            claims.

        fundsReserve: A code, used only on a response to a preauthorization, to indicate whether the
            benefits payable have been reserved and for whom.

        related: Other claims which are related to this claim such as prior submissions or
            claims for related services or for the same event.

        prescription: Prescription to support the dispensing of pharmacy, device or vision products.

        originalPrescription: Original prescription which has been superseded by this prescription to
            support the dispensing of pharmacy services, medications or products.

        payee: The party to be reimbursed for cost of the products and services according to
            the terms of the policy.

        referral: A reference to a referral resource.

        facility: Facility where the services were provided.

        claim: The business identifier for the instance of the adjudication request: claim
            predetermination or preauthorization.

        claimResponse: The business identifier for the instance of the adjudication response: claim,
            predetermination or preauthorization response.

        outcome: The outcome of the claim, predetermination, or preauthorization processing.

        disposition: A human readable description of the status of the adjudication.

        preAuthRef: Reference from the Insurer which is used in later communications which refers
            to this adjudication.

        preAuthRefPeriod: The timeframe during which the supplied preauthorization reference may be
            quoted on claims to obtain the adjudication as provided.

        careTeam: The members of the team who provided the products and services.

        supportingInfo: Additional information codes regarding exceptions, special considerations, the
            condition, situation, prior or concurrent issues.

        diagnosis: Information about diagnoses relevant to the claim items.

        procedure: Procedures performed on the patient relevant to the billing items with the
            claim.

        precedence: This indicates the relative order of a series of EOBs related to different
            coverages for the same suite of services.

        insurance: Financial instruments for reimbursement for the health care products and
            services specified on the claim.

        accident: Details of a accident which resulted in injuries which required the products
            and services listed in the claim.

        item: A claim line. Either a simple (a product or service) or a 'group' of details
            which can also be a simple items or groups of sub-details.

        addItem: The first-tier service adjudications for payor added product or service lines.

        adjudication: The adjudication results which are presented at the header level rather than
            at the line-item or add-item levels.

        total: Categorized monetary totals for the adjudication.

        payment: Payment details for the adjudication of the claim.

        formCode: A code for the form to be used for printing the content.

        form: The actual form, by reference or inclusion, for printing the content or an
            EOB.

        processNote: A note that describes or explains adjudication results in a human readable
            form.

        benefitPeriod: The term of the benefits documented in this response.

        benefitBalance: Balance by Benefit Category.

        """
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
                # This is a ExplanationOfBenefit resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # A unique identifier assigned to this explanation of benefit.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The status of the resource instance.
                StructField("status", StringType(), True),
                # The category of claim, e.g. oral, pharmacy, vision, institutional,
                # professional.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A finer grained suite of claim type codes which may convey additional
                # information such as Inpatient vs Outpatient and/or a specialty service.
                StructField(
                    "subType", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A code to indicate whether the nature of the request is: to request
                # adjudication of products and services previously rendered; or requesting
                # authorization and adjudication for provision in the future; or requesting the
                # non-binding adjudication of the listed products and services which could be
                # provided in the future.
                StructField("use", code.get_schema(recursion_depth + 1), True),
                # The party to whom the professional services and/or products have been supplied
                # or are being considered and for whom actual for forecast reimbursement is
                # sought.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # The period for which charges are being submitted.
                StructField(
                    "billablePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The date this resource was created.
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Individual who created the claim, predetermination or preauthorization.
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                # The party responsible for authorization, adjudication and reimbursement.
                StructField(
                    "insurer", Reference.get_schema(recursion_depth + 1), True
                ),
                # The provider which is responsible for the claim, predetermination or
                # preauthorization.
                StructField(
                    "provider", Reference.get_schema(recursion_depth + 1), True
                ),
                # The provider-required urgency of processing the request. Typical values
                # include: stat, routine deferred.
                StructField(
                    "priority",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A code to indicate whether and for whom funds are to be reserved for future
                # claims.
                StructField(
                    "fundsReserveRequested",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A code, used only on a response to a preauthorization, to indicate whether the
                # benefits payable have been reserved and for whom.
                StructField(
                    "fundsReserve",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Other claims which are related to this claim such as prior submissions or
                # claims for related services or for the same event.
                StructField(
                    "related",
                    ArrayType(
                        ExplanationOfBenefit_Related.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Prescription to support the dispensing of pharmacy, device or vision products.
                StructField(
                    "prescription", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Original prescription which has been superseded by this prescription to
                # support the dispensing of pharmacy services, medications or products.
                StructField(
                    "originalPrescription",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The party to be reimbursed for cost of the products and services according to
                # the terms of the policy.
                StructField(
                    "payee",
                    ExplanationOfBenefit_Payee.get_schema(recursion_depth + 1),
                    True
                ),
                # A reference to a referral resource.
                StructField(
                    "referral", Reference.get_schema(recursion_depth + 1), True
                ),
                # Facility where the services were provided.
                StructField(
                    "facility", Reference.get_schema(recursion_depth + 1), True
                ),
                # The business identifier for the instance of the adjudication request: claim
                # predetermination or preauthorization.
                StructField(
                    "claim", Reference.get_schema(recursion_depth + 1), True
                ),
                # The business identifier for the instance of the adjudication response: claim,
                # predetermination or preauthorization response.
                StructField(
                    "claimResponse", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The outcome of the claim, predetermination, or preauthorization processing.
                StructField(
                    "outcome", code.get_schema(recursion_depth + 1), True
                ),
                # A human readable description of the status of the adjudication.
                StructField("disposition", StringType(), True),
                # Reference from the Insurer which is used in later communications which refers
                # to this adjudication.
                StructField("preAuthRef", ArrayType(StringType()), True),
                # The timeframe during which the supplied preauthorization reference may be
                # quoted on claims to obtain the adjudication as provided.
                StructField(
                    "preAuthRefPeriod",
                    ArrayType(Period.get_schema(recursion_depth + 1)), True
                ),
                # The members of the team who provided the products and services.
                StructField(
                    "careTeam",
                    ArrayType(
                        ExplanationOfBenefit_CareTeam.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Additional information codes regarding exceptions, special considerations, the
                # condition, situation, prior or concurrent issues.
                StructField(
                    "supportingInfo",
                    ArrayType(
                        ExplanationOfBenefit_SupportingInfo.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Information about diagnoses relevant to the claim items.
                StructField(
                    "diagnosis",
                    ArrayType(
                        ExplanationOfBenefit_Diagnosis.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Procedures performed on the patient relevant to the billing items with the
                # claim.
                StructField(
                    "procedure",
                    ArrayType(
                        ExplanationOfBenefit_Procedure.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # This indicates the relative order of a series of EOBs related to different
                # coverages for the same suite of services.
                StructField(
                    "precedence", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                # Financial instruments for reimbursement for the health care products and
                # services specified on the claim.
                StructField(
                    "insurance",
                    ArrayType(
                        ExplanationOfBenefit_Insurance.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Details of a accident which resulted in injuries which required the products
                # and services listed in the claim.
                StructField(
                    "accident",
                    ExplanationOfBenefit_Accident.
                    get_schema(recursion_depth + 1), True
                ),
                # A claim line. Either a simple (a product or service) or a 'group' of details
                # which can also be a simple items or groups of sub-details.
                StructField(
                    "item",
                    ArrayType(
                        ExplanationOfBenefit_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The first-tier service adjudications for payor added product or service lines.
                StructField(
                    "addItem",
                    ArrayType(
                        ExplanationOfBenefit_AddItem.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The adjudication results which are presented at the header level rather than
                # at the line-item or add-item levels.
                StructField(
                    "adjudication",
                    ArrayType(
                        ExplanationOfBenefit_Adjudication.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Categorized monetary totals for the adjudication.
                StructField(
                    "total",
                    ArrayType(
                        ExplanationOfBenefit_Total.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Payment details for the adjudication of the claim.
                StructField(
                    "payment",
                    ExplanationOfBenefit_Payment.
                    get_schema(recursion_depth + 1), True
                ),
                # A code for the form to be used for printing the content.
                StructField(
                    "formCode",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The actual form, by reference or inclusion, for printing the content or an
                # EOB.
                StructField(
                    "form", Attachment.get_schema(recursion_depth + 1), True
                ),
                # A note that describes or explains adjudication results in a human readable
                # form.
                StructField(
                    "processNote",
                    ArrayType(
                        ExplanationOfBenefit_ProcessNote.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The term of the benefits documented in this response.
                StructField(
                    "benefitPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Balance by Benefit Category.
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
