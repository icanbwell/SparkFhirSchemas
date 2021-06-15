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
    IntegerType,
    DataType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchObservation(AutoMapperDataTypeComplexBase):
    """
    Measurements and simple assertions made about a patient, device or other
    subject.
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
        basedOn: Optional[Any] = None,
        partOf: Optional[Any] = None,
        status: Optional[Any] = None,
        category: Optional[Any] = None,
        code: Optional[Any] = None,
        subject: Optional[Any] = None,
        focus: Optional[Any] = None,
        encounter: Optional[Any] = None,
        effectiveDateTime: Optional[Any] = None,
        effectivePeriod: Optional[Any] = None,
        effectiveTiming: Optional[Any] = None,
        effectiveInstant: Optional[Any] = None,
        issued: Optional[Any] = None,
        performer: Optional[Any] = None,
        valueQuantity: Optional[Any] = None,
        valueCodeableConcept: Optional[Any] = None,
        valueString: Optional[Any] = None,
        valueBoolean: Optional[Any] = None,
        valueInteger: Optional[Any] = None,
        valueRange: Optional[Any] = None,
        valueRatio: Optional[Any] = None,
        valueSampledData: Optional[Any] = None,
        valueTime: Optional[Any] = None,
        valueDateTime: Optional[Any] = None,
        valuePeriod: Optional[Any] = None,
        dataAbsentReason: Optional[Any] = None,
        interpretation: Optional[Any] = None,
        note: Optional[Any] = None,
        bodySite: Optional[Any] = None,
        method: Optional[Any] = None,
        specimen: Optional[Any] = None,
        device: Optional[Any] = None,
        referenceRange: Optional[Any] = None,
        hasMember: Optional[Any] = None,
        derivedFrom: Optional[Any] = None,
        component: Optional[Any] = None,
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
            basedOn=basedOn,
            partOf=partOf,
            status=status,
            category=category,
            code=code,
            subject=subject,
            focus=focus,
            encounter=encounter,
            effectiveDateTime=effectiveDateTime,
            effectivePeriod=effectivePeriod,
            effectiveTiming=effectiveTiming,
            effectiveInstant=effectiveInstant,
            issued=issued,
            performer=performer,
            valueQuantity=valueQuantity,
            valueCodeableConcept=valueCodeableConcept,
            valueString=valueString,
            valueBoolean=valueBoolean,
            valueInteger=valueInteger,
            valueRange=valueRange,
            valueRatio=valueRatio,
            valueSampledData=valueSampledData,
            valueTime=valueTime,
            valueDateTime=valueDateTime,
            valuePeriod=valuePeriod,
            dataAbsentReason=dataAbsentReason,
            interpretation=interpretation,
            note=note,
            bodySite=bodySite,
            method=method,
            specimen=specimen,
            device=device,
            referenceRange=referenceRange,
            hasMember=hasMember,
            derivedFrom=derivedFrom,
            component=component,
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
        Measurements and simple assertions made about a patient, device or other
        subject.


        resourceType: This is a Observation resource

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

        identifier: A unique identifier assigned to this observation.

        basedOn: A plan, proposal or order that is fulfilled in whole or in part by this event.
            For example, a MedicationRequest may require a patient to have laboratory test
            performed before  it is dispensed.

        partOf: A larger event of which this particular Observation is a component or step.
            For example,  an observation as part of a procedure.

        status: The status of the result value.

        category: A code that classifies the general type of observation being made.

        code: Describes what was observed. Sometimes this is called the observation "name".

        subject: The patient, or group of patients, location, or device this observation is
            about and into whose record the observation is placed. If the actual focus of
            the observation is different from the subject (or a sample of, part, or region
            of the subject), the `focus` element or the `code` itself specifies the actual
            focus of the observation.

        focus: The actual focus of an observation when it is not the patient of record
            representing something or someone associated with the patient such as a
            spouse, parent, fetus, or donor. For example, fetus observations in a mother's
            record.  The focus of an observation could also be an existing condition,  an
            intervention, the subject's diet,  another observation of the subject,  or a
            body structure such as tumor or implanted device.   An example use case would
            be using the Observation resource to capture whether the mother is trained to
            change her child's tracheostomy tube. In this example, the child is the
            patient of record and the mother is the focus.

        encounter: The healthcare event  (e.g. a patient and healthcare provider interaction)
            during which this observation is made.

        effectiveDateTime: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        effectivePeriod: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        effectiveTiming: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        effectiveInstant: The time or time-period the observed value is asserted as being true. For
            biological subjects - e.g. human patients - this is usually called the
            "physiologically relevant time". This is usually either the time of the
            procedure or of specimen collection, but very often the source of the
            date/time is not known, only the date/time itself.

        issued: The date and time this version of the observation was made available to
            providers, typically after the results have been reviewed and verified.

        performer: Who was responsible for asserting the observed value as "true".

        valueQuantity: The information determined as a result of making the observation, if the
            information has a simple value.

        valueCodeableConcept: The information determined as a result of making the observation, if the
            information has a simple value.

        valueString: The information determined as a result of making the observation, if the
            information has a simple value.

        valueBoolean: The information determined as a result of making the observation, if the
            information has a simple value.

        valueInteger: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRange: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRatio: The information determined as a result of making the observation, if the
            information has a simple value.

        valueSampledData: The information determined as a result of making the observation, if the
            information has a simple value.

        valueTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valueDateTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valuePeriod: The information determined as a result of making the observation, if the
            information has a simple value.

        dataAbsentReason: Provides a reason why the expected value in the element Observation.value[x]
            is missing.

        interpretation: A categorical assessment of an observation value.  For example, high, low,
            normal.

        note: Comments about the observation or the results.

        bodySite: Indicates the site on the subject's body where the observation was made (i.e.
            the target site).

        method: Indicates the mechanism used to perform the observation.

        specimen: The specimen that was used when this observation was made.

        device: The device used to generate the observation data.

        referenceRange: Guidance on how to interpret the value by comparison to a normal or
            recommended range.  Multiple reference ranges are interpreted as an "OR".   In
            other words, to represent two distinct target populations, two
            `referenceRange` elements would be used.

        hasMember: This observation is a group observation (e.g. a battery, a panel of tests, a
            set of vital sign measurements) that includes the target as a member of the
            group.

        derivedFrom: The target resource that represents a measurement from which this observation
            value is derived. For example, a calculated anion gap or a fetal measurement
            based on an ultrasound image.

        component: Some observations have multiple component observations.  These component
            observations are expressed as separate code value pairs that share the same
            attributes.  Examples include systolic and diastolic component observations
            for blood pressure measurement and multiple component observations for
            genetics observations.

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
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.instant import (
            AutoMapperElasticSearchinstant as instantSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.sampleddata import (
            AutoMapperElasticSearchSampledData as SampledDataSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.observation_referencerange import (
            AutoMapperElasticSearchObservation_ReferenceRange as Observation_ReferenceRangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.observation_component import (
            AutoMapperElasticSearchObservation_Component as Observation_ComponentSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Observation") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Observation"]
        schema = StructType(
            [
                # This is a Observation resource
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
                # A unique identifier assigned to this observation.
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
                # A plan, proposal or order that is fulfilled in whole or in part by this event.
                # For example, a MedicationRequest may require a patient to have laboratory test
                # performed before  it is dispensed.
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
                # A larger event of which this particular Observation is a component or step.
                # For example,  an observation as part of a procedure.
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
                # The status of the result value.
                StructField("status", StringType(), True),
                # A code that classifies the general type of observation being made.
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
                # Describes what was observed. Sometimes this is called the observation "name".
                StructField(
                    "code",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The patient, or group of patients, location, or device this observation is
                # about and into whose record the observation is placed. If the actual focus of
                # the observation is different from the subject (or a sample of, part, or region
                # of the subject), the `focus` element or the `code` itself specifies the actual
                # focus of the observation.
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
                # The actual focus of an observation when it is not the patient of record
                # representing something or someone associated with the patient such as a
                # spouse, parent, fetus, or donor. For example, fetus observations in a mother's
                # record.  The focus of an observation could also be an existing condition,  an
                # intervention, the subject's diet,  another observation of the subject,  or a
                # body structure such as tumor or implanted device.   An example use case would
                # be using the Observation resource to capture whether the mother is trained to
                # change her child's tracheostomy tube. In this example, the child is the
                # patient of record and the mother is the focus.
                StructField(
                    "focus",
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
                # The healthcare event  (e.g. a patient and healthcare provider interaction)
                # during which this observation is made.
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
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField("effectiveDateTime", TimestampType(), True),
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField(
                    "effectivePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField(
                    "effectiveTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The time or time-period the observed value is asserted as being true. For
                # biological subjects - e.g. human patients - this is usually called the
                # "physiologically relevant time". This is usually either the time of the
                # procedure or of specimen collection, but very often the source of the
                # date/time is not known, only the date/time itself.
                StructField("effectiveInstant", StringType(), True),
                # The date and time this version of the observation was made available to
                # providers, typically after the results have been reviewed and verified.
                StructField(
                    "issued",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Who was responsible for asserting the observed value as "true".
                StructField(
                    "performer",
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
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueString", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueBoolean", BooleanType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueInteger", IntegerType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueSampledData",
                    SampledDataSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueTime", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueDateTime", TimestampType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valuePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Provides a reason why the expected value in the element Observation.value[x]
                # is missing.
                StructField(
                    "dataAbsentReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A categorical assessment of an observation value.  For example, high, low,
                # normal.
                StructField(
                    "interpretation",
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
                # Comments about the observation or the results.
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
                # Indicates the site on the subject's body where the observation was made (i.e.
                # the target site).
                StructField(
                    "bodySite",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the mechanism used to perform the observation.
                StructField(
                    "method",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The specimen that was used when this observation was made.
                StructField(
                    "specimen",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The device used to generate the observation data.
                StructField(
                    "device",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Guidance on how to interpret the value by comparison to a normal or
                # recommended range.  Multiple reference ranges are interpreted as an "OR".   In
                # other words, to represent two distinct target populations, two
                # `referenceRange` elements would be used.
                StructField(
                    "referenceRange",
                    ArrayType(
                        Observation_ReferenceRangeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # This observation is a group observation (e.g. a battery, a panel of tests, a
                # set of vital sign measurements) that includes the target as a member of the
                # group.
                StructField(
                    "hasMember",
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
                # The target resource that represents a measurement from which this observation
                # value is derived. For example, a calculated anion gap or a fetal measurement
                # based on an ultrasound image.
                StructField(
                    "derivedFrom",
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
                # Some observations have multiple component observations.  These component
                # observations are expressed as separate code value pairs that share the same
                # attributes.  Examples include systolic and diastolic component observations
                # for blood pressure measurement and multiple component observations for
                # genetics observations.
                StructField(
                    "component",
                    ArrayType(
                        Observation_ComponentSchema.schema(
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
