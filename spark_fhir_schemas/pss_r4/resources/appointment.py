from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchAppointment(AutoMapperDataTypeComplexBase):
    """
    A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one or
    more Encounter(s).
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
        cancelationReason: Optional[Any] = None,
        serviceCategory: Optional[Any] = None,
        serviceType: Optional[Any] = None,
        specialty: Optional[Any] = None,
        appointmentType: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        priority: Optional[Any] = None,
        description: Optional[Any] = None,
        supportingInformation: Optional[Any] = None,
        start: Optional[Any] = None,
        end: Optional[Any] = None,
        minutesDuration: Optional[Any] = None,
        slot: Optional[Any] = None,
        created: Optional[Any] = None,
        comment: Optional[Any] = None,
        patientInstruction: Optional[Any] = None,
        basedOn: Optional[Any] = None,
        participant: Optional[Any] = None,
        requestedPeriod: Optional[Any] = None,
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
            cancelationReason=cancelationReason,
            serviceCategory=serviceCategory,
            serviceType=serviceType,
            specialty=specialty,
            appointmentType=appointmentType,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            priority=priority,
            description=description,
            supportingInformation=supportingInformation,
            start=start,
            end=end,
            minutesDuration=minutesDuration,
            slot=slot,
            created=created,
            comment=comment,
            patientInstruction=patientInstruction,
            basedOn=basedOn,
            participant=participant,
            requestedPeriod=requestedPeriod,
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
        A booking of a healthcare event among patient(s), practitioner(s), related
        person(s) and/or device(s) for a specific date/time. This may result in one or
        more Encounter(s).


        resourceType: This is a Appointment resource

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

        identifier: This records identifiers associated with this appointment concern that are
            defined by business processes and/or used to refer to it when a direct URL
            reference to the resource itself is not appropriate (e.g. in CDA documents, or
            in written / printed documentation).

        status: The overall status of the Appointment. Each of the participants has their own
            participation status which indicates their involvement in the process, however
            this status indicates the shared status.

        cancelationReason: The coded reason for the appointment being cancelled. This is often used in
            reporting/billing/futher processing to determine if further actions are
            required, or specific fees apply.

        serviceCategory: A broad categorization of the service that is to be performed during this
            appointment.

        serviceType: The specific service that is to be performed during this appointment.

        specialty: The specialty of a practitioner that would be required to perform the service
            requested in this appointment.

        appointmentType: The style of appointment or patient that has been booked in the slot (not
            service type).

        reasonCode: The coded reason that this appointment is being scheduled. This is more
            clinical than administrative.

        reasonReference: Reason the appointment has been scheduled to take place, as specified using
            information from another resource. When the patient arrives and the encounter
            begins it may be used as the admission diagnosis. The indication will
            typically be a Condition (with other resources referenced in the
            evidence.detail), or a Procedure.

        priority: The priority of the appointment. Can be used to make informed decisions if
            needing to re-prioritize appointments. (The iCal Standard specifies 0 as
            undefined, 1 as highest, 9 as lowest priority).

        description: The brief description of the appointment as would be shown on a subject line
            in a meeting request, or appointment list. Detailed or expanded information
            should be put in the comment field.

        supportingInformation: Additional information to support the appointment provided when making the
            appointment.

        start: Date/Time that the appointment is to take place.

        end: Date/Time that the appointment is to conclude.

        minutesDuration: Number of minutes that the appointment is to take. This can be less than the
            duration between the start and end times.  For example, where the actual time
            of appointment is only an estimate or if a 30 minute appointment is being
            requested, but any time would work.  Also, if there is, for example, a planned
            15 minute break in the middle of a long appointment, the duration may be 15
            minutes less than the difference between the start and end.

        slot: The slots from the participants' schedules that will be filled by the
            appointment.

        created: The date that this appointment was initially created. This could be different
            to the meta.lastModified value on the initial entry, as this could have been
            before the resource was created on the FHIR server, and should remain
            unchanged over the lifespan of the appointment.

        comment: Additional comments about the appointment.

        patientInstruction: While Appointment.comment contains information for internal use,
            Appointment.patientInstructions is used to capture patient facing information
            about the Appointment (e.g. please bring your referral or fast from 8pm night
            before).

        basedOn: The service request this appointment is allocated to assess (e.g. incoming
            referral or procedure request).

        participant: List of participants involved in the appointment.

        requestedPeriod: A set of date ranges (potentially including times) that the appointment is
            preferred to be scheduled within.

            The duration (usually in minutes) could also be provided to indicate the
            length of the appointment to fill and populate the start/end times for the
            actual allocated time. However, in other situations the duration may be
            calculated by the scheduling system.

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
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.instant import (
            AutoMapperElasticSearchinstant as instantSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.positiveint import (
            AutoMapperElasticSearchpositiveInt as positiveIntSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.appointment_participant import (
            AutoMapperElasticSearchAppointment_Participant as Appointment_ParticipantSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Appointment") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Appointment"]
        schema = StructType(
            [
                # This is a Appointment resource
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
                # This records identifiers associated with this appointment concern that are
                # defined by business processes and/or used to refer to it when a direct URL
                # reference to the resource itself is not appropriate (e.g. in CDA documents, or
                # in written / printed documentation).
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
                # The overall status of the Appointment. Each of the participants has their own
                # participation status which indicates their involvement in the process, however
                # this status indicates the shared status.
                StructField("status", StringType(), True),
                # The coded reason for the appointment being cancelled. This is often used in
                # reporting/billing/futher processing to determine if further actions are
                # required, or specific fees apply.
                StructField(
                    "cancelationReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A broad categorization of the service that is to be performed during this
                # appointment.
                StructField(
                    "serviceCategory",
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
                # The specific service that is to be performed during this appointment.
                StructField(
                    "serviceType",
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
                # The specialty of a practitioner that would be required to perform the service
                # requested in this appointment.
                StructField(
                    "specialty",
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
                # The style of appointment or patient that has been booked in the slot (not
                # service type).
                StructField(
                    "appointmentType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The coded reason that this appointment is being scheduled. This is more
                # clinical than administrative.
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
                # Reason the appointment has been scheduled to take place, as specified using
                # information from another resource. When the patient arrives and the encounter
                # begins it may be used as the admission diagnosis. The indication will
                # typically be a Condition (with other resources referenced in the
                # evidence.detail), or a Procedure.
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
                # The priority of the appointment. Can be used to make informed decisions if
                # needing to re-prioritize appointments. (The iCal Standard specifies 0 as
                # undefined, 1 as highest, 9 as lowest priority).
                StructField(
                    "priority",
                    unsignedIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The brief description of the appointment as would be shown on a subject line
                # in a meeting request, or appointment list. Detailed or expanded information
                # should be put in the comment field.
                StructField("description", StringType(), True),
                # Additional information to support the appointment provided when making the
                # appointment.
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
                # Date/Time that the appointment is to take place.
                StructField(
                    "start",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Date/Time that the appointment is to conclude.
                StructField(
                    "end",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Number of minutes that the appointment is to take. This can be less than the
                # duration between the start and end times.  For example, where the actual time
                # of appointment is only an estimate or if a 30 minute appointment is being
                # requested, but any time would work.  Also, if there is, for example, a planned
                # 15 minute break in the middle of a long appointment, the duration may be 15
                # minutes less than the difference between the start and end.
                StructField(
                    "minutesDuration",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The slots from the participants' schedules that will be filled by the
                # appointment.
                StructField(
                    "slot",
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
                # The date that this appointment was initially created. This could be different
                # to the meta.lastModified value on the initial entry, as this could have been
                # before the resource was created on the FHIR server, and should remain
                # unchanged over the lifespan of the appointment.
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
                # Additional comments about the appointment.
                StructField("comment", StringType(), True),
                # While Appointment.comment contains information for internal use,
                # Appointment.patientInstructions is used to capture patient facing information
                # about the Appointment (e.g. please bring your referral or fast from 8pm night
                # before).
                StructField("patientInstruction", StringType(), True),
                # The service request this appointment is allocated to assess (e.g. incoming
                # referral or procedure request).
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
                # List of participants involved in the appointment.
                StructField(
                    "participant",
                    ArrayType(
                        Appointment_ParticipantSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A set of date ranges (potentially including times) that the appointment is
                # preferred to be scheduled within.
                #
                # The duration (usually in minutes) could also be provided to indicate the
                # length of the appointment to fill and populate the start/end times for the
                # actual allocated time. However, in other situations the duration may be
                # calculated by the scheduling system.
                StructField(
                    "requestedPeriod",
                    ArrayType(
                        PeriodSchema.schema(
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