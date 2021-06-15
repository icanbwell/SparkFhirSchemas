from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchMedicationRequest(AutoMapperDataTypeComplexBase):
    """
    An order or request for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
    to generalize the use across inpatient and outpatient settings, including care
    plans, etc., and to harmonize with workflow patterns.
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
        statusReason: Optional[Any] = None,
        intent: Optional[Any] = None,
        category: Optional[Any] = None,
        priority: Optional[Any] = None,
        doNotPerform: Optional[Any] = None,
        reportedBoolean: Optional[Any] = None,
        reportedReference: Optional[Any] = None,
        medicationCodeableConcept: Optional[Any] = None,
        medicationReference: Optional[Any] = None,
        subject: Optional[Any] = None,
        encounter: Optional[Any] = None,
        supportingInformation: Optional[Any] = None,
        authoredOn: Optional[Any] = None,
        requester: Optional[Any] = None,
        performer: Optional[Any] = None,
        performerType: Optional[Any] = None,
        recorder: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        instantiatesCanonical: Optional[Any] = None,
        instantiatesUri: Optional[Any] = None,
        basedOn: Optional[Any] = None,
        groupIdentifier: Optional[Any] = None,
        courseOfTherapyType: Optional[Any] = None,
        insurance: Optional[Any] = None,
        note: Optional[Any] = None,
        dosageInstruction: Optional[Any] = None,
        dispenseRequest: Optional[Any] = None,
        substitution: Optional[Any] = None,
        priorPrescription: Optional[Any] = None,
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
            status=status,
            statusReason=statusReason,
            intent=intent,
            category=category,
            priority=priority,
            doNotPerform=doNotPerform,
            reportedBoolean=reportedBoolean,
            reportedReference=reportedReference,
            medicationCodeableConcept=medicationCodeableConcept,
            medicationReference=medicationReference,
            subject=subject,
            encounter=encounter,
            supportingInformation=supportingInformation,
            authoredOn=authoredOn,
            requester=requester,
            performer=performer,
            performerType=performerType,
            recorder=recorder,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            groupIdentifier=groupIdentifier,
            courseOfTherapyType=courseOfTherapyType,
            insurance=insurance,
            note=note,
            dosageInstruction=dosageInstruction,
            dispenseRequest=dispenseRequest,
            substitution=substitution,
            priorPrescription=priorPrescription,
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
        An order or request for both supply of the medication and the instructions for
        administration of the medication to a patient. The resource is called
        "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder"
        to generalize the use across inpatient and outpatient settings, including care
        plans, etc., and to harmonize with workflow patterns.


        resourceType: This is a MedicationRequest resource

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

        identifier: Identifiers associated with this medication request that are defined by
            business processes and/or used to refer to it when a direct URL reference to
            the resource itself is not appropriate. They are business identifiers assigned
            to this resource by the performer or other systems and remain constant as the
            resource is updated and propagates from server to server.

        status: A code specifying the current state of the order.  Generally, this will be
            active or completed state.

        statusReason: Captures the reason for the current state of the MedicationRequest.

        intent: Whether the request is a proposal, plan, or an original order.

        category: Indicates the type of medication request (for example, where the medication is
            expected to be consumed or administered (i.e. inpatient or outpatient)).

        priority: Indicates how quickly the Medication Request should be addressed with respect
            to other requests.

        doNotPerform: If true indicates that the provider is asking for the medication request not
            to occur.

        reportedBoolean: Indicates if this record was captured as a secondary 'reported' record rather
            than as an original primary source-of-truth record.  It may also indicate the
            source of the report.

        reportedReference: Indicates if this record was captured as a secondary 'reported' record rather
            than as an original primary source-of-truth record.  It may also indicate the
            source of the report.

        medicationCodeableConcept: Identifies the medication being requested. This is a link to a resource that
            represents the medication which may be the details of the medication or simply
            an attribute carrying a code that identifies the medication from a known list
            of medications.

        medicationReference: Identifies the medication being requested. This is a link to a resource that
            represents the medication which may be the details of the medication or simply
            an attribute carrying a code that identifies the medication from a known list
            of medications.

        subject: A link to a resource representing the person or set of individuals to whom the
            medication will be given.

        encounter: The Encounter during which this [x] was created or to which the creation of
            this record is tightly associated.

        supportingInformation: Include additional information (for example, patient height and weight) that
            supports the ordering of the medication.

        authoredOn: The date (and perhaps time) when the prescription was initially written or
            authored on.

        requester: The individual, organization, or device that initiated the request and has
            responsibility for its activation.

        performer: The specified desired performer of the medication treatment (e.g. the
            performer of the medication administration).

        performerType: Indicates the type of performer of the administration of the medication.

        recorder: The person who entered the order on behalf of another individual for example
            in the case of a verbal or a telephone order.

        reasonCode: The reason or the indication for ordering or not ordering the medication.

        reasonReference: Condition or observation that supports why the medication was ordered.

        instantiatesCanonical: The URL pointing to a protocol, guideline, orderset, or other definition that
            is adhered to in whole or in part by this MedicationRequest.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            MedicationRequest.

        basedOn: A plan or request that is fulfilled in whole or in part by this medication
            request.

        groupIdentifier: A shared identifier common to all requests that were authorized more or less
            simultaneously by a single author, representing the identifier of the
            requisition or prescription.

        courseOfTherapyType: The description of the overall patte3rn of the administration of the
            medication to the patient.

        insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
            determinations that may be required for delivering the requested service.

        note: Extra information about the prescription that could not be conveyed by the
            other attributes.

        dosageInstruction: Indicates how the medication is to be used by the patient.

        dispenseRequest: Indicates the specific details for the dispense or medication supply part of a
            medication request (also known as a Medication Prescription or Medication
            Order).  Note that this information is not always sent with the order.  There
            may be in some settings (e.g. hospitals) institutional or system support for
            completing the dispense details in the pharmacy department.

        substitution: Indicates whether or not substitution can or should be part of the dispense.
            In some cases, substitution must happen, in other cases substitution must not
            happen. This block explains the prescriber's intent. If nothing is specified
            substitution may be done.

        priorPrescription: A link to a resource representing an earlier order related order or
            prescription.

        detectedIssue: Indicates an actual or potential clinical issue with or between one or more
            active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
            duplicate therapy, dosage alert etc.

        eventHistory: Links to Provenance records for past versions of this resource or fulfilling
            request or event resources that identify key state transitions or updates that
            are likely to be relevant to a user looking at the current version of the
            resource.

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
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.dosage import (
            AutoMapperElasticSearchDosage as DosageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationrequest_dispenserequest import (
            AutoMapperElasticSearchMedicationRequest_DispenseRequest as MedicationRequest_DispenseRequestSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicationrequest_substitution import (
            AutoMapperElasticSearchMedicationRequest_Substitution as MedicationRequest_SubstitutionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MedicationRequest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MedicationRequest"]
        schema = StructType(
            [
                # This is a MedicationRequest resource
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
                # Identifiers associated with this medication request that are defined by
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
                # A code specifying the current state of the order.  Generally, this will be
                # active or completed state.
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
                # Captures the reason for the current state of the MedicationRequest.
                StructField(
                    "statusReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Whether the request is a proposal, plan, or an original order.
                StructField(
                    "intent",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the type of medication request (for example, where the medication is
                # expected to be consumed or administered (i.e. inpatient or outpatient)).
                StructField(
                    "category",
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
                # Indicates how quickly the Medication Request should be addressed with respect
                # to other requests.
                StructField(
                    "priority",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If true indicates that the provider is asking for the medication request not
                # to occur.
                StructField("doNotPerform", BooleanType(), True),
                # Indicates if this record was captured as a secondary 'reported' record rather
                # than as an original primary source-of-truth record.  It may also indicate the
                # source of the report.
                StructField("reportedBoolean", BooleanType(), True),
                # Indicates if this record was captured as a secondary 'reported' record rather
                # than as an original primary source-of-truth record.  It may also indicate the
                # source of the report.
                StructField(
                    "reportedReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the medication being requested. This is a link to a resource that
                # represents the medication which may be the details of the medication or simply
                # an attribute carrying a code that identifies the medication from a known list
                # of medications.
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
                # Identifies the medication being requested. This is a link to a resource that
                # represents the medication which may be the details of the medication or simply
                # an attribute carrying a code that identifies the medication from a known list
                # of medications.
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
                # A link to a resource representing the person or set of individuals to whom the
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
                # The Encounter during which this [x] was created or to which the creation of
                # this record is tightly associated.
                StructField(
                    "encounter",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Include additional information (for example, patient height and weight) that
                # supports the ordering of the medication.
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
                # The date (and perhaps time) when the prescription was initially written or
                # authored on.
                StructField(
                    "authoredOn",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The individual, organization, or device that initiated the request and has
                # responsibility for its activation.
                StructField(
                    "requester",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The specified desired performer of the medication treatment (e.g. the
                # performer of the medication administration).
                StructField(
                    "performer",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the type of performer of the administration of the medication.
                StructField(
                    "performerType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The person who entered the order on behalf of another individual for example
                # in the case of a verbal or a telephone order.
                StructField(
                    "recorder",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The reason or the indication for ordering or not ordering the medication.
                StructField(
                    "reasonCode",
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
                # Condition or observation that supports why the medication was ordered.
                StructField(
                    "reasonReference",
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
                # The URL pointing to a protocol, guideline, orderset, or other definition that
                # is adhered to in whole or in part by this MedicationRequest.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(
                        canonicalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this
                # MedicationRequest.
                StructField(
                    "instantiatesUri",
                    ArrayType(
                        uriSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A plan or request that is fulfilled in whole or in part by this medication
                # request.
                StructField(
                    "basedOn",
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
                # A shared identifier common to all requests that were authorized more or less
                # simultaneously by a single author, representing the identifier of the
                # requisition or prescription.
                StructField(
                    "groupIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The description of the overall patte3rn of the administration of the
                # medication to the patient.
                StructField(
                    "courseOfTherapyType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Insurance plans, coverage extensions, pre-authorizations and/or pre-
                # determinations that may be required for delivering the requested service.
                StructField(
                    "insurance",
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
                # Extra information about the prescription that could not be conveyed by the
                # other attributes.
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
                # Indicates the specific details for the dispense or medication supply part of a
                # medication request (also known as a Medication Prescription or Medication
                # Order).  Note that this information is not always sent with the order.  There
                # may be in some settings (e.g. hospitals) institutional or system support for
                # completing the dispense details in the pharmacy department.
                StructField(
                    "dispenseRequest",
                    MedicationRequest_DispenseRequestSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates whether or not substitution can or should be part of the dispense.
                # In some cases, substitution must happen, in other cases substitution must not
                # happen. This block explains the prescriber's intent. If nothing is specified
                # substitution may be done.
                StructField(
                    "substitution",
                    MedicationRequest_SubstitutionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A link to a resource representing an earlier order related order or
                # prescription.
                StructField(
                    "priorPrescription",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates an actual or potential clinical issue with or between one or more
                # active or proposed clinical actions for a patient; e.g. Drug-drug interaction,
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
                # Links to Provenance records for past versions of this resource or fulfilling
                # request or event resources that identify key state transitions or updates that
                # are likely to be relevant to a user looking at the current version of the
                # resource.
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
