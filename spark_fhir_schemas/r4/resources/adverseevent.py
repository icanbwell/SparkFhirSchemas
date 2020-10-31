from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class AdverseEvent:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Actual or  potential/avoided event causing unintended physical injury
        resulting from or contributed to by medical care, a research study or other
        healthcare setting factors that requires additional monitoring, treatment, or
        hospitalization, or that results in death.


        resourceType: This is a AdverseEvent resource

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

        identifier: Business identifiers assigned to this adverse event by the performer or other
            systems which remain constant as the resource is updated and propagates from
            server to server.

        actuality: Whether the event actually happened, or just had the potential to. Note that
            this is independent of whether anyone was affected or harmed or how severely.

        category: The overall type of event, intended for search and filtering purposes.

        event: This element defines the specific type of event that occurred or that was
            prevented from occurring.

        subject: This subject or group impacted by the event.

        encounter: The Encounter during which AdverseEvent was created or to which the creation
            of this record is tightly associated.

        date: The date (and perhaps time) when the adverse event occurred.

        detected: Estimated or actual date the AdverseEvent began, in the opinion of the
            reporter.

        recordedDate: The date on which the existence of the AdverseEvent was first recorded.

        resultingCondition: Includes information about the reaction that occurred as a result of exposure
            to a substance (for example, a drug or a chemical).

        location: The information about where the adverse event occurred.

        seriousness: Assessment whether this event was of real importance.

        severity: Describes the severity of the adverse event, in relation to the subject.
            Contrast to AdverseEvent.seriousness - a severe rash might not be serious, but
            a mild heart problem is.

        outcome: Describes the type of outcome from the adverse event.

        recorder: Information on who recorded the adverse event.  May be the patient or a
            practitioner.

        contributor: Parties that may or should contribute or have contributed information to the
            adverse event, which can consist of one or more activities.  Such information
            includes information leading to the decision to perform the activity and how
            to perform the activity (e.g. consultant), information that the activity
            itself seeks to reveal (e.g. informant of clinical history), or information
            about what activity was performed (e.g. informant witness).

        suspectEntity: Describes the entity that is suspected to have caused the adverse event.

        subjectMedicalHistory: AdverseEvent.subjectMedicalHistory.

        referenceDocument: AdverseEvent.referenceDocument.

        study: AdverseEvent.study.

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
        from spark_fhir_schemas.r4.complex_types.adverseevent_suspectentity import AdverseEvent_SuspectEntity
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a AdverseEvent resource
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
                # Business identifiers assigned to this adverse event by the performer or other
                # systems which remain constant as the resource is updated and propagates from
                # server to server.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # Whether the event actually happened, or just had the potential to. Note that
                # this is independent of whether anyone was affected or harmed or how severely.
                StructField("actuality", StringType(), True),
                # The overall type of event, intended for search and filtering purposes.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # This element defines the specific type of event that occurred or that was
                # prevented from occurring.
                StructField(
                    "event", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # This subject or group impacted by the event.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The Encounter during which AdverseEvent was created or to which the creation
                # of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The date (and perhaps time) when the adverse event occurred.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Estimated or actual date the AdverseEvent began, in the opinion of the
                # reporter.
                StructField(
                    "detected", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The date on which the existence of the AdverseEvent was first recorded.
                StructField(
                    "recordedDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Includes information about the reaction that occurred as a result of exposure
                # to a substance (for example, a drug or a chemical).
                StructField(
                    "resultingCondition",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The information about where the adverse event occurred.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # Assessment whether this event was of real importance.
                StructField(
                    "seriousness",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Describes the severity of the adverse event, in relation to the subject.
                # Contrast to AdverseEvent.seriousness - a severe rash might not be serious, but
                # a mild heart problem is.
                StructField(
                    "severity",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Describes the type of outcome from the adverse event.
                StructField(
                    "outcome", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Information on who recorded the adverse event.  May be the patient or a
                # practitioner.
                StructField(
                    "recorder", Reference.get_schema(recursion_depth + 1), True
                ),
                # Parties that may or should contribute or have contributed information to the
                # adverse event, which can consist of one or more activities.  Such information
                # includes information leading to the decision to perform the activity and how
                # to perform the activity (e.g. consultant), information that the activity
                # itself seeks to reveal (e.g. informant of clinical history), or information
                # about what activity was performed (e.g. informant witness).
                StructField(
                    "contributor",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Describes the entity that is suspected to have caused the adverse event.
                StructField(
                    "suspectEntity",
                    ArrayType(
                        AdverseEvent_SuspectEntity.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # AdverseEvent.subjectMedicalHistory.
                StructField(
                    "subjectMedicalHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # AdverseEvent.referenceDocument.
                StructField(
                    "referenceDocument",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # AdverseEvent.study.
                StructField(
                    "study",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
