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
class AutoMapperElasticSearchClinicalImpression(AutoMapperDataTypeComplexBase):
    """
    A record of a clinical assessment performed to determine what problem(s) may
    affect the patient and before planning the treatments or management strategies
    that are best to manage a patient's condition. Assessments are often 1:1 with
    a clinical consultation / encounter,  but this varies greatly depending on the
    clinical workflow. This resource is called "ClinicalImpression" rather than
    "ClinicalAssessment" to avoid confusion with the recording of assessment tools
    such as Apgar score.
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
        code: Optional[Any] = None,
        description: Optional[Any] = None,
        subject: Optional[Any] = None,
        encounter: Optional[Any] = None,
        effectiveDateTime: Optional[Any] = None,
        effectivePeriod: Optional[Any] = None,
        date: Optional[Any] = None,
        assessor: Optional[Any] = None,
        previous: Optional[Any] = None,
        problem: Optional[Any] = None,
        investigation: Optional[Any] = None,
        protocol: Optional[Any] = None,
        summary: Optional[Any] = None,
        finding: Optional[Any] = None,
        prognosisCodeableConcept: Optional[Any] = None,
        prognosisReference: Optional[Any] = None,
        supportingInfo: Optional[Any] = None,
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
            status=status,
            statusReason=statusReason,
            code=code,
            description=description,
            subject=subject,
            encounter=encounter,
            effectiveDateTime=effectiveDateTime,
            effectivePeriod=effectivePeriod,
            date=date,
            assessor=assessor,
            previous=previous,
            problem=problem,
            investigation=investigation,
            protocol=protocol,
            summary=summary,
            finding=finding,
            prognosisCodeableConcept=prognosisCodeableConcept,
            prognosisReference=prognosisReference,
            supportingInfo=supportingInfo,
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
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.clinicalimpression_investigation import (
            AutoMapperElasticSearchClinicalImpression_Investigation as ClinicalImpression_InvestigationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.clinicalimpression_finding import (
            AutoMapperElasticSearchClinicalImpression_Finding as ClinicalImpression_FindingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ClinicalImpression") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ClinicalImpression"]
        schema = StructType(
            [
                # This is a ClinicalImpression resource
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
                # Business identifiers assigned to this clinical impression by the performer or
                # other systems which remain constant as the resource is updated and propagates
                # from server to server.
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
                # Identifies the workflow status of the assessment.
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
                # Captures the reason for the current state of the ClinicalImpression.
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
                # Categorizes the type of clinical assessment performed.
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
                # A summary of the context and/or cause of the assessment - why / where it was
                # performed, and what patient events/status prompted it.
                StructField("description", StringType(), True),
                # The patient or group of individuals assessed as part of this record.
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
                # The Encounter during which this ClinicalImpression was created or to which the
                # creation of this record is tightly associated.
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
                # The point in time or period over which the subject was assessed.
                StructField("effectiveDateTime", TimestampType(), True),
                # The point in time or period over which the subject was assessed.
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
                # Indicates when the documentation of the assessment was complete.
                StructField(
                    "date",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The clinician performing the assessment.
                StructField(
                    "assessor",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to the last assessment that was conducted on this patient.
                # Assessments are often/usually ongoing in nature; a care provider (practitioner
                # or team) will make new assessments on an ongoing basis as new data arises or
                # the patient's conditions changes.
                StructField(
                    "previous",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A list of the relevant problems/conditions for a patient.
                StructField(
                    "problem",
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
                # One or more sets of investigations (signs, symptoms, etc.). The actual
                # grouping of investigations varies greatly depending on the type and context of
                # the assessment. These investigations may include data generated during the
                # assessment process, or data previously generated and recorded that is
                # pertinent to the outcomes.
                StructField(
                    "investigation",
                    ArrayType(
                        ClinicalImpression_InvestigationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Reference to a specific published clinical protocol that was followed during
                # this assessment, and/or that provides evidence in support of the diagnosis.
                StructField(
                    "protocol",
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
                # A text summary of the investigations and the diagnosis.
                StructField("summary", StringType(), True),
                # Specific findings or diagnoses that were considered likely or relevant to
                # ongoing treatment.
                StructField(
                    "finding",
                    ArrayType(
                        ClinicalImpression_FindingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Estimate of likely outcome.
                StructField(
                    "prognosisCodeableConcept",
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
                # RiskAssessment expressing likely outcome.
                StructField(
                    "prognosisReference",
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
                # Information supporting the clinical impression.
                StructField(
                    "supportingInfo",
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
                # Commentary about the impression, typically recorded after the impression
                # itself was made, though supplemental notes by the original author could also
                # appear.
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
