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
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchMeasure(AutoMapperDataTypeComplexBase):
    """
    The Measure resource provides the definition of a quality measure.
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
        subtitle: Optional[Any] = None,
        status: Optional[Any] = None,
        experimental: Optional[Any] = None,
        subjectCodeableConcept: Optional[Any] = None,
        subjectReference: Optional[Any] = None,
        date: Optional[Any] = None,
        publisher: Optional[Any] = None,
        contact: Optional[Any] = None,
        description: Optional[Any] = None,
        useContext: Optional[Any] = None,
        jurisdiction: Optional[Any] = None,
        purpose: Optional[Any] = None,
        usage: Optional[Any] = None,
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
        library: Optional[Any] = None,
        disclaimer: Optional[Any] = None,
        scoring: Optional[Any] = None,
        compositeScoring: Optional[Any] = None,
        type_: Optional[Any] = None,
        riskAdjustment: Optional[Any] = None,
        rateAggregation: Optional[Any] = None,
        rationale: Optional[Any] = None,
        clinicalRecommendationStatement: Optional[Any] = None,
        improvementNotation: Optional[Any] = None,
        definition: Optional[Any] = None,
        guidance: Optional[Any] = None,
        group: Optional[Any] = None,
        supplementalData: Optional[Any] = None,
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
            subtitle=subtitle,
            status=status,
            experimental=experimental,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            usage=usage,
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
            library=library,
            disclaimer=disclaimer,
            scoring=scoring,
            compositeScoring=compositeScoring,
            type_=type_,
            riskAdjustment=riskAdjustment,
            rateAggregation=rateAggregation,
            rationale=rationale,
            clinicalRecommendationStatement=clinicalRecommendationStatement,
            improvementNotation=improvementNotation,
            definition=definition,
            guidance=guidance,
            group=group,
            supplementalData=supplementalData,
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
        The Measure resource provides the definition of a quality measure.


        resourceType: This is a Measure resource

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

        url: An absolute URI that is used to identify this measure when it is referenced in
            a specification, model, design or an instance; also called its canonical
            identifier. This SHOULD be globally unique and SHOULD be a literal address at
            which at which an authoritative instance of this measure is (or will be)
            published. This URL can be the target of a canonical reference. It SHALL
            remain the same when the measure is stored on different servers.

        identifier: A formal identifier that is used to identify this measure when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the measure when it is
            referenced in a specification, model, design or instance. This is an arbitrary
            value managed by the measure author and is not expected to be globally unique.
            For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
            not available. There is also no expectation that versions can be placed in a
            lexicographical sequence. To provide a version consistent with the Decision
            Support Service specification, use the format Major.Minor.Revision (e.g.
            1.0.0). For more information on versioning knowledge assets, refer to the
            Decision Support Service specification. Note that a version is required for
            non-experimental active artifacts.

        name: A natural language name identifying the measure. This name should be usable as
            an identifier for the module by machine processing applications such as code
            generation.

        title: A short, descriptive, user-friendly title for the measure.

        subtitle: An explanatory or alternate title for the measure giving additional
            information about its content.

        status: The status of this measure. Enables tracking the life-cycle of the content.

        experimental: A Boolean value to indicate that this measure is authored for testing purposes
            (or education/evaluation/marketing) and is not intended to be used for genuine
            usage.

        subjectCodeableConcept: The intended subjects for the measure. If this element is not provided, a
            Patient subject is assumed, but the subject of the measure can be anything.

        subjectReference: The intended subjects for the measure. If this element is not provided, a
            Patient subject is assumed, but the subject of the measure can be anything.

        date: The date  (and optionally time) when the measure was published. The date must
            change when the business version changes and it must change if the status code
            changes. In addition, it should change when the substantive content of the
            measure changes.

        publisher: The name of the organization or individual that published the measure.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the measure from a consumer's
            perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate measure
            instances.

        jurisdiction: A legal or geographic region in which the measure is intended to be used.

        purpose: Explanation of why this measure is needed and why it has been designed as it
            has.

        usage: A detailed description, from a clinical perspective, of how the measure is
            used.

        copyright: A copyright statement relating to the measure and/or its contents. Copyright
            statements are generally legal restrictions on the use and publishing of the
            measure.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval but does not change the original approval date.

        effectivePeriod: The period during which the measure content was or is planned to be in active
            use.

        topic: Descriptive topics related to the content of the measure. Topics provide a
            high-level categorization grouping types of measures that can be useful for
            filtering and searching.

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

        library: A reference to a Library resource containing the formal logic used by the
            measure.

        disclaimer: Notices and disclaimers regarding the use of the measure or related to
            intellectual property (such as code systems) referenced by the measure.

        scoring: Indicates how the calculation is performed for the measure, including
            proportion, ratio, continuous-variable, and cohort. The value set is
            extensible, allowing additional measure scoring types to be represented.

        compositeScoring: If this is a composite measure, the scoring method used to combine the
            component measures to determine the composite score.

        type: Indicates whether the measure is used to examine a process, an outcome over
            time, a patient-reported outcome, or a structure measure such as utilization.

        riskAdjustment: A description of the risk adjustment factors that may impact the resulting
            score for the measure and how they may be accounted for when computing and
            reporting measure results.

        rateAggregation: Describes how to combine the information calculated, based on logic in each of
            several populations, into one summarized result.

        rationale: Provides a succinct statement of the need for the measure. Usually includes
            statements pertaining to importance criterion: impact, gap in care, and
            evidence.

        clinicalRecommendationStatement: Provides a summary of relevant clinical guidelines or other clinical
            recommendations supporting the measure.

        improvementNotation: Information on whether an increase or decrease in score is the preferred
            result (e.g., a higher score indicates better quality OR a lower score
            indicates better quality OR quality is within a range).

        definition: Provides a description of an individual term used within the measure.

        guidance: Additional guidance for the measure including how it can be used in a clinical
            context, and the intent of the measure.

        group: A group of population criteria for the measure.

        supplementalData: The supplemental data criteria for the measure report, specified as either the
            name of a valid CQL expression within a referenced library, or a valid FHIR
            Resource Path.

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
        from spark_fhir_schemas.pss_r4.complex_types.contactdetail import (
            AutoMapperElasticSearchContactDetail as ContactDetailSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.usagecontext import (
            AutoMapperElasticSearchUsageContext as UsageContextSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.relatedartifact import (
            AutoMapperElasticSearchRelatedArtifact as RelatedArtifactSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.measure_group import (
            AutoMapperElasticSearchMeasure_Group as Measure_GroupSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.measure_supplementaldata import (
            AutoMapperElasticSearchMeasure_SupplementalData as Measure_SupplementalDataSchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Measure") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Measure"]
        schema = StructType(
            [
                # This is a Measure resource
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
                # An absolute URI that is used to identify this measure when it is referenced in
                # a specification, model, design or an instance; also called its canonical
                # identifier. This SHOULD be globally unique and SHOULD be a literal address at
                # which at which an authoritative instance of this measure is (or will be)
                # published. This URL can be the target of a canonical reference. It SHALL
                # remain the same when the measure is stored on different servers.
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
                # A formal identifier that is used to identify this measure when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
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
                # The identifier that is used to identify this version of the measure when it is
                # referenced in a specification, model, design or instance. This is an arbitrary
                # value managed by the measure author and is not expected to be globally unique.
                # For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is
                # not available. There is also no expectation that versions can be placed in a
                # lexicographical sequence. To provide a version consistent with the Decision
                # Support Service specification, use the format Major.Minor.Revision (e.g.
                # 1.0.0). For more information on versioning knowledge assets, refer to the
                # Decision Support Service specification. Note that a version is required for
                # non-experimental active artifacts.
                StructField("version", StringType(), True),
                # A natural language name identifying the measure. This name should be usable as
                # an identifier for the module by machine processing applications such as code
                # generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the measure.
                StructField("title", StringType(), True),
                # An explanatory or alternate title for the measure giving additional
                # information about its content.
                StructField("subtitle", StringType(), True),
                # The status of this measure. Enables tracking the life-cycle of the content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this measure is authored for testing purposes
                # (or education/evaluation/marketing) and is not intended to be used for genuine
                # usage.
                StructField("experimental", BooleanType(), True),
                # The intended subjects for the measure. If this element is not provided, a
                # Patient subject is assumed, but the subject of the measure can be anything.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The intended subjects for the measure. If this element is not provided, a
                # Patient subject is assumed, but the subject of the measure can be anything.
                StructField(
                    "subjectReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date  (and optionally time) when the measure was published. The date must
                # change when the business version changes and it must change if the status code
                # changes. In addition, it should change when the substantive content of the
                # measure changes.
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
                # The name of the organization or individual that published the measure.
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
                # A free text natural language description of the measure from a consumer's
                # perspective.
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
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate measure
                # instances.
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
                # A legal or geographic region in which the measure is intended to be used.
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
                # Explanation of why this measure is needed and why it has been designed as it
                # has.
                StructField(
                    "purpose",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A detailed description, from a clinical perspective, of how the measure is
                # used.
                StructField("usage", StringType(), True),
                # A copyright statement relating to the measure and/or its contents. Copyright
                # statements are generally legal restrictions on the use and publishing of the
                # measure.
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
                # The period during which the measure content was or is planned to be in active
                # use.
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
                # Descriptive topics related to the content of the measure. Topics provide a
                # high-level categorization grouping types of measures that can be useful for
                # filtering and searching.
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
                # A reference to a Library resource containing the formal logic used by the
                # measure.
                StructField(
                    "library",
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
                # Notices and disclaimers regarding the use of the measure or related to
                # intellectual property (such as code systems) referenced by the measure.
                StructField(
                    "disclaimer",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates how the calculation is performed for the measure, including
                # proportion, ratio, continuous-variable, and cohort. The value set is
                # extensible, allowing additional measure scoring types to be represented.
                StructField(
                    "scoring",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If this is a composite measure, the scoring method used to combine the
                # component measures to determine the composite score.
                StructField(
                    "compositeScoring",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates whether the measure is used to examine a process, an outcome over
                # time, a patient-reported outcome, or a structure measure such as utilization.
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
                # A description of the risk adjustment factors that may impact the resulting
                # score for the measure and how they may be accounted for when computing and
                # reporting measure results.
                StructField("riskAdjustment", StringType(), True),
                # Describes how to combine the information calculated, based on logic in each of
                # several populations, into one summarized result.
                StructField("rateAggregation", StringType(), True),
                # Provides a succinct statement of the need for the measure. Usually includes
                # statements pertaining to importance criterion: impact, gap in care, and
                # evidence.
                StructField(
                    "rationale",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Provides a summary of relevant clinical guidelines or other clinical
                # recommendations supporting the measure.
                StructField(
                    "clinicalRecommendationStatement",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Information on whether an increase or decrease in score is the preferred
                # result (e.g., a higher score indicates better quality OR a lower score
                # indicates better quality OR quality is within a range).
                StructField(
                    "improvementNotation",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Provides a description of an individual term used within the measure.
                StructField(
                    "definition",
                    ArrayType(
                        markdownSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Additional guidance for the measure including how it can be used in a clinical
                # context, and the intent of the measure.
                StructField(
                    "guidance",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A group of population criteria for the measure.
                StructField(
                    "group",
                    ArrayType(
                        Measure_GroupSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The supplemental data criteria for the measure report, specified as either the
                # name of a valid CQL expression within a referenced library, or a valid FHIR
                # Resource Path.
                StructField(
                    "supplementalData",
                    ArrayType(
                        Measure_SupplementalDataSchema.schema(
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