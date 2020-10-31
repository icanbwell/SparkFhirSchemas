from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class AllergyIntolerance:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Risk of harmful or undesirable, physiological response which is unique to an
        individual and associated with exposure to a substance.


        resourceType: This is a AllergyIntolerance resource

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

        identifier: Business identifiers assigned to this AllergyIntolerance by the performer or
            other systems which remain constant as the resource is updated and propagates
            from server to server.

        clinicalStatus: The clinical status of the allergy or intolerance.

        verificationStatus: Assertion about certainty associated with the propensity, or potential risk,
            of a reaction to the identified substance (including pharmaceutical product).

        type: Identification of the underlying physiological mechanism for the reaction
            risk.

        category: Category of the identified substance.

        criticality: Estimate of the potential clinical harm, or seriousness, of the reaction to
            the identified substance.

        code: Code for an allergy or intolerance statement (either a positive or a
            negated/excluded statement).  This may be a code for a substance or
            pharmaceutical product that is considered to be responsible for the adverse
            reaction risk (e.g., "Latex"), an allergy or intolerance condition (e.g.,
            "Latex allergy"), or a negated/excluded code for a specific substance or class
            (e.g., "No latex allergy") or a general or categorical negated statement
            (e.g.,  "No known allergy", "No known drug allergies").  Note: the substance
            for a specific reaction may be different from the substance identified as the
            cause of the risk, but it must be consistent with it. For instance, it may be
            a more specific substance (e.g. a brand medication) or a composite product
            that includes the identified substance. It must be clinically safe to only
            process the 'code' and ignore the 'reaction.substance'.  If a receiving system
            is unable to confirm that AllergyIntolerance.reaction.substance falls within
            the semantic scope of AllergyIntolerance.code, then the receiving system
            should ignore AllergyIntolerance.reaction.substance.

        patient: The patient who has the allergy or intolerance.

        encounter: The encounter when the allergy or intolerance was asserted.

        onsetDateTime: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetAge: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetPeriod: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetRange: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetString: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        recordedDate: The recordedDate represents when this particular AllergyIntolerance record was
            created in the system, which is often a system-generated date.

        recorder: Individual who recorded the record and takes responsibility for its content.

        asserter: The source of the information about the allergy that is recorded.

        lastOccurrence: Represents the date and/or time of the last known occurrence of a reaction
            event.

        note: Additional narrative about the propensity for the Adverse Reaction, not
            captured in other fields.

        reaction: Details about each adverse reaction event linked to exposure to the identified
            substance.

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
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.allergyintolerance_reaction import AllergyIntolerance_Reaction
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a AllergyIntolerance resource
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
                # Business identifiers assigned to this AllergyIntolerance by the performer or
                # other systems which remain constant as the resource is updated and propagates
                # from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The clinical status of the allergy or intolerance.
                StructField(
                    "clinicalStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Assertion about certainty associated with the propensity, or potential risk,
                # of a reaction to the identified substance (including pharmaceutical product).
                StructField(
                    "verificationStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identification of the underlying physiological mechanism for the reaction
                # risk.
                StructField("type", StringType(), True),
                # Category of the identified substance.
                # Estimate of the potential clinical harm, or seriousness, of the reaction to
                # the identified substance.
                StructField("criticality", StringType(), True),
                # Code for an allergy or intolerance statement (either a positive or a
                # negated/excluded statement).  This may be a code for a substance or
                # pharmaceutical product that is considered to be responsible for the adverse
                # reaction risk (e.g., "Latex"), an allergy or intolerance condition (e.g.,
                # "Latex allergy"), or a negated/excluded code for a specific substance or class
                # (e.g., "No latex allergy") or a general or categorical negated statement
                # (e.g.,  "No known allergy", "No known drug allergies").  Note: the substance
                # for a specific reaction may be different from the substance identified as the
                # cause of the risk, but it must be consistent with it. For instance, it may be
                # a more specific substance (e.g. a brand medication) or a composite product
                # that includes the identified substance. It must be clinically safe to only
                # process the 'code' and ignore the 'reaction.substance'.  If a receiving system
                # is unable to confirm that AllergyIntolerance.reaction.substance falls within
                # the semantic scope of AllergyIntolerance.code, then the receiving system
                # should ignore AllergyIntolerance.reaction.substance.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The patient who has the allergy or intolerance.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # The encounter when the allergy or intolerance was asserted.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField("onsetDateTime", StringType(), True),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField(
                    "onsetAge", Age.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField(
                    "onsetPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField(
                    "onsetRange", Range.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField("onsetString", StringType(), True),
                # The recordedDate represents when this particular AllergyIntolerance record was
                # created in the system, which is often a system-generated date.
                StructField(
                    "recordedDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Individual who recorded the record and takes responsibility for its content.
                StructField(
                    "recorder", Reference.get_schema(recursion_depth + 1), True
                ),
                # The source of the information about the allergy that is recorded.
                StructField(
                    "asserter", Reference.get_schema(recursion_depth + 1), True
                ),
                # Represents the date and/or time of the last known occurrence of a reaction
                # event.
                StructField(
                    "lastOccurrence", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Additional narrative about the propensity for the Adverse Reaction, not
                # captured in other fields.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Details about each adverse reaction event linked to exposure to the identified
                # substance.
                StructField(
                    "reaction",
                    ArrayType(
                        AllergyIntolerance_Reaction.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
