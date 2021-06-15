from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchEncounter(AutoMapperDataTypeComplexBase):
    """
    An interaction between a patient and healthcare provider(s) for the purpose of
    providing healthcare service(s) or assessing the health status of a patient.
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
        statusHistory: Optional[Any] = None,
        class_: Optional[Any] = None,
        classHistory: Optional[Any] = None,
        type_: Optional[Any] = None,
        serviceType: Optional[Any] = None,
        priority: Optional[Any] = None,
        subject: Optional[Any] = None,
        episodeOfCare: Optional[Any] = None,
        basedOn: Optional[Any] = None,
        participant: Optional[Any] = None,
        appointment: Optional[Any] = None,
        period: Optional[Any] = None,
        length: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        diagnosis: Optional[Any] = None,
        account: Optional[Any] = None,
        hospitalization: Optional[Any] = None,
        location: Optional[Any] = None,
        serviceProvider: Optional[Any] = None,
        partOf: Optional[Any] = None,
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
            statusHistory=statusHistory,
            class_=class_,
            classHistory=classHistory,
            type_=type_,
            serviceType=serviceType,
            priority=priority,
            subject=subject,
            episodeOfCare=episodeOfCare,
            basedOn=basedOn,
            participant=participant,
            appointment=appointment,
            period=period,
            length=length,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            diagnosis=diagnosis,
            account=account,
            hospitalization=hospitalization,
            location=location,
            serviceProvider=serviceProvider,
            partOf=partOf,
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
        An interaction between a patient and healthcare provider(s) for the purpose of
        providing healthcare service(s) or assessing the health status of a patient.


        resourceType: This is a Encounter resource

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

        identifier: Identifier(s) by which this encounter is known.

        status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +.

        statusHistory: The status history permits the encounter resource to contain the status
            history without needing to read through the historical versions of the
            resource, or even have the server store them.

        class: Concepts representing classification of patient encounter such as ambulatory
            (outpatient), inpatient, emergency, home health or others due to local
            variations.

        classHistory: The class history permits the tracking of the encounters transitions without
            needing to go  through the resource history.  This would be used for a case
            where an admission starts of as an emergency encounter, then transitions into
            an inpatient scenario. Doing this and not restarting a new encounter ensures
            that any lab/diagnostic results can more easily follow the patient and not
            require re-processing and not get lost or cancelled during a kind of discharge
            from emergency to inpatient.

        type: Specific type of encounter (e.g. e-mail consultation, surgical day-care,
            skilled nursing, rehabilitation).

        serviceType: Broad categorization of the service that is to be provided (e.g. cardiology).

        priority: Indicates the urgency of the encounter.

        subject: The patient or group present at the encounter.

        episodeOfCare: Where a specific encounter should be classified as a part of a specific
            episode(s) of care this field should be used. This association can facilitate
            grouping of related encounters together for a specific purpose, such as
            government reporting, issue tracking, association via a common problem.  The
            association is recorded on the encounter as these are typically created after
            the episode of care and grouped on entry rather than editing the episode of
            care to append another encounter to it (the episode of care could span years).

        basedOn: The request this encounter satisfies (e.g. incoming referral or procedure
            request).

        participant: The list of people responsible for providing the service.

        appointment: The appointment that scheduled this encounter.

        period: The start and end time of the encounter.

        length: Quantity of time the encounter lasted. This excludes the time during leaves of
            absence.

        reasonCode: Reason the encounter takes place, expressed as a code. For admissions, this
            can be used for a coded admission diagnosis.

        reasonReference: Reason the encounter takes place, expressed as a code. For admissions, this
            can be used for a coded admission diagnosis.

        diagnosis: The list of diagnosis relevant to this encounter.

        account: The set of accounts that may be used for billing for this Encounter.

        hospitalization: Details about the admission to a healthcare service.

        location: List of locations where  the patient has been during this encounter.

        serviceProvider: The organization that is primarily responsible for this Encounter's services.
            This MAY be the same as the organization on the Patient record, however it
            could be different, such as if the actor performing the services was from an
            external organization (which may be billed seperately) for an external
            consultation.  Refer to the example bundle showing an abbreviated set of
            Encounters for a colonoscopy.

        partOf: Another Encounter of which this encounter is a part of (administratively or in
            time).

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
        from spark_fhir_schemas.pss_r4.complex_types.encounter_statushistory import (
            AutoMapperElasticSearchEncounter_StatusHistory as Encounter_StatusHistorySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.encounter_classhistory import (
            AutoMapperElasticSearchEncounter_ClassHistory as Encounter_ClassHistorySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.encounter_participant import (
            AutoMapperElasticSearchEncounter_Participant as Encounter_ParticipantSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.encounter_diagnosis import (
            AutoMapperElasticSearchEncounter_Diagnosis as Encounter_DiagnosisSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.encounter_hospitalization import (
            AutoMapperElasticSearchEncounter_Hospitalization as Encounter_HospitalizationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.encounter_location import (
            AutoMapperElasticSearchEncounter_Location as Encounter_LocationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Encounter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Encounter"]
        schema = StructType(
            [
                # This is a Encounter resource
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
                # Identifier(s) by which this encounter is known.
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
                # planned | arrived | triaged | in-progress | onleave | finished | cancelled +.
                StructField("status", StringType(), True),
                # The status history permits the encounter resource to contain the status
                # history without needing to read through the historical versions of the
                # resource, or even have the server store them.
                StructField(
                    "statusHistory",
                    ArrayType(
                        Encounter_StatusHistorySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Concepts representing classification of patient encounter such as ambulatory
                # (outpatient), inpatient, emergency, home health or others due to local
                # variations.
                StructField(
                    "class",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The class history permits the tracking of the encounters transitions without
                # needing to go  through the resource history.  This would be used for a case
                # where an admission starts of as an emergency encounter, then transitions into
                # an inpatient scenario. Doing this and not restarting a new encounter ensures
                # that any lab/diagnostic results can more easily follow the patient and not
                # require re-processing and not get lost or cancelled during a kind of discharge
                # from emergency to inpatient.
                StructField(
                    "classHistory",
                    ArrayType(
                        Encounter_ClassHistorySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Specific type of encounter (e.g. e-mail consultation, surgical day-care,
                # skilled nursing, rehabilitation).
                StructField(
                    "type",
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
                # Broad categorization of the service that is to be provided (e.g. cardiology).
                StructField(
                    "serviceType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the urgency of the encounter.
                StructField(
                    "priority",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The patient or group present at the encounter.
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
                # Where a specific encounter should be classified as a part of a specific
                # episode(s) of care this field should be used. This association can facilitate
                # grouping of related encounters together for a specific purpose, such as
                # government reporting, issue tracking, association via a common problem.  The
                # association is recorded on the encounter as these are typically created after
                # the episode of care and grouped on entry rather than editing the episode of
                # care to append another encounter to it (the episode of care could span years).
                StructField(
                    "episodeOfCare",
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
                # The request this encounter satisfies (e.g. incoming referral or procedure
                # request).
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
                # The list of people responsible for providing the service.
                StructField(
                    "participant",
                    ArrayType(
                        Encounter_ParticipantSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The appointment that scheduled this encounter.
                StructField(
                    "appointment",
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
                # The start and end time of the encounter.
                StructField(
                    "period",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Quantity of time the encounter lasted. This excludes the time during leaves of
                # absence.
                StructField(
                    "length",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Reason the encounter takes place, expressed as a code. For admissions, this
                # can be used for a coded admission diagnosis.
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
                # Reason the encounter takes place, expressed as a code. For admissions, this
                # can be used for a coded admission diagnosis.
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
                # The list of diagnosis relevant to this encounter.
                StructField(
                    "diagnosis",
                    ArrayType(
                        Encounter_DiagnosisSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The set of accounts that may be used for billing for this Encounter.
                StructField(
                    "account",
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
                # Details about the admission to a healthcare service.
                StructField(
                    "hospitalization",
                    Encounter_HospitalizationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # List of locations where  the patient has been during this encounter.
                StructField(
                    "location",
                    ArrayType(
                        Encounter_LocationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The organization that is primarily responsible for this Encounter's services.
                # This MAY be the same as the organization on the Patient record, however it
                # could be different, such as if the actor performing the services was from an
                # external organization (which may be billed seperately) for an external
                # consultation.  Refer to the example bundle showing an abbreviated set of
                # Encounters for a colonoscopy.
                StructField(
                    "serviceProvider",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Another Encounter of which this encounter is a part of (administratively or in
                # time).
                StructField(
                    "partOf",
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
