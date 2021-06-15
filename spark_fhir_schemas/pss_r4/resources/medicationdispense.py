from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMedicationDispense(AutoMapperDataTypeComplexBase):
    """
    Indicates that a medication product is to be or has been dispensed for a named
    person/patient.  This includes a description of the medication product
    (supply) provided and the instructions for administering the medication.  The
    medication dispense is the result of a pharmacy system responding to a
    medication order.
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
        partOf: Optional[Any] = None,
        status: Optional[Any] = None,
        statusReasonCodeableConcept: Optional[Any] = None,
        statusReasonReference: Optional[Any] = None,
        category: Optional[Any] = None,
        medicationCodeableConcept: Optional[Any] = None,
        medicationReference: Optional[Any] = None,
        subject: Optional[Any] = None,
        context: Optional[Any] = None,
        supportingInformation: Optional[Any] = None,
        performer: Optional[Any] = None,
        location: Optional[Any] = None,
        authorizingPrescription: Optional[Any] = None,
        type_: Optional[Any] = None,
        quantity: Optional[Any] = None,
        daysSupply: Optional[Any] = None,
        whenPrepared: Optional[Any] = None,
        whenHandedOver: Optional[Any] = None,
        destination: Optional[Any] = None,
        receiver: Optional[Any] = None,
        note: Optional[Any] = None,
        dosageInstruction: Optional[Any] = None,
        substitution: Optional[Any] = None,
        detectedIssue: Optional[Any] = None,
        eventHistory: Optional[Any] = None,
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
            partOf=partOf,
            status=status,
            statusReasonCodeableConcept=statusReasonCodeableConcept,
            statusReasonReference=statusReasonReference,
            category=category,
            medicationCodeableConcept=medicationCodeableConcept,
            medicationReference=medicationReference,
            subject=subject,
            context=context,
            supportingInformation=supportingInformation,
            performer=performer,
            location=location,
            authorizingPrescription=authorizingPrescription,
            type_=type_,
            quantity=quantity,
            daysSupply=daysSupply,
            whenPrepared=whenPrepared,
            whenHandedOver=whenHandedOver,
            destination=destination,
            receiver=receiver,
            note=note,
            dosageInstruction=dosageInstruction,
            substitution=substitution,
            detectedIssue=detectedIssue,
            eventHistory=eventHistory,
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
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationdispense_performer import (
            AutoMapperElasticSearchMedicationDispense_Performer as MedicationDispense_PerformerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.dosage import (
            AutoMapperElasticSearchDosage as DosageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationdispense_substitution import (
            AutoMapperElasticSearchMedicationDispense_Substitution as MedicationDispense_SubstitutionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MedicationDispense") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MedicationDispense"]
        schema = StructType(
            [
                # This is a MedicationDispense resource
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
                # Identifiers associated with this Medication Dispense that are defined by
                # business processes and/or used to refer to it when a direct URL reference to
                # the resource itself is not appropriate. They are business identifiers assigned
                # to this resource by the performer or other systems and remain constant as the
                # resource is updated and propagates from server to server.
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
                # The procedure that trigger the dispense.
                StructField(
                    "partOf",
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
                # A code specifying the state of the set of dispense events.
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
                # Indicates the reason why a dispense was not performed.
                StructField(
                    "statusReasonCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the reason why a dispense was not performed.
                StructField(
                    "statusReasonReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the type of medication dispense (for example, where the medication
                # is expected to be consumed or administered (i.e. inpatient or outpatient)).
                StructField(
                    "category",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the medication being administered. This is either a link to a
                # resource representing the details of the medication or a simple attribute
                # carrying a code that identifies the medication from a known list of
                # medications.
                StructField(
                    "medicationCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the medication being administered. This is either a link to a
                # resource representing the details of the medication or a simple attribute
                # carrying a code that identifies the medication from a known list of
                # medications.
                StructField(
                    "medicationReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A link to a resource representing the person or the group to whom the
                # medication will be given.
                StructField(
                    "subject",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The encounter or episode of care that establishes the context for this event.
                StructField(
                    "context",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional information that supports the medication being dispensed.
                StructField(
                    "supportingInformation",
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
                # Indicates who or what performed the event.
                StructField(
                    "performer",
                    ArrayType(
                        MedicationDispense_PerformerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The principal physical location where the dispense was performed.
                StructField(
                    "location",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the medication order that is being dispensed against.
                StructField(
                    "authorizingPrescription",
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
                # Indicates the type of dispensing event that is performed. For example, Trial
                # Fill, Completion of Trial, Partial Fill, Emergency Fill, Samples, etc.
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
                # The amount of medication that has been dispensed. Includes unit of measure.
                StructField(
                    "quantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The amount of medication expressed as a timing amount.
                StructField(
                    "daysSupply",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The time when the dispensed product was packaged and reviewed.
                StructField(
                    "whenPrepared",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The time the dispensed product was provided to the patient or their
                # representative.
                StructField(
                    "whenHandedOver",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identification of the facility/location where the medication was shipped to,
                # as part of the dispense event.
                StructField(
                    "destination",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the person who picked up the medication.  This will usually be a
                # patient or their caregiver, but some cases exist where it can be a healthcare
                # professional.
                StructField(
                    "receiver",
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
                # Extra information about the dispense that could not be conveyed in the other
                # attributes.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates how the medication is to be used by the patient.
                StructField(
                    "dosageInstruction",
                    ArrayType(
                        DosageSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates whether or not substitution was made as part of the dispense.  In
                # some cases, substitution will be expected but does not happen, in other cases
                # substitution is not expected but does happen.  This block explains what
                # substitution did or did not happen and why.  If nothing is specified,
                # substitution was not done.
                StructField(
                    "substitution",
                    MedicationDispense_SubstitutionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates an actual or potential clinical issue with or between one or more
                # active or proposed clinical actions for a patient; e.g. drug-drug interaction,
                # duplicate therapy, dosage alert etc.
                StructField(
                    "detectedIssue",
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
                # A summary of the events of interest that have occurred, such as when the
                # dispense was verified.
                StructField(
                    "eventHistory",
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
