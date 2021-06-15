from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchClaim(AutoMapperDataTypeComplexBase):
    """
    A provider issued list of professional services and products which have been
    provided, or are to be provided, to a patient which is sent to an insurer for
    reimbursement.
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
        fundsReserve: Optional[Any] = None,
        related: Optional[Any] = None,
        prescription: Optional[Any] = None,
        originalPrescription: Optional[Any] = None,
        payee: Optional[Any] = None,
        referral: Optional[Any] = None,
        facility: Optional[Any] = None,
        careTeam: Optional[Any] = None,
        supportingInfo: Optional[Any] = None,
        diagnosis: Optional[Any] = None,
        procedure: Optional[Any] = None,
        insurance: Optional[Any] = None,
        accident: Optional[Any] = None,
        item: Optional[Any] = None,
        total: Optional[Any] = None,
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
            fundsReserve=fundsReserve,
            related=related,
            prescription=prescription,
            originalPrescription=originalPrescription,
            payee=payee,
            referral=referral,
            facility=facility,
            careTeam=careTeam,
            supportingInfo=supportingInfo,
            diagnosis=diagnosis,
            procedure=procedure,
            insurance=insurance,
            accident=accident,
            item=item,
            total=total,
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
        A provider issued list of professional services and products which have been
        provided, or are to be provided, to a patient which is sent to an insurer for
        reimbursement.


        resourceType: This is a Claim resource

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

        identifier: A unique identifier assigned to this claim.

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
            or are being considered and for whom actual or forecast reimbursement is
            sought.

        billablePeriod: The period for which charges are being submitted.

        created: The date this resource was created.

        enterer: Individual who created the claim, predetermination or preauthorization.

        insurer: The Insurer who is target of the request.

        provider: The provider which is responsible for the claim, predetermination or
            preauthorization.

        priority: The provider-required urgency of processing the request. Typical values
            include: stat, routine deferred.

        fundsReserve: A code to indicate whether and for whom funds are to be reserved for future
            claims.

        related: Other claims which are related to this claim such as prior submissions or
            claims for related services or for the same event.

        prescription: Prescription to support the dispensing of pharmacy, device or vision products.

        originalPrescription: Original prescription which has been superseded by this prescription to
            support the dispensing of pharmacy services, medications or products.

        payee: The party to be reimbursed for cost of the products and services according to
            the terms of the policy.

        referral: A reference to a referral resource.

        facility: Facility where the services were provided.

        careTeam: The members of the team who provided the products and services.

        supportingInfo: Additional information codes regarding exceptions, special considerations, the
            condition, situation, prior or concurrent issues.

        diagnosis: Information about diagnoses relevant to the claim items.

        procedure: Procedures performed on the patient relevant to the billing items with the
            claim.

        insurance: Financial instruments for reimbursement for the health care products and
            services specified on the claim.

        accident: Details of an accident which resulted in injuries which required the products
            and services listed in the claim.

        item: A claim line. Either a simple  product or service or a 'group' of details
            which can each be a simple items or groups of sub-details.

        total: The total value of the all the items in the claim.

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
        from spark_fhir_schemas.pss_r4.complex_types.claim_related import (
            AutoMapperElasticSearchClaim_Related as Claim_RelatedSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_payee import (
            AutoMapperElasticSearchClaim_Payee as Claim_PayeeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_careteam import (
            AutoMapperElasticSearchClaim_CareTeam as Claim_CareTeamSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_supportinginfo import (
            AutoMapperElasticSearchClaim_SupportingInfo as Claim_SupportingInfoSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_diagnosis import (
            AutoMapperElasticSearchClaim_Diagnosis as Claim_DiagnosisSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_procedure import (
            AutoMapperElasticSearchClaim_Procedure as Claim_ProcedureSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_insurance import (
            AutoMapperElasticSearchClaim_Insurance as Claim_InsuranceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_accident import (
            AutoMapperElasticSearchClaim_Accident as Claim_AccidentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.claim_item import (
            AutoMapperElasticSearchClaim_Item as Claim_ItemSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.money import (
            AutoMapperElasticSearchMoney as MoneySchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Claim") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Claim"]
        schema = StructType(
            [
                # This is a Claim resource
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
                # A unique identifier assigned to this claim.
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
                StructField(
                    "status",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
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
                StructField("use", StringType(), True),
                # The party to whom the professional services and/or products have been supplied
                # or are being considered and for whom actual or forecast reimbursement is
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
                # The Insurer who is target of the request.
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
                        Claim_RelatedSchema.schema(
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
                    Claim_PayeeSchema.schema(
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
                # The members of the team who provided the products and services.
                StructField(
                    "careTeam",
                    ArrayType(
                        Claim_CareTeamSchema.schema(
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
                        Claim_SupportingInfoSchema.schema(
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
                        Claim_DiagnosisSchema.schema(
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
                        Claim_ProcedureSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Financial instruments for reimbursement for the health care products and
                # services specified on the claim.
                StructField(
                    "insurance",
                    ArrayType(
                        Claim_InsuranceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Details of an accident which resulted in injuries which required the products
                # and services listed in the claim.
                StructField(
                    "accident",
                    Claim_AccidentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A claim line. Either a simple  product or service or a 'group' of details
                # which can each be a simple items or groups of sub-details.
                StructField(
                    "item",
                    ArrayType(
                        Claim_ItemSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The total value of the all the items in the claim.
                StructField(
                    "total",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
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
