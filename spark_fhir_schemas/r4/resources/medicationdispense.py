from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicationDispense:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Indicates that a medication product is to be or has been dispensed for a named
        person/patient.  This includes a description of the medication product
        (supply) provided and the instructions for administering the medication.  The
        medication dispense is the result of a pharmacy system responding to a
        medication order.


        resourceType: This is a MedicationDispense resource

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

        identifier: Identifiers associated with this Medication Dispense that are defined by
            business processes and/or used to refer to it when a direct URL reference to
            the resource itself is not appropriate. They are business identifiers assigned
            to this resource by the performer or other systems and remain constant as the
            resource is updated and propagates from server to server.

        partOf: The procedure that trigger the dispense.

        status: A code specifying the state of the set of dispense events.

        statusReasonCodeableConcept: Indicates the reason why a dispense was not performed.

        statusReasonReference: Indicates the reason why a dispense was not performed.

        category: Indicates the type of medication dispense (for example, where the medication
            is expected to be consumed or administered (i.e. inpatient or outpatient)).

        medicationCodeableConcept: Identifies the medication being administered. This is either a link to a
            resource representing the details of the medication or a simple attribute
            carrying a code that identifies the medication from a known list of
            medications.

        medicationReference: Identifies the medication being administered. This is either a link to a
            resource representing the details of the medication or a simple attribute
            carrying a code that identifies the medication from a known list of
            medications.

        subject: A link to a resource representing the person or the group to whom the
            medication will be given.

        context: The encounter or episode of care that establishes the context for this event.

        supportingInformation: Additional information that supports the medication being dispensed.

        performer: Indicates who or what performed the event.

        location: The principal physical location where the dispense was performed.

        authorizingPrescription: Indicates the medication order that is being dispensed against.

        type: Indicates the type of dispensing event that is performed. For example, Trial
            Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.

        quantity: The amount of medication that has been dispensed. Includes unit of measure.

        daysSupply: The amount of medication expressed as a timing amount.

        whenPrepared: The time when the dispensed product was packaged and reviewed.

        whenHandedOver: The time the dispensed product was provided to the patient or their
            representative.

        destination: Identification of the facility/location where the medication was shipped to,
            as part of the dispense event.

        receiver: Identifies the person who picked up the medication.  This will usually be a
            patient or their caregiver, but some cases exist where it can be a healthcare
            professional.

        note: Extra information about the dispense that could not be conveyed in the other
            attributes.

        dosageInstruction: Indicates how the medication is to be used by the patient.

        substitution: Indicates whether or not substitution was made as part of the dispense.  In
            some cases, substitution will be expected but does not happen, in other cases
            substitution is not expected but does happen.  This block explains what
            substitution did or did not happen and why.  If nothing is specified,
            substitution was not done.

        detectedIssue: Indicates an actual or potential clinical issue with or between one or more
            active or proposed clinical actions for a patient; e.g. drug-drug interaction,
            duplicate therapy, dosage alert etc.

        eventHistory: A summary of the events of interest that have occurred, such as when the
            dispense was verified.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.medicationdispense_performer import MedicationDispense_Performer
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.dosage import Dosage
        from spark_fhir_schemas.r4.complex_types.medicationdispense_substitution import MedicationDispense_Substitution
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MedicationDispense resource
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
                # Identifiers associated with this Medication Dispense that are defined by
                # business processes and/or used to refer to it when a direct URL reference to
                # the resource itself is not appropriate. They are business identifiers assigned
                # to this resource by the performer or other systems and remain constant as the
                # resource is updated and propagates from server to server.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The procedure that trigger the dispense.
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A code specifying the state of the set of dispense events.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates the reason why a dispense was not performed.
                StructField(
                    "statusReasonCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates the reason why a dispense was not performed.
                StructField(
                    "statusReasonReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Indicates the type of medication dispense (for example, where the medication
                # is expected to be consumed or administered (i.e. inpatient or outpatient)).
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identifies the medication being administered. This is either a link to a
                # resource representing the details of the medication or a simple attribute
                # carrying a code that identifies the medication from a known list of
                # medications.
                StructField(
                    "medicationCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Identifies the medication being administered. This is either a link to a
                # resource representing the details of the medication or a simple attribute
                # carrying a code that identifies the medication from a known list of
                # medications.
                StructField(
                    "medicationReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A link to a resource representing the person or the group to whom the
                # medication will be given.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The encounter or episode of care that establishes the context for this event.
                StructField(
                    "context", Reference.get_schema(recursion_depth + 1), True
                ),
                # Additional information that supports the medication being dispensed.
                StructField(
                    "supportingInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Indicates who or what performed the event.
                StructField(
                    "performer",
                    ArrayType(
                        MedicationDispense_Performer.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The principal physical location where the dispense was performed.
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                # Indicates the medication order that is being dispensed against.
                StructField(
                    "authorizingPrescription",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Indicates the type of dispensing event that is performed. For example, Trial
                # Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The amount of medication that has been dispensed. Includes unit of measure.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # The amount of medication expressed as a timing amount.
                StructField(
                    "daysSupply", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The time when the dispensed product was packaged and reviewed.
                StructField(
                    "whenPrepared", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # The time the dispensed product was provided to the patient or their
                # representative.
                StructField(
                    "whenHandedOver", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Identification of the facility/location where the medication was shipped to,
                # as part of the dispense event.
                StructField(
                    "destination", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Identifies the person who picked up the medication.  This will usually be a
                # patient or their caregiver, but some cases exist where it can be a healthcare
                # professional.
                StructField(
                    "receiver",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Extra information about the dispense that could not be conveyed in the other
                # attributes.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Indicates how the medication is to be used by the patient.
                StructField(
                    "dosageInstruction",
                    ArrayType(Dosage.get_schema(recursion_depth + 1)), True
                ),
                # Indicates whether or not substitution was made as part of the dispense.  In
                # some cases, substitution will be expected but does not happen, in other cases
                # substitution is not expected but does happen.  This block explains what
                # substitution did or did not happen and why.  If nothing is specified,
                # substitution was not done.
                StructField(
                    "substitution",
                    MedicationDispense_Substitution.
                    get_schema(recursion_depth + 1), True
                ),
                # Indicates an actual or potential clinical issue with or between one or more
                # active or proposed clinical actions for a patient; e.g. drug-drug interaction,
                # duplicate therapy, dosage alert etc.
                StructField(
                    "detectedIssue",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # A summary of the events of interest that have occurred, such as when the
                # dispense was verified.
                StructField(
                    "eventHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
