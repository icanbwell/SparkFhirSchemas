from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchEffectEvidenceSynthesis(AutoMapperDataTypeComplexBase):
    """
    The EffectEvidenceSynthesis resource describes the difference in an outcome
    between exposures states in a population where the effect estimate is derived
    from a combination of research studies.
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
        url: Optional[Any] = None,
        identifier: Optional[Any] = None,
        version: Optional[Any] = None,
        name: Optional[Any] = None,
        title: Optional[Any] = None,
        status: Optional[Any] = None,
        date: Optional[Any] = None,
        publisher: Optional[Any] = None,
        contact: Optional[Any] = None,
        description: Optional[Any] = None,
        note: Optional[Any] = None,
        useContext: Optional[Any] = None,
        jurisdiction: Optional[Any] = None,
        copyright_: Optional[Any] = None,
        approvalDate: Optional[Any] = None,
        lastReviewDate: Optional[Any] = None,
        effectivePeriod: Optional[Any] = None,
        topic: Optional[Any] = None,
        author: Optional[Any] = None,
        editor: Optional[Any] = None,
        reviewer: Optional[Any] = None,
        endorser: Optional[Any] = None,
        relatedArtifact: Optional[Any] = None,
        synthesisType: Optional[Any] = None,
        studyType: Optional[Any] = None,
        population: Optional[Any] = None,
        exposure: Optional[Any] = None,
        exposureAlternative: Optional[Any] = None,
        outcome: Optional[Any] = None,
        sampleSize: Optional[Any] = None,
        resultsByExposure: Optional[Any] = None,
        effectEstimate: Optional[Any] = None,
        certainty: Optional[Any] = None,
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
            url=url,
            identifier=identifier,
            version=version,
            name=name,
            title=title,
            status=status,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            note=note,
            useContext=useContext,
            jurisdiction=jurisdiction,
            copyright_=copyright_,
            approvalDate=approvalDate,
            lastReviewDate=lastReviewDate,
            effectivePeriod=effectivePeriod,
            topic=topic,
            author=author,
            editor=editor,
            reviewer=reviewer,
            endorser=endorser,
            relatedArtifact=relatedArtifact,
            synthesisType=synthesisType,
            studyType=studyType,
            population=population,
            exposure=exposure,
            exposureAlternative=exposureAlternative,
            outcome=outcome,
            sampleSize=sampleSize,
            resultsByExposure=resultsByExposure,
            effectEstimate=effectEstimate,
            certainty=certainty,
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
        The EffectEvidenceSynthesis resource describes the difference in an outcome
        between exposures states in a population where the effect estimate is derived
        from a combination of research studies.


        resourceType: This is a EffectEvidenceSynthesis resource

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

        url: An absolute URI that is used to identify this effect evidence synthesis when
            it is referenced in a specification, model, design or an instance; also called
            its canonical identifier. This SHOULD be globally unique and SHOULD be a
            literal address at which at which an authoritative instance of this effect
            evidence synthesis is (or will be) published. This URL can be the target of a
            canonical reference. It SHALL remain the same when the effect evidence
            synthesis is stored on different servers.

        identifier: A formal identifier that is used to identify this effect evidence synthesis
            when it is represented in other formats, or referenced in a specification,
            model, design or an instance.

        version: The identifier that is used to identify this version of the effect evidence
            synthesis when it is referenced in a specification, model, design or instance.
            This is an arbitrary value managed by the effect evidence synthesis author and
            is not expected to be globally unique. For example, it might be a timestamp
            (e.g. yyyymmdd) if a managed version is not available. There is also no
            expectation that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the effect evidence synthesis. This name
            should be usable as an identifier for the module by machine processing
            applications such as code generation.

        title: A short, descriptive, user-friendly title for the effect evidence synthesis.

        status: The status of this effect evidence synthesis. Enables tracking the life-cycle
            of the content.

        date: The date  (and optionally time) when the effect evidence synthesis was
            published. The date must change when the business version changes and it must
            change if the status code changes. In addition, it should change when the
            substantive content of the effect evidence synthesis changes.

        publisher: The name of the organization or individual that published the effect evidence
            synthesis.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the effect evidence synthesis from
            a consumer's perspective.

        note: A human-readable string to clarify or explain concepts about the resource.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate effect
            evidence synthesis instances.

        jurisdiction: A legal or geographic region in which the effect evidence synthesis is
            intended to be used.

        copyright: A copyright statement relating to the effect evidence synthesis and/or its
            contents. Copyright statements are generally legal restrictions on the use and
            publishing of the effect evidence synthesis.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval but does not change the original approval date.

        effectivePeriod: The period during which the effect evidence synthesis content was or is
            planned to be in active use.

        topic: Descriptive topics related to the content of the EffectEvidenceSynthesis.
            Topics provide a high-level categorization grouping types of
            EffectEvidenceSynthesiss that can be useful for filtering and searching.

        author: An individiual or organization primarily involved in the creation and
            maintenance of the content.

        editor: An individual or organization primarily responsible for internal coherence of
            the content.

        reviewer: An individual or organization primarily responsible for review of some aspect
            of the content.

        endorser: An individual or organization responsible for officially endorsing the content
            for use in some setting.

        relatedArtifact: Related artifacts such as additional documentation, justification, or
            bibliographic references.

        synthesisType: Type of synthesis eg meta-analysis.

        studyType: Type of study eg randomized trial.

        population: A reference to a EvidenceVariable resource that defines the population for the
            research.

        exposure: A reference to a EvidenceVariable resource that defines the exposure for the
            research.

        exposureAlternative: A reference to a EvidenceVariable resource that defines the comparison
            exposure for the research.

        outcome: A reference to a EvidenceVariable resomece that defines the outcome for the
            research.

        sampleSize: A description of the size of the sample involved in the synthesis.

        resultsByExposure: A description of the results for each exposure considered in the effect
            estimate.

        effectEstimate: The estimated effect of the exposure variant.

        certainty: A description of the certainty of the effect estimate.

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
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactdetail import (
            AutoMapperElasticSearchContactDetail as ContactDetailSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.usagecontext import (
            AutoMapperElasticSearchUsageContext as UsageContextSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.relatedartifact import (
            AutoMapperElasticSearchRelatedArtifact as RelatedArtifactSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.effectevidencesynthesis_samplesize import (
            AutoMapperElasticSearchEffectEvidenceSynthesis_SampleSize as EffectEvidenceSynthesis_SampleSizeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.effectevidencesynthesis_resultsbyexposure import (
            AutoMapperElasticSearchEffectEvidenceSynthesis_ResultsByExposure as EffectEvidenceSynthesis_ResultsByExposureSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.effectevidencesynthesis_effectestimate import (
            AutoMapperElasticSearchEffectEvidenceSynthesis_EffectEstimate as EffectEvidenceSynthesis_EffectEstimateSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.effectevidencesynthesis_certainty import (
            AutoMapperElasticSearchEffectEvidenceSynthesis_Certainty as EffectEvidenceSynthesis_CertaintySchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("EffectEvidenceSynthesis") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["EffectEvidenceSynthesis"]
        schema = StructType(
            [
                # This is a EffectEvidenceSynthesis resource
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
                # An absolute URI that is used to identify this effect evidence synthesis when
                # it is referenced in a specification, model, design or an instance; also called
                # its canonical identifier. This SHOULD be globally unique and SHOULD be a
                # literal address at which at which an authoritative instance of this effect
                # evidence synthesis is (or will be) published. This URL can be the target of a
                # canonical reference. It SHALL remain the same when the effect evidence
                # synthesis is stored on different servers.
                StructField(
                    "url",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A formal identifier that is used to identify this effect evidence synthesis
                # when it is represented in other formats, or referenced in a specification,
                # model, design or an instance.
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
                # The identifier that is used to identify this version of the effect evidence
                # synthesis when it is referenced in a specification, model, design or instance.
                # This is an arbitrary value managed by the effect evidence synthesis author and
                # is not expected to be globally unique. For example, it might be a timestamp
                # (e.g. yyyymmdd) if a managed version is not available. There is also no
                # expectation that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the effect evidence synthesis. This name
                # should be usable as an identifier for the module by machine processing
                # applications such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the effect evidence synthesis.
                StructField("title", StringType(), True),
                # The status of this effect evidence synthesis. Enables tracking the life-cycle
                # of the content.
                StructField("status", StringType(), True),
                # The date  (and optionally time) when the effect evidence synthesis was
                # published. The date must change when the business version changes and it must
                # change if the status code changes. In addition, it should change when the
                # substantive content of the effect evidence synthesis changes.
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
                # The name of the organization or individual that published the effect evidence
                # synthesis.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(
                        ContactDetailSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A free text natural language description of the effect evidence synthesis from
                # a consumer's perspective.
                StructField(
                    "description",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A human-readable string to clarify or explain concepts about the resource.
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
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate effect
                # evidence synthesis instances.
                StructField(
                    "useContext",
                    ArrayType(
                        UsageContextSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A legal or geographic region in which the effect evidence synthesis is
                # intended to be used.
                StructField(
                    "jurisdiction",
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
                # A copyright statement relating to the effect evidence synthesis and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the effect evidence synthesis.
                StructField(
                    "copyright",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date on which the resource content was approved by the publisher. Approval
                # happens once when the content is officially approved for usage.
                StructField("approvalDate", DateType(), True),
                # The date on which the resource content was last reviewed. Review happens
                # periodically after approval but does not change the original approval date.
                StructField("lastReviewDate", DateType(), True),
                # The period during which the effect evidence synthesis content was or is
                # planned to be in active use.
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
                # Descriptive topics related to the content of the EffectEvidenceSynthesis.
                # Topics provide a high-level categorization grouping types of
                # EffectEvidenceSynthesiss that can be useful for filtering and searching.
                StructField(
                    "topic",
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
                # An individiual or organization primarily involved in the creation and
                # maintenance of the content.
                StructField(
                    "author",
                    ArrayType(
                        ContactDetailSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An individual or organization primarily responsible for internal coherence of
                # the content.
                StructField(
                    "editor",
                    ArrayType(
                        ContactDetailSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An individual or organization primarily responsible for review of some aspect
                # of the content.
                StructField(
                    "reviewer",
                    ArrayType(
                        ContactDetailSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An individual or organization responsible for officially endorsing the content
                # for use in some setting.
                StructField(
                    "endorser",
                    ArrayType(
                        ContactDetailSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Related artifacts such as additional documentation, justification, or
                # bibliographic references.
                StructField(
                    "relatedArtifact",
                    ArrayType(
                        RelatedArtifactSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Type of synthesis eg meta-analysis.
                StructField(
                    "synthesisType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Type of study eg randomized trial.
                StructField(
                    "studyType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a EvidenceVariable resource that defines the population for the
                # research.
                StructField(
                    "population",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a EvidenceVariable resource that defines the exposure for the
                # research.
                StructField(
                    "exposure",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a EvidenceVariable resource that defines the comparison
                # exposure for the research.
                StructField(
                    "exposureAlternative",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a EvidenceVariable resomece that defines the outcome for the
                # research.
                StructField(
                    "outcome",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A description of the size of the sample involved in the synthesis.
                StructField(
                    "sampleSize",
                    EffectEvidenceSynthesis_SampleSizeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A description of the results for each exposure considered in the effect
                # estimate.
                StructField(
                    "resultsByExposure",
                    ArrayType(
                        EffectEvidenceSynthesis_ResultsByExposureSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The estimated effect of the exposure variant.
                StructField(
                    "effectEstimate",
                    ArrayType(
                        EffectEvidenceSynthesis_EffectEstimateSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A description of the certainty of the effect estimate.
                StructField(
                    "certainty",
                    ArrayType(
                        EffectEvidenceSynthesis_CertaintySchema.schema(
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