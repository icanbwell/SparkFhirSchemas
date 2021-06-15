from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchContract(AutoMapperDataTypeComplexBase):
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
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
        url: Optional[Any] = None,
        version: Optional[Any] = None,
        status: Optional[Any] = None,
        legalState: Optional[Any] = None,
        instantiatesCanonical: Optional[Any] = None,
        instantiatesUri: Optional[Any] = None,
        contentDerivative: Optional[Any] = None,
        issued: Optional[Any] = None,
        applies: Optional[Any] = None,
        expirationType: Optional[Any] = None,
        subject: Optional[Any] = None,
        authority: Optional[Any] = None,
        domain: Optional[Any] = None,
        site: Optional[Any] = None,
        name: Optional[Any] = None,
        title: Optional[Any] = None,
        subtitle: Optional[Any] = None,
        alias: Optional[Any] = None,
        author: Optional[Any] = None,
        scope: Optional[Any] = None,
        topicCodeableConcept: Optional[Any] = None,
        topicReference: Optional[Any] = None,
        type_: Optional[Any] = None,
        subType: Optional[Any] = None,
        contentDefinition: Optional[Any] = None,
        term: Optional[Any] = None,
        supportingInfo: Optional[Any] = None,
        relevantHistory: Optional[Any] = None,
        signer: Optional[Any] = None,
        friendly: Optional[Any] = None,
        legal: Optional[Any] = None,
        rule: Optional[Any] = None,
        legallyBindingAttachment: Optional[Any] = None,
        legallyBindingReference: Optional[Any] = None,
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
            url=url,
            version=version,
            status=status,
            legalState=legalState,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            contentDerivative=contentDerivative,
            issued=issued,
            applies=applies,
            expirationType=expirationType,
            subject=subject,
            authority=authority,
            domain=domain,
            site=site,
            name=name,
            title=title,
            subtitle=subtitle,
            alias=alias,
            author=author,
            scope=scope,
            topicCodeableConcept=topicCodeableConcept,
            topicReference=topicReference,
            type_=type_,
            subType=subType,
            contentDefinition=contentDefinition,
            term=term,
            supportingInfo=supportingInfo,
            relevantHistory=relevantHistory,
            signer=signer,
            friendly=friendly,
            legal=legal,
            rule=rule,
            legallyBindingAttachment=legallyBindingAttachment,
            legallyBindingReference=legallyBindingReference,
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
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.


        resourceType: This is a Contract resource

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

        identifier: Unique identifier for this Contract or a derivative that references a Source
            Contract.

        url: Canonical identifier for this contract, represented as a URI (globally
            unique).

        version: An edition identifier used for business purposes to label business significant
            variants.

        status: The status of the resource instance.

        legalState: Legal states of the formation of a legal instrument, which is a formally
            executed written document that can be formally attributed to its author,
            records and formally expresses a legally enforceable act, process, or
            contractual duty, obligation, or right, and therefore evidences that act,
            process, or agreement.

        instantiatesCanonical: The URL pointing to a FHIR-defined Contract Definition that is adhered to in
            whole or part by this Contract.

        instantiatesUri: The URL pointing to an externally maintained definition that is adhered to in
            whole or in part by this Contract.

        contentDerivative: The minimal content derived from the basal information source at a specific
            stage in its lifecycle.

        issued: When this  Contract was issued.

        applies: Relevant time or time-period when this Contract is applicable.

        expirationType: Event resulting in discontinuation or termination of this Contract instance by
            one or more parties to the contract.

        subject: The target entity impacted by or of interest to parties to the agreement.

        authority: A formally or informally recognized grouping of people, principals,
            organizations, or jurisdictions formed for the purpose of achieving some form
            of collective action such as the promulgation, administration and enforcement
            of contracts and policies.

        domain: Recognized governance framework or system operating with a circumscribed scope
            in accordance with specified principles, policies, processes or procedures for
            managing rights, actions, or behaviors of parties or principals relative to
            resources.

        site: Sites in which the contract is complied with,  exercised, or in force.

        name: A natural language name identifying this Contract definition, derivative, or
            instance in any legal state. Provides additional information about its
            content. This name should be usable as an identifier for the module by machine
            processing applications such as code generation.

        title: A short, descriptive, user-friendly title for this Contract definition,
            derivative, or instance in any legal state.t giving additional information
            about its content.

        subtitle: An explanatory or alternate user-friendly title for this Contract definition,
            derivative, or instance in any legal state.t giving additional information
            about its content.

        alias: Alternative representation of the title for this Contract definition,
            derivative, or instance in any legal state., e.g., a domain specific contract
            number related to legislation.

        author: The individual or organization that authored the Contract definition,
            derivative, or instance in any legal state.

        scope: A selector of legal concerns for this Contract definition, derivative, or
            instance in any legal state.

        topicCodeableConcept: Narrows the range of legal concerns to focus on the achievement of specific
            contractual objectives.

        topicReference: Narrows the range of legal concerns to focus on the achievement of specific
            contractual objectives.

        type: A high-level category for the legal instrument, whether constructed as a
            Contract definition, derivative, or instance in any legal state.  Provides
            additional information about its content within the context of the Contract's
            scope to distinguish the kinds of systems that would be interested in the
            contract.

        subType: Sub-category for the Contract that distinguishes the kinds of systems that
            would be interested in the Contract within the context of the Contract's
            scope.

        contentDefinition: Precusory content developed with a focus and intent of supporting the
            formation a Contract instance, which may be associated with and transformable
            into a Contract.

        term: One or more Contract Provisions, which may be related and conveyed as a group,
            and may contain nested groups.

        supportingInfo: Information that may be needed by/relevant to the performer in their execution
            of this term action.

        relevantHistory: Links to Provenance records for past versions of this Contract definition,
            derivative, or instance, which identify key state transitions or updates that
            are likely to be relevant to a user looking at the current version of the
            Contract.  The Provence.entity indicates the target that was changed in the
            update. http://build.fhir.org/provenance-definitions.html#Provenance.entity.

        signer: Parties with legal standing in the Contract, including the principal parties,
            the grantor(s) and grantee(s), which are any person or organization bound by
            the contract, and any ancillary parties, which facilitate the execution of the
            contract such as a notary or witness.

        friendly: The "patient friendly language" versionof the Contract in whole or in parts.
            "Patient friendly language" means the representation of the Contract and
            Contract Provisions in a manner that is readily accessible and understandable
            by a layperson in accordance with best practices for communication styles that
            ensure that those agreeing to or signing the Contract understand the roles,
            actions, obligations, responsibilities, and implication of the agreement.

        legal: List of Legal expressions or representations of this Contract.

        rule: List of Computable Policy Rule Language Representations of this Contract.

        legallyBindingAttachment: Legally binding Contract: This is the signed and legally recognized
            representation of the Contract, which is considered the "source of truth" and
            which would be the basis for legal action related to enforcement of this
            Contract.

        legallyBindingReference: Legally binding Contract: This is the signed and legally recognized
            representation of the Contract, which is considered the "source of truth" and
            which would be the basis for legal action related to enforcement of this
            Contract.

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
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_contentdefinition import (
            AutoMapperElasticSearchContract_ContentDefinition as Contract_ContentDefinitionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_term import (
            AutoMapperElasticSearchContract_Term as Contract_TermSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_signer import (
            AutoMapperElasticSearchContract_Signer as Contract_SignerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_friendly import (
            AutoMapperElasticSearchContract_Friendly as Contract_FriendlySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_legal import (
            AutoMapperElasticSearchContract_Legal as Contract_LegalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_rule import (
            AutoMapperElasticSearchContract_Rule as Contract_RuleSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Contract") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Contract"]
        schema = StructType(
            [
                # This is a Contract resource
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
                # Unique identifier for this Contract or a derivative that references a Source
                # Contract.
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
                # Canonical identifier for this contract, represented as a URI (globally
                # unique).
                StructField(
                    "url",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An edition identifier used for business purposes to label business significant
                # variants.
                StructField("version", StringType(), True),
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
                # Legal states of the formation of a legal instrument, which is a formally
                # executed written document that can be formally attributed to its author,
                # records and formally expresses a legally enforceable act, process, or
                # contractual duty, obligation, or right, and therefore evidences that act,
                # process, or agreement.
                StructField(
                    "legalState",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The URL pointing to a FHIR-defined Contract Definition that is adhered to in
                # whole or part by this Contract.
                StructField(
                    "instantiatesCanonical",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The URL pointing to an externally maintained definition that is adhered to in
                # whole or in part by this Contract.
                StructField(
                    "instantiatesUri",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The minimal content derived from the basal information source at a specific
                # stage in its lifecycle.
                StructField(
                    "contentDerivative",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # When this  Contract was issued.
                StructField(
                    "issued",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Relevant time or time-period when this Contract is applicable.
                StructField(
                    "applies",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Event resulting in discontinuation or termination of this Contract instance by
                # one or more parties to the contract.
                StructField(
                    "expirationType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The target entity impacted by or of interest to parties to the agreement.
                StructField(
                    "subject",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A formally or informally recognized grouping of people, principals,
                # organizations, or jurisdictions formed for the purpose of achieving some form
                # of collective action such as the promulgation, administration and enforcement
                # of contracts and policies.
                StructField(
                    "authority",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Recognized governance framework or system operating with a circumscribed scope
                # in accordance with specified principles, policies, processes or procedures for
                # managing rights, actions, or behaviors of parties or principals relative to
                # resources.
                StructField(
                    "domain",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Sites in which the contract is complied with,  exercised, or in force.
                StructField(
                    "site",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A natural language name identifying this Contract definition, derivative, or
                # instance in any legal state. Provides additional information about its
                # content. This name should be usable as an identifier for the module by machine
                # processing applications such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for this Contract definition,
                # derivative, or instance in any legal state.t giving additional information
                # about its content.
                StructField("title", StringType(), True),
                # An explanatory or alternate user-friendly title for this Contract definition,
                # derivative, or instance in any legal state.t giving additional information
                # about its content.
                StructField("subtitle", StringType(), True),
                # Alternative representation of the title for this Contract definition,
                # derivative, or instance in any legal state., e.g., a domain specific contract
                # number related to legislation.
                StructField("alias", ArrayType(StringType()), True),
                # The individual or organization that authored the Contract definition,
                # derivative, or instance in any legal state.
                StructField(
                    "author",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A selector of legal concerns for this Contract definition, derivative, or
                # instance in any legal state.
                StructField(
                    "scope",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Narrows the range of legal concerns to focus on the achievement of specific
                # contractual objectives.
                StructField(
                    "topicCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Narrows the range of legal concerns to focus on the achievement of specific
                # contractual objectives.
                StructField(
                    "topicReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A high-level category for the legal instrument, whether constructed as a
                # Contract definition, derivative, or instance in any legal state.  Provides
                # additional information about its content within the context of the Contract's
                # scope to distinguish the kinds of systems that would be interested in the
                # contract.
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
                # Sub-category for the Contract that distinguishes the kinds of systems that
                # would be interested in the Contract within the context of the Contract's
                # scope.
                StructField(
                    "subType",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Precusory content developed with a focus and intent of supporting the
                # formation a Contract instance, which may be associated with and transformable
                # into a Contract.
                StructField(
                    "contentDefinition",
                    Contract_ContentDefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # One or more Contract Provisions, which may be related and conveyed as a group,
                # and may contain nested groups.
                StructField(
                    "term",
                    ArrayType(
                        Contract_TermSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Information that may be needed by/relevant to the performer in their execution
                # of this term action.
                StructField(
                    "supportingInfo",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Links to Provenance records for past versions of this Contract definition,
                # derivative, or instance, which identify key state transitions or updates that
                # are likely to be relevant to a user looking at the current version of the
                # Contract.  The Provence.entity indicates the target that was changed in the
                # update. http://build.fhir.org/provenance-definitions.html#Provenance.entity.
                StructField(
                    "relevantHistory",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Parties with legal standing in the Contract, including the principal parties,
                # the grantor(s) and grantee(s), which are any person or organization bound by
                # the contract, and any ancillary parties, which facilitate the execution of the
                # contract such as a notary or witness.
                StructField(
                    "signer",
                    ArrayType(
                        Contract_SignerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The "patient friendly language" versionof the Contract in whole or in parts.
                # "Patient friendly language" means the representation of the Contract and
                # Contract Provisions in a manner that is readily accessible and understandable
                # by a layperson in accordance with best practices for communication styles that
                # ensure that those agreeing to or signing the Contract understand the roles,
                # actions, obligations, responsibilities, and implication of the agreement.
                StructField(
                    "friendly",
                    ArrayType(
                        Contract_FriendlySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # List of Legal expressions or representations of this Contract.
                StructField(
                    "legal",
                    ArrayType(
                        Contract_LegalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # List of Computable Policy Rule Language Representations of this Contract.
                StructField(
                    "rule",
                    ArrayType(
                        Contract_RuleSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Legally binding Contract: This is the signed and legally recognized
                # representation of the Contract, which is considered the "source of truth" and
                # which would be the basis for legal action related to enforcement of this
                # Contract.
                StructField(
                    "legallyBindingAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Legally binding Contract: This is the signed and legally recognized
                # representation of the Contract, which is considered the "source of truth" and
                # which would be the basis for legal action related to enforcement of this
                # Contract.
                StructField(
                    "legallyBindingReference",
                    ReferenceSchema.schema(
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
