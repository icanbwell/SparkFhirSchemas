from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchResearchStudy(AutoMapperDataTypeComplexBase):
    """
    A process where a researcher or organization plans and then executes a series
    of steps intended to increase the field of healthcare-related knowledge.  This
    includes studies of safety, efficacy, comparative effectiveness and other
    information about medications, devices, therapies and other interventional and
    investigative techniques.  A ResearchStudy involves the gathering of
    information about human or animal subjects.
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
        title: Optional[Any] = None,
        protocol: Optional[Any] = None,
        partOf: Optional[Any] = None,
        status: Optional[Any] = None,
        primaryPurposeType: Optional[Any] = None,
        phase: Optional[Any] = None,
        category: Optional[Any] = None,
        focus: Optional[Any] = None,
        condition: Optional[Any] = None,
        contact: Optional[Any] = None,
        relatedArtifact: Optional[Any] = None,
        keyword: Optional[Any] = None,
        location: Optional[Any] = None,
        description: Optional[Any] = None,
        enrollment: Optional[Any] = None,
        period: Optional[Any] = None,
        sponsor: Optional[Any] = None,
        principalInvestigator: Optional[Any] = None,
        site: Optional[Any] = None,
        reasonStopped: Optional[Any] = None,
        note: Optional[Any] = None,
        arm: Optional[Any] = None,
        objective: Optional[Any] = None,
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
            title=title,
            protocol=protocol,
            partOf=partOf,
            status=status,
            primaryPurposeType=primaryPurposeType,
            phase=phase,
            category=category,
            focus=focus,
            condition=condition,
            contact=contact,
            relatedArtifact=relatedArtifact,
            keyword=keyword,
            location=location,
            description=description,
            enrollment=enrollment,
            period=period,
            sponsor=sponsor,
            principalInvestigator=principalInvestigator,
            site=site,
            reasonStopped=reasonStopped,
            note=note,
            arm=arm,
            objective=objective,
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
        A process where a researcher or organization plans and then executes a series
        of steps intended to increase the field of healthcare-related knowledge.  This
        includes studies of safety, efficacy, comparative effectiveness and other
        information about medications, devices, therapies and other interventional and
        investigative techniques.  A ResearchStudy involves the gathering of
        information about human or animal subjects.


        resourceType: This is a ResearchStudy resource

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

        identifier: Identifiers assigned to this research study by the sponsor or other systems.

        title: A short, descriptive user-friendly label for the study.

        protocol: The set of steps expected to be performed as part of the execution of the
            study.

        partOf: A larger research study of which this particular study is a component or step.

        status: The current state of the study.

        primaryPurposeType: The type of study based upon the intent of the study's activities. A
            classification of the intent of the study.

        phase: The stage in the progression of a therapy from initial experimental use in
            humans in clinical trials to post-market evaluation.

        category: Codes categorizing the type of study such as investigational vs.
            observational, type of blinding, type of randomization, safety vs. efficacy,
            etc.

        focus: The medication(s), food(s), therapy(ies), device(s) or other concerns or
            interventions that the study is seeking to gain more information about.

        condition: The condition that is the focus of the study.  For example, In a study to
            examine risk factors for Lupus, might have as an inclusion criterion "healthy
            volunteer", but the target condition code would be a Lupus SNOMED code.

        contact: Contact details to assist a user in learning more about or engaging with the
            study.

        relatedArtifact: Citations, references and other related documents.

        keyword: Key terms to aid in searching for or filtering the study.

        location: Indicates a country, state or other region where the study is taking place.

        description: A full description of how the study is being conducted.

        enrollment: Reference to a Group that defines the criteria for and quantity of subjects
            participating in the study.  E.g. " 200 female Europeans between the ages of
            20 and 45 with early onset diabetes".

        period: Identifies the start date and the expected (or actual, depending on status)
            end date for the study.

        sponsor: An organization that initiates the investigation and is legally responsible
            for the study.

        principalInvestigator: A researcher in a study who oversees multiple aspects of the study, such as
            concept development, protocol writing, protocol submission for IRB approval,
            participant recruitment, informed consent, data collection, analysis,
            interpretation and presentation.

        site: A facility in which study activities are conducted.

        reasonStopped: A description and/or code explaining the premature termination of the study.

        note: Comments made about the study by the performer, subject or other participants.

        arm: Describes an expected sequence of events for one of the participants of a
            study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
            follow-up.

        objective: A goal that the study is aiming to achieve in terms of a scientific question
            to be answered by the analysis of data collected during the study.

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
        from spark_fhir_schemas.pss_r4.complex_types.contactdetail import (
            AutoMapperElasticSearchContactDetail as ContactDetailSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.relatedartifact import (
            AutoMapperElasticSearchRelatedArtifact as RelatedArtifactSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.researchstudy_arm import (
            AutoMapperElasticSearchResearchStudy_Arm as ResearchStudy_ArmSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.researchstudy_objective import (
            AutoMapperElasticSearchResearchStudy_Objective as ResearchStudy_ObjectiveSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ResearchStudy") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ResearchStudy"]
        schema = StructType(
            [
                # This is a ResearchStudy resource
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
                # Identifiers assigned to this research study by the sponsor or other systems.
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
                # A short, descriptive user-friendly label for the study.
                StructField("title", StringType(), True),
                # The set of steps expected to be performed as part of the execution of the
                # study.
                StructField(
                    "protocol",
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
                # A larger research study of which this particular study is a component or step.
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
                # The current state of the study.
                StructField("status", StringType(), True),
                # The type of study based upon the intent of the study's activities. A
                # classification of the intent of the study.
                StructField(
                    "primaryPurposeType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The stage in the progression of a therapy from initial experimental use in
                # humans in clinical trials to post-market evaluation.
                StructField(
                    "phase",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Codes categorizing the type of study such as investigational vs.
                # observational, type of blinding, type of randomization, safety vs. efficacy,
                # etc.
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
                # The medication(s), food(s), therapy(ies), device(s) or other concerns or
                # interventions that the study is seeking to gain more information about.
                StructField(
                    "focus",
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
                # The condition that is the focus of the study.  For example, In a study to
                # examine risk factors for Lupus, might have as an inclusion criterion "healthy
                # volunteer", but the target condition code would be a Lupus SNOMED code.
                StructField(
                    "condition",
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
                # Contact details to assist a user in learning more about or engaging with the
                # study.
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
                # Citations, references and other related documents.
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
                # Key terms to aid in searching for or filtering the study.
                StructField(
                    "keyword",
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
                # Indicates a country, state or other region where the study is taking place.
                StructField(
                    "location",
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
                # A full description of how the study is being conducted.
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
                # Reference to a Group that defines the criteria for and quantity of subjects
                # participating in the study.  E.g. " 200 female Europeans between the ages of
                # 20 and 45 with early onset diabetes".
                StructField(
                    "enrollment",
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
                # Identifies the start date and the expected (or actual, depending on status)
                # end date for the study.
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
                # An organization that initiates the investigation and is legally responsible
                # for the study.
                StructField(
                    "sponsor",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A researcher in a study who oversees multiple aspects of the study, such as
                # concept development, protocol writing, protocol submission for IRB approval,
                # participant recruitment, informed consent, data collection, analysis,
                # interpretation and presentation.
                StructField(
                    "principalInvestigator",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A facility in which study activities are conducted.
                StructField(
                    "site",
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
                # A description and/or code explaining the premature termination of the study.
                StructField(
                    "reasonStopped",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Comments made about the study by the performer, subject or other participants.
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
                # Describes an expected sequence of events for one of the participants of a
                # study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
                # follow-up.
                StructField(
                    "arm",
                    ArrayType(
                        ResearchStudy_ArmSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A goal that the study is aiming to achieve in terms of a scientific question
                # to be answered by the analysis of data collected during the study.
                StructField(
                    "objective",
                    ArrayType(
                        ResearchStudy_ObjectiveSchema.schema(
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