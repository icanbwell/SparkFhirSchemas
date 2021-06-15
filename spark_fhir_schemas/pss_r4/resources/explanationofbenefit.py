from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchExplanationOfBenefit(AutoMapperDataTypeComplexBase):
    """
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        resourceType: Optional[Any] = None,
        id_: Optional[Any] = None,
        meta: Optional[Any] = None,
        implicitRules: Optional[Any] = None,
        language: Optional[Any] = None,
        text: Optional[Any] = None,
        contained: Optional[Any] = None,
        extension: Optional[Any] = None,
        identifier: Optional[Any] = None,
        status: Optional[Any] = None,
        type_: Optional[Any] = None,
        subType: Optional[Any] = None,
        use: Optional[Any] = None,
        patient: Optional[Any] = None,
        billablePeriod: Optional[Any] = None,
        created: Optional[Any] = None,
        enterer: Optional[Any] = None,
        insurer: Optional[Any] = None,
        provider: Optional[Any] = None,
        priority: Optional[Any] = None,
        fundsReserveRequested: Optional[Any] = None,
        fundsReserve: Optional[Any] = None,
        related: Optional[Any] = None,
        prescription: Optional[Any] = None,
        originalPrescription: Optional[Any] = None,
        payee: Optional[Any] = None,
        referral: Optional[Any] = None,
        facility: Optional[Any] = None,
        claim: Optional[Any] = None,
        claimResponse: Optional[Any] = None,
        outcome: Optional[Any] = None,
        disposition: Optional[Any] = None,
        preAuthRef: Optional[Any] = None,
        preAuthRefPeriod: Optional[Any] = None,
        careTeam: Optional[Any] = None,
        supportingInfo: Optional[Any] = None,
        diagnosis: Optional[Any] = None,
        procedure: Optional[Any] = None,
        precedence: Optional[Any] = None,
        insurance: Optional[Any] = None,
        accident: Optional[Any] = None,
        item: Optional[Any] = None,
        addItem: Optional[Any] = None,
        adjudication: Optional[Any] = None,
        total: Optional[Any] = None,
        payment: Optional[Any] = None,
        formCode: Optional[Any] = None,
        form: Optional[Any] = None,
        processNote: Optional[Any] = None,
        benefitPeriod: Optional[Any] = None,
        benefitBalance: Optional[Any] = None,
    ) -> None:
        super().__init__(
            resourceType=resourceType,
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            identifier=identifier,
            status=status,
            type_=type_,
            subType=subType,
            use=use,
            patient=patient,
            billablePeriod=billablePeriod,
            created=created,
            enterer=enterer,
            insurer=insurer,
            provider=provider,
            priority=priority,
            fundsReserveRequested=fundsReserveRequested,
            fundsReserve=fundsReserve,
            related=related,
            prescription=prescription,
            originalPrescription=originalPrescription,
            payee=payee,
            referral=referral,
            facility=facility,
            claim=claim,
            claimResponse=claimResponse,
            outcome=outcome,
            disposition=disposition,
            preAuthRef=preAuthRef,
            preAuthRefPeriod=preAuthRefPeriod,
            careTeam=careTeam,
            supportingInfo=supportingInfo,
            diagnosis=diagnosis,
            procedure=procedure,
            precedence=precedence,
            insurance=insurance,
            accident=accident,
            item=item,
            addItem=addItem,
            adjudication=adjudication,
            total=total,
            payment=payment,
            formCode=formCode,
            form=form,
            processNote=processNote,
            benefitPeriod=benefitPeriod,
            benefitBalance=benefitBalance,
        )
        super().include_null_properties(include_null_properties=True)

    @staticmethod
    def schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.meta import (
            AutoMapperElasticSearchMeta as MetaSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.narrative import (
            AutoMapperElasticSearchNarrative as NarrativeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_related import (
            AutoMapperElasticSearchExplanationOfBenefit_Related as ExplanationOfBenefit_RelatedSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_payee import (
            AutoMapperElasticSearchExplanationOfBenefit_Payee as ExplanationOfBenefit_PayeeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_careteam import (
            AutoMapperElasticSearchExplanationOfBenefit_CareTeam as ExplanationOfBenefit_CareTeamSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_supportinginfo import (
            AutoMapperElasticSearchExplanationOfBenefit_SupportingInfo as ExplanationOfBenefit_SupportingInfoSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_diagnosis import (
            AutoMapperElasticSearchExplanationOfBenefit_Diagnosis as ExplanationOfBenefit_DiagnosisSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_procedure import (
            AutoMapperElasticSearchExplanationOfBenefit_Procedure as ExplanationOfBenefit_ProcedureSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.positiveint import (
            AutoMapperElasticSearchpositiveInt as positiveIntSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_insurance import (
            AutoMapperElasticSearchExplanationOfBenefit_Insurance as ExplanationOfBenefit_InsuranceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_accident import (
            AutoMapperElasticSearchExplanationOfBenefit_Accident as ExplanationOfBenefit_AccidentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_item import (
            AutoMapperElasticSearchExplanationOfBenefit_Item as ExplanationOfBenefit_ItemSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_additem import (
            AutoMapperElasticSearchExplanationOfBenefit_AddItem as ExplanationOfBenefit_AddItemSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_adjudication import (
            AutoMapperElasticSearchExplanationOfBenefit_Adjudication as ExplanationOfBenefit_AdjudicationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_total import (
            AutoMapperElasticSearchExplanationOfBenefit_Total as ExplanationOfBenefit_TotalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_payment import (
            AutoMapperElasticSearchExplanationOfBenefit_Payment as ExplanationOfBenefit_PaymentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_processnote import (
            AutoMapperElasticSearchExplanationOfBenefit_ProcessNote as ExplanationOfBenefit_ProcessNoteSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.explanationofbenefit_benefitbalance import (
            AutoMapperElasticSearchExplanationOfBenefit_BenefitBalance as ExplanationOfBenefit_BenefitBalanceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ExplanationOfBenefit") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ExplanationOfBenefit"]
        schema = StructType(
            [
                # This is a ExplanationOfBenefit resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A unique identifier assigned to this explanation of benefit.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The status of the resource instance.
                StructField("status", StringType(), True),
                # The category of claim, e.g. oral, pharmacy, vision, institutional,
                # professional.
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A finer grained suite of claim type codes which may convey additional
                # information such as Inpatient vs Outpatient and/or a specialty service.
                StructField(
                    "subType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code to indicate whether the nature of the request is: to request
                # adjudication of products and services previously rendered; or requesting
                # authorization and adjudication for provision in the future; or requesting the
                # non-binding adjudication of the listed products and services which could be
                # provided in the future.
                StructField(
                    "use",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The party to whom the professional services and/or products have been supplied
                # or are being considered and for whom actual for forecast reimbursement is
                # sought.
                StructField(
                    "patient",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period for which charges are being submitted.
                StructField(
                    "billablePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date this resource was created.
                StructField(
                    "created",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Individual who created the claim, predetermination or preauthorization.
                StructField(
                    "enterer",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The party responsible for authorization, adjudication and reimbursement.
                StructField(
                    "insurer",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The provider which is responsible for the claim, predetermination or
                # preauthorization.
                StructField(
                    "provider",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The provider-required urgency of processing the request. Typical values
                # include: stat, routine deferred.
                StructField(
                    "priority",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code to indicate whether and for whom funds are to be reserved for future
                # claims.
                StructField(
                    "fundsReserveRequested",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code, used only on a response to a preauthorization, to indicate whether the
                # benefits payable have been reserved and for whom.
                StructField(
                    "fundsReserve",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Other claims which are related to this claim such as prior submissions or
                # claims for related services or for the same event.
                StructField(
                    "related",
                    ArrayType(
                        ExplanationOfBenefit_RelatedSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Prescription to support the dispensing of pharmacy, device or vision products.
                StructField(
                    "prescription",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Original prescription which has been superseded by this prescription to
                # support the dispensing of pharmacy services, medications or products.
                StructField(
                    "originalPrescription",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The party to be reimbursed for cost of the products and services according to
                # the terms of the policy.
                StructField(
                    "payee",
                    ExplanationOfBenefit_PayeeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a referral resource.
                StructField(
                    "referral",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Facility where the services were provided.
                StructField(
                    "facility",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The business identifier for the instance of the adjudication request: claim
                # predetermination or preauthorization.
                StructField(
                    "claim",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The business identifier for the instance of the adjudication response: claim,
                # predetermination or preauthorization response.
                StructField(
                    "claimResponse",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The outcome of the claim, predetermination, or preauthorization processing.
                StructField(
                    "outcome",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
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
                    ArrayType(
                        PeriodSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The members of the team who provided the products and services.
                StructField(
                    "careTeam",
                    ArrayType(
                        ExplanationOfBenefit_CareTeamSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Additional information codes regarding exceptions, special considerations, the
                # condition, situation, prior or concurrent issues.
                StructField(
                    "supportingInfo",
                    ArrayType(
                        ExplanationOfBenefit_SupportingInfoSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Information about diagnoses relevant to the claim items.
                StructField(
                    "diagnosis",
                    ArrayType(
                        ExplanationOfBenefit_DiagnosisSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Procedures performed on the patient relevant to the billing items with the
                # claim.
                StructField(
                    "procedure",
                    ArrayType(
                        ExplanationOfBenefit_ProcedureSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # This indicates the relative order of a series of EOBs related to different
                # coverages for the same suite of services.
                StructField(
                    "precedence",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Financial instruments for reimbursement for the health care products and
                # services specified on the claim.
                StructField(
                    "insurance",
                    ArrayType(
                        ExplanationOfBenefit_InsuranceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Details of a accident which resulted in injuries which required the products
                # and services listed in the claim.
                StructField(
                    "accident",
                    ExplanationOfBenefit_AccidentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A claim line. Either a simple (a product or service) or a 'group' of details
                # which can also be a simple items or groups of sub-details.
                StructField(
                    "item",
                    ArrayType(
                        ExplanationOfBenefit_ItemSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The first-tier service adjudications for payor added product or service lines.
                StructField(
                    "addItem",
                    ArrayType(
                        ExplanationOfBenefit_AddItemSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The adjudication results which are presented at the header level rather than
                # at the line-item or add-item levels.
                StructField(
                    "adjudication",
                    ArrayType(
                        ExplanationOfBenefit_AdjudicationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Categorized monetary totals for the adjudication.
                StructField(
                    "total",
                    ArrayType(
                        ExplanationOfBenefit_TotalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Payment details for the adjudication of the claim.
                StructField(
                    "payment",
                    ExplanationOfBenefit_PaymentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code for the form to be used for printing the content.
                StructField(
                    "formCode",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The actual form, by reference or inclusion, for printing the content or an
                # EOB.
                StructField(
                    "form",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A note that describes or explains adjudication results in a human readable
                # form.
                StructField(
                    "processNote",
                    ArrayType(
                        ExplanationOfBenefit_ProcessNoteSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The term of the benefits documented in this response.
                StructField(
                    "benefitPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Balance by Benefit Category.
                StructField(
                    "benefitBalance",
                    ArrayType(
                        ExplanationOfBenefit_BenefitBalanceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
