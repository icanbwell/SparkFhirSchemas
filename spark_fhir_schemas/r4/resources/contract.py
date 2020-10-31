from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.contract_contentdefinition import Contract_ContentDefinition
        from spark_fhir_schemas.r4.complex_types.contract_term import Contract_Term
        from spark_fhir_schemas.r4.complex_types.contract_signer import Contract_Signer
        from spark_fhir_schemas.r4.complex_types.contract_friendly import Contract_Friendly
        from spark_fhir_schemas.r4.complex_types.contract_legal import Contract_Legal
        from spark_fhir_schemas.r4.complex_types.contract_rule import Contract_Rule
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Contract resource
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
                # Unique identifier for this Contract or a derivative that references a Source
                # Contract.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Canonical identifier for this contract, represented as a URI (globally
                # unique).
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # An edition identifier used for business purposes to label business significant
                # variants.
                StructField("version", StringType(), True),
                # The status of the resource instance.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Legal states of the formation of a legal instrument, which is a formally
                # executed written document that can be formally attributed to its author,
                # records and formally expresses a legally enforceable act, process, or
                # contractual duty, obligation, or right, and therefore evidences that act,
                # process, or agreement.
                StructField(
                    "legalState",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The URL pointing to a FHIR-defined Contract Definition that is adhered to in
                # whole or part by this Contract.
                StructField(
                    "instantiatesCanonical",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The URL pointing to an externally maintained definition that is adhered to in
                # whole or in part by this Contract.
                StructField(
                    "instantiatesUri", uri.get_schema(recursion_depth + 1),
                    True
                ),
                # The minimal content derived from the basal information source at a specific
                # stage in its lifecycle.
                StructField(
                    "contentDerivative",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # When this  Contract was issued.
                StructField(
                    "issued", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Relevant time or time-period when this Contract is applicable.
                StructField(
                    "applies", Period.get_schema(recursion_depth + 1), True
                ),
                # Event resulting in discontinuation or termination of this Contract instance by
                # one or more parties to the contract.
                StructField(
                    "expirationType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The target entity impacted by or of interest to parties to the agreement.
                StructField(
                    "subject",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A formally or informally recognized grouping of people, principals,
                # organizations, or jurisdictions formed for the purpose of achieving some form
                # of collective action such as the promulgation, administration and enforcement
                # of contracts and policies.
                StructField(
                    "authority",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Recognized governance framework or system operating with a circumscribed scope
                # in accordance with specified principles, policies, processes or procedures for
                # managing rights, actions, or behaviors of parties or principals relative to
                # resources.
                StructField(
                    "domain",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Sites in which the contract is complied with,  exercised, or in force.
                StructField(
                    "site",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
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
                    "author", Reference.get_schema(recursion_depth + 1), True
                ),
                # A selector of legal concerns for this Contract definition, derivative, or
                # instance in any legal state.
                StructField(
                    "scope", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Narrows the range of legal concerns to focus on the achievement of specific
                # contractual objectives.
                StructField(
                    "topicCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Narrows the range of legal concerns to focus on the achievement of specific
                # contractual objectives.
                StructField(
                    "topicReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A high-level category for the legal instrument, whether constructed as a
                # Contract definition, derivative, or instance in any legal state.  Provides
                # additional information about its content within the context of the Contract's
                # scope to distinguish the kinds of systems that would be interested in the
                # contract.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Sub-category for the Contract that distinguishes the kinds of systems that
                # would be interested in the Contract within the context of the Contract's
                # scope.
                StructField(
                    "subType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Precusory content developed with a focus and intent of supporting the
                # formation a Contract instance, which may be associated with and transformable
                # into a Contract.
                StructField(
                    "contentDefinition",
                    Contract_ContentDefinition.get_schema(recursion_depth + 1),
                    True
                ),
                # One or more Contract Provisions, which may be related and conveyed as a group,
                # and may contain nested groups.
                StructField(
                    "term",
                    ArrayType(Contract_Term.get_schema(recursion_depth + 1)),
                    True
                ),
                # Information that may be needed by/relevant to the performer in their execution
                # of this term action.
                StructField(
                    "supportingInfo",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Links to Provenance records for past versions of this Contract definition,
                # derivative, or instance, which identify key state transitions or updates that
                # are likely to be relevant to a user looking at the current version of the
                # Contract.  The Provence.entity indicates the target that was changed in the
                # update. http://build.fhir.org/provenance-definitions.html#Provenance.entity.
                StructField(
                    "relevantHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Parties with legal standing in the Contract, including the principal parties,
                # the grantor(s) and grantee(s), which are any person or organization bound by
                # the contract, and any ancillary parties, which facilitate the execution of the
                # contract such as a notary or witness.
                StructField(
                    "signer",
                    ArrayType(Contract_Signer.get_schema(recursion_depth + 1)),
                    True
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
                        Contract_Friendly.get_schema(recursion_depth + 1)
                    ), True
                ),
                # List of Legal expressions or representations of this Contract.
                StructField(
                    "legal",
                    ArrayType(Contract_Legal.get_schema(recursion_depth + 1)),
                    True
                ),
                # List of Computable Policy Rule Language Representations of this Contract.
                StructField(
                    "rule",
                    ArrayType(Contract_Rule.get_schema(recursion_depth + 1)),
                    True
                ),
                # Legally binding Contract: This is the signed and legally recognized
                # representation of the Contract, which is considered the "source of truth" and
                # which would be the basis for legal action related to enforcement of this
                # Contract.
                StructField(
                    "legallyBindingAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # Legally binding Contract: This is the signed and legally recognized
                # representation of the Contract, which is considered the "source of truth" and
                # which would be the basis for legal action related to enforcement of this
                # Contract.
                StructField(
                    "legallyBindingReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
