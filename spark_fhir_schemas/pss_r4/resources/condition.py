from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DataType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchCondition(AutoMapperDataTypeComplexBase):
    """
    A clinical condition, problem, diagnosis, or other event, situation, issue, or
    clinical concept that has risen to a level of concern.
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
        clinicalStatus: Optional[Any] = None,
        verificationStatus: Optional[Any] = None,
        category: Optional[Any] = None,
        severity: Optional[Any] = None,
        code: Optional[Any] = None,
        bodySite: Optional[Any] = None,
        subject: Optional[Any] = None,
        encounter: Optional[Any] = None,
        onsetDateTime: Optional[Any] = None,
        onsetAge: Optional[Any] = None,
        onsetPeriod: Optional[Any] = None,
        onsetRange: Optional[Any] = None,
        onsetString: Optional[Any] = None,
        abatementDateTime: Optional[Any] = None,
        abatementAge: Optional[Any] = None,
        abatementPeriod: Optional[Any] = None,
        abatementRange: Optional[Any] = None,
        abatementString: Optional[Any] = None,
        recordedDate: Optional[Any] = None,
        recorder: Optional[Any] = None,
        asserter: Optional[Any] = None,
        stage: Optional[Any] = None,
        evidence: Optional[Any] = None,
        note: Optional[Any] = None,
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
            clinicalStatus=clinicalStatus,
            verificationStatus=verificationStatus,
            category=category,
            severity=severity,
            code=code,
            bodySite=bodySite,
            subject=subject,
            encounter=encounter,
            onsetDateTime=onsetDateTime,
            onsetAge=onsetAge,
            onsetPeriod=onsetPeriod,
            onsetRange=onsetRange,
            onsetString=onsetString,
            abatementDateTime=abatementDateTime,
            abatementAge=abatementAge,
            abatementPeriod=abatementPeriod,
            abatementRange=abatementRange,
            abatementString=abatementString,
            recordedDate=recordedDate,
            recorder=recorder,
            asserter=asserter,
            stage=stage,
            evidence=evidence,
            note=note,
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
        A clinical condition, problem, diagnosis, or other event, situation, issue, or
        clinical concept that has risen to a level of concern.


        resourceType: This is a Condition resource

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

        identifier: Business identifiers assigned to this condition by the performer or other
            systems which remain constant as the resource is updated and propagates from
            server to server.

        clinicalStatus: The clinical status of the condition.

        verificationStatus: The verification status to support the clinical status of the condition.

        category: A category assigned to the condition.

        severity: A subjective assessment of the severity of the condition as evaluated by the
            clinician.

        code: Identification of the condition, problem or diagnosis.

        bodySite: The anatomical location where this condition manifests itself.

        subject: Indicates the patient or group who the condition record is associated with.

        encounter: The Encounter during which this Condition was created or to which the creation
            of this record is tightly associated.

        onsetDateTime: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetAge: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetPeriod: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetRange: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        onsetString: Estimated or actual date or date-time  the condition began, in the opinion of
            the clinician.

        abatementDateTime: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementAge: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementPeriod: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementRange: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        abatementString: The date or estimated date that the condition resolved or went into remission.
            This is called "abatement" because of the many overloaded connotations
            associated with "remission" or "resolution" - Conditions are never really
            resolved, but they can abate.

        recordedDate: The recordedDate represents when this particular Condition record was created
            in the system, which is often a system-generated date.

        recorder: Individual who recorded the record and takes responsibility for its content.

        asserter: Individual who is making the condition statement.

        stage: Clinical stage or grade of a condition. May include formal severity
            assessments.

        evidence: Supporting evidence / manifestations that are the basis of the Condition's
            verification status, such as evidence that confirmed or refuted the condition.

        note: Additional information about the Condition. This is a general notes/comments
            entry  for description of the Condition, its diagnosis and prognosis.

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
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.condition_stage import (
            AutoMapperElasticSearchCondition_Stage as Condition_StageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.condition_evidence import (
            AutoMapperElasticSearchCondition_Evidence as Condition_EvidenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Condition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Condition"]
        schema = StructType(
            [
                # This is a Condition resource
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
                # Business identifiers assigned to this condition by the performer or other
                # systems which remain constant as the resource is updated and propagates from
                # server to server.
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
                # The clinical status of the condition.
                StructField(
                    "clinicalStatus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The verification status to support the clinical status of the condition.
                StructField(
                    "verificationStatus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A category assigned to the condition.
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
                # A subjective assessment of the severity of the condition as evaluated by the
                # clinician.
                StructField(
                    "severity",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identification of the condition, problem or diagnosis.
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
                # The anatomical location where this condition manifests itself.
                StructField(
                    "bodySite",
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
                # Indicates the patient or group who the condition record is associated with.
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
                # The Encounter during which this Condition was created or to which the creation
                # of this record is tightly associated.
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
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField("onsetDateTime", TimestampType(), True),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField(
                    "onsetRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date or date-time  the condition began, in the opinion of
                # the clinician.
                StructField("onsetString", StringType(), True),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField("abatementDateTime", TimestampType(), True),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField(
                    "abatementRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date or estimated date that the condition resolved or went into remission.
                # This is called "abatement" because of the many overloaded connotations
                # associated with "remission" or "resolution" - Conditions are never really
                # resolved, but they can abate.
                StructField("abatementString", StringType(), True),
                # The recordedDate represents when this particular Condition record was created
                # in the system, which is often a system-generated date.
                StructField(
                    "recordedDate",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Individual who recorded the record and takes responsibility for its content.
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
                # Individual who is making the condition statement.
                StructField(
                    "asserter",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Clinical stage or grade of a condition. May include formal severity
                # assessments.
                StructField(
                    "stage",
                    ArrayType(
                        Condition_StageSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Supporting evidence / manifestations that are the basis of the Condition's
                # verification status, such as evidence that confirmed or refuted the condition.
                StructField(
                    "evidence",
                    ArrayType(
                        Condition_EvidenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Additional information about the Condition. This is a general notes/comments
                # entry  for description of the Condition, its diagnosis and prognosis.
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
