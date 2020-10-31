from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Consent:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A record of a healthcare consumer’s  choices, which permits or denies
        identified recipient(s) or recipient role(s) to perform one or more actions
        within a given policy context, for specific purposes and periods of time.


        resourceType: This is a Consent resource

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

        identifier: Unique identifier for this copy of the Consent Statement.

        status: Indicates the current state of this consent.

        scope: A selector of the type of consent being presented: ADR, Privacy, Treatment,
            Research.  This list is now extensible.

        category: A classification of the type of consents found in the statement. This element
            supports indexing and retrieval of consent statements.

        patient: The patient/healthcare consumer to whom this consent applies.

        dateTime: When this  Consent was issued / created / indexed.

        performer: Either the Grantor, which is the entity responsible for granting the rights
            listed in a Consent Directive or the Grantee, which is the entity responsible
            for complying with the Consent Directive, including any obligations or
            limitations on authorizations and enforcement of prohibitions.

        organization: The organization that manages the consent, and the framework within which it
            is executed.

        sourceAttachment: The source on which this consent statement is based. The source might be a
            scanned original paper form, or a reference to a consent that links back to
            such a source, a reference to a document repository (e.g. XDS) that stores the
            original consent document.

        sourceReference: The source on which this consent statement is based. The source might be a
            scanned original paper form, or a reference to a consent that links back to
            such a source, a reference to a document repository (e.g. XDS) that stores the
            original consent document.

        policy: The references to the policies that are included in this consent scope.
            Policies may be organizational, but are often defined jurisdictionally, or in
            law.

        policyRule: A reference to the specific base computable regulation or policy.

        verification: Whether a treatment instruction (e.g. artificial respiration yes or no) was
            verified with the patient, his/her family or another authorized person.

        provision: An exception to the base policy of this consent. An exception can be an
            addition or removal of access permissions.

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
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.consent_policy import Consent_Policy
        from spark_fhir_schemas.r4.complex_types.consent_verification import Consent_Verification
        from spark_fhir_schemas.r4.complex_types.consent_provision import Consent_Provision
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Consent resource
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
                # Unique identifier for this copy of the Consent Statement.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Indicates the current state of this consent.
                StructField("status", StringType(), True),
                # A selector of the type of consent being presented: ADR, Privacy, Treatment,
                # Research.  This list is now extensible.
                StructField(
                    "scope", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A classification of the type of consents found in the statement. This element
                # supports indexing and retrieval of consent statements.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The patient/healthcare consumer to whom this consent applies.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # When this  Consent was issued / created / indexed.
                StructField(
                    "dateTime", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Either the Grantor, which is the entity responsible for granting the rights
                # listed in a Consent Directive or the Grantee, which is the entity responsible
                # for complying with the Consent Directive, including any obligations or
                # limitations on authorizations and enforcement of prohibitions.
                StructField(
                    "performer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The organization that manages the consent, and the framework within which it
                # is executed.
                StructField(
                    "organization",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The source on which this consent statement is based. The source might be a
                # scanned original paper form, or a reference to a consent that links back to
                # such a source, a reference to a document repository (e.g. XDS) that stores the
                # original consent document.
                StructField(
                    "sourceAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                # The source on which this consent statement is based. The source might be a
                # scanned original paper form, or a reference to a consent that links back to
                # such a source, a reference to a document repository (e.g. XDS) that stores the
                # original consent document.
                StructField(
                    "sourceReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The references to the policies that are included in this consent scope.
                # Policies may be organizational, but are often defined jurisdictionally, or in
                # law.
                StructField(
                    "policy",
                    ArrayType(Consent_Policy.get_schema(recursion_depth + 1)),
                    True
                ),
                # A reference to the specific base computable regulation or policy.
                StructField(
                    "policyRule",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Whether a treatment instruction (e.g. artificial respiration yes or no) was
                # verified with the patient, his/her family or another authorized person.
                StructField(
                    "verification",
                    ArrayType(
                        Consent_Verification.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An exception to the base policy of this consent. An exception can be an
                # addition or removal of access permissions.
                StructField(
                    "provision",
                    Consent_Provision.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
