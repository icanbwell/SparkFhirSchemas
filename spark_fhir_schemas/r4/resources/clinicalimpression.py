from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ClinicalImpression:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A record of a clinical assessment performed to determine what problem(s) may
        affect the patient and before planning the treatments or management strategies
        that are best to manage a patient's condition. Assessments are often 1:1 with
        a clinical consultation / encounter,  but this varies greatly depending on the
        clinical workflow. This resource is called "ClinicalImpression" rather than
        "ClinicalAssessment" to avoid confusion with the recording of assessment tools
        such as Apgar score.


        resourceType: This is a ClinicalImpression resource

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

        identifier: Business identifiers assigned to this clinical impression by the performer or
            other systems which remain constant as the resource is updated and propagates
            from server to server.

        status: Identifies the workflow status of the assessment.

        statusReason: Captures the reason for the current state of the ClinicalImpression.

        code: Categorizes the type of clinical assessment performed.

        description: A summary of the context and/or cause of the assessment - why / where it was
            performed, and what patient events/status prompted it.

        subject: The patient or group of individuals assessed as part of this record.

        encounter: The Encounter during which this ClinicalImpression was created or to which the
            creation of this record is tightly associated.

        effectiveDateTime: The point in time or period over which the subject was assessed.

        effectivePeriod: The point in time or period over which the subject was assessed.

        date: Indicates when the documentation of the assessment was complete.

        assessor: The clinician performing the assessment.

        previous: A reference to the last assessment that was conducted on this patient.
            Assessments are often/usually ongoing in nature; a care provider (practitioner
            or team) will make new assessments on an ongoing basis as new data arises or
            the patient's conditions changes.

        problem: A list of the relevant problems/conditions for a patient.

        investigation: One or more sets of investigations (signs, symptoms, etc.). The actual
            grouping of investigations varies greatly depending on the type and context of
            the assessment. These investigations may include data generated during the
            assessment process, or data previously generated and recorded that is
            pertinent to the outcomes.

        protocol: Reference to a specific published clinical protocol that was followed during
            this assessment, and/or that provides evidence in support of the diagnosis.

        summary: A text summary of the investigations and the diagnosis.

        finding: Specific findings or diagnoses that were considered likely or relevant to
            ongoing treatment.

        prognosisCodeableConcept: Estimate of likely outcome.

        prognosisReference: RiskAssessment expressing likely outcome.

        supportingInfo: Information supporting the clinical impression.

        note: Commentary about the impression, typically recorded after the impression
            itself was made, though supplemental notes by the original author could also
            appear.

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
        from spark_fhir_schemas.r4.complex_types.clinicalimpression_investigation import ClinicalImpression_Investigation
        from spark_fhir_schemas.r4.complex_types.clinicalimpression_finding import ClinicalImpression_Finding
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ClinicalImpression resource
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
                # Business identifiers assigned to this clinical impression by the performer or
                # other systems which remain constant as the resource is updated and propagates
                # from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Identifies the workflow status of the assessment.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Captures the reason for the current state of the ClinicalImpression.
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Categorizes the type of clinical assessment performed.
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A summary of the context and/or cause of the assessment - why / where it was
                # performed, and what patient events/status prompted it.
                StructField("description", StringType(), True),
                # The patient or group of individuals assessed as part of this record.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The Encounter during which this ClinicalImpression was created or to which the
                # creation of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The point in time or period over which the subject was assessed.
                StructField("effectiveDateTime", StringType(), True),
                # The point in time or period over which the subject was assessed.
                StructField(
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates when the documentation of the assessment was complete.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The clinician performing the assessment.
                StructField(
                    "assessor", Reference.get_schema(recursion_depth + 1), True
                ),
                # A reference to the last assessment that was conducted on this patient.
                # Assessments are often/usually ongoing in nature; a care provider (practitioner
                # or team) will make new assessments on an ongoing basis as new data arises or
                # the patient's conditions changes.
                StructField(
                    "previous", Reference.get_schema(recursion_depth + 1), True
                ),
                # A list of the relevant problems/conditions for a patient.
                StructField(
                    "problem",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # One or more sets of investigations (signs, symptoms, etc.). The actual
                # grouping of investigations varies greatly depending on the type and context of
                # the assessment. These investigations may include data generated during the
                # assessment process, or data previously generated and recorded that is
                # pertinent to the outcomes.
                StructField(
                    "investigation",
                    ArrayType(
                        ClinicalImpression_Investigation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Reference to a specific published clinical protocol that was followed during
                # this assessment, and/or that provides evidence in support of the diagnosis.
                StructField(
                    "protocol", ArrayType(uri.get_schema(recursion_depth + 1)),
                    True
                ),
                # A text summary of the investigations and the diagnosis.
                StructField("summary", StringType(), True),
                # Specific findings or diagnoses that were considered likely or relevant to
                # ongoing treatment.
                StructField(
                    "finding",
                    ArrayType(
                        ClinicalImpression_Finding.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Estimate of likely outcome.
                StructField(
                    "prognosisCodeableConcept",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # RiskAssessment expressing likely outcome.
                StructField(
                    "prognosisReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Information supporting the clinical impression.
                StructField(
                    "supportingInfo",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Commentary about the impression, typically recorded after the impression
                # itself was made, though supplemental notes by the original author could also
                # appear.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
