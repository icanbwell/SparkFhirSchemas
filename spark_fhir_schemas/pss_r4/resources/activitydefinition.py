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
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchActivityDefinition(AutoMapperDataTypeComplexBase):
    """
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
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
        kind: Optional[Any] = None,
        profile: Optional[Any] = None,
        code: Optional[Any] = None,
        intent: Optional[Any] = None,
        priority: Optional[Any] = None,
        doNotPerform: Optional[Any] = None,
        timingTiming: Optional[Any] = None,
        timingDateTime: Optional[Any] = None,
        timingAge: Optional[Any] = None,
        timingPeriod: Optional[Any] = None,
        timingRange: Optional[Any] = None,
        timingDuration: Optional[Any] = None,
        location: Optional[Any] = None,
        participant: Optional[Any] = None,
        productReference: Optional[Any] = None,
        productCodeableConcept: Optional[Any] = None,
        quantity: Optional[Any] = None,
        dosage: Optional[Any] = None,
        bodySite: Optional[Any] = None,
        specimenRequirement: Optional[Any] = None,
        observationRequirement: Optional[Any] = None,
        observationResultRequirement: Optional[Any] = None,
        transform: Optional[Any] = None,
        dynamicValue: Optional[Any] = None,
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
            kind=kind,
            profile=profile,
            code=code,
            intent=intent,
            priority=priority,
            doNotPerform=doNotPerform,
            timingTiming=timingTiming,
            timingDateTime=timingDateTime,
            timingAge=timingAge,
            timingPeriod=timingPeriod,
            timingRange=timingRange,
            timingDuration=timingDuration,
            location=location,
            participant=participant,
            productReference=productReference,
            productCodeableConcept=productCodeableConcept,
            quantity=quantity,
            dosage=dosage,
            bodySite=bodySite,
            specimenRequirement=specimenRequirement,
            observationRequirement=observationRequirement,
            observationResultRequirement=observationResultRequirement,
            transform=transform,
            dynamicValue=dynamicValue,
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
        This resource allows for the definition of some activity to be performed,
        independent of a particular patient, practitioner, or other performance
        context.


        resourceType: This is a ActivityDefinition resource

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

        url: An absolute URI that is used to identify this activity definition when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this activity
            definition is (or will be) published. This URL can be the target of a
            canonical reference. It SHALL remain the same when the activity definition is
            stored on different servers.

        identifier: A formal identifier that is used to identify this activity definition when it
            is represented in other formats, or referenced in a specification, model,
            design or an instance.

        version: The identifier that is used to identify this version of the activity
            definition when it is referenced in a specification, model, design or
            instance. This is an arbitrary value managed by the activity definition author
            and is not expected to be globally unique. For example, it might be a
            timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
            no expectation that versions can be placed in a lexicographical sequence. To
            provide a version consistent with the Decision Support Service specification,
            use the format Major.Minor.Revision (e.g. 1.0.0). For more information on
            versioning knowledge assets, refer to the Decision Support Service
            specification. Note that a version is required for non-experimental active
            assets.

        name: A natural language name identifying the activity definition. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the activity definition.

        subtitle: An explanatory or alternate title for the activity definition giving
            additional information about its content.

        status: The status of this activity definition. Enables tracking the life-cycle of the
            content.

        experimental: A Boolean value to indicate that this activity definition is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        subjectCodeableConcept: A code or group definition that describes the intended subject of the activity
            being defined.

        subjectReference: A code or group definition that describes the intended subject of the activity
            being defined.

        date: The date  (and optionally time) when the activity definition was published.
            The date must change when the business version changes and it must change if
            the status code changes. In addition, it should change when the substantive
            content of the activity definition changes.

        publisher: The name of the organization or individual that published the activity
            definition.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the activity definition from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate activity
            definition instances.

        jurisdiction: A legal or geographic region in which the activity definition is intended to
            be used.

        purpose: Explanation of why this activity definition is needed and why it has been
            designed as it has.

        usage: A detailed description of how the activity definition is used from a clinical
            perspective.

        copyright: A copyright statement relating to the activity definition and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the activity definition.

        approvalDate: The date on which the resource content was approved by the publisher. Approval
            happens once when the content is officially approved for usage.

        lastReviewDate: The date on which the resource content was last reviewed. Review happens
            periodically after approval but does not change the original approval date.

        effectivePeriod: The period during which the activity definition content was or is planned to
            be in active use.

        topic: Descriptive topics related to the content of the activity. Topics provide a
            high-level categorization of the activity that can be useful for filtering and
            searching.

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

        library: A reference to a Library resource containing any formal logic used by the
            activity definition.

        kind: A description of the kind of resource the activity definition is representing.
            For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequest.
            Typically, but not always, this is a Request resource.

        profile: A profile to which the target of the activity definition is expected to
            conform.

        code: Detailed description of the type of activity; e.g. What lab test, what
            procedure, what kind of encounter.

        intent: Indicates the level of authority/intentionality associated with the activity
            and where the request should fit into the workflow chain.

        priority: Indicates how quickly the activity  should be addressed with respect to other
            requests.

        doNotPerform: Set this to true if the definition is to indicate that a particular activity
            should NOT be performed. If true, this element should be interpreted to
            reinforce a negative coding. For example NPO as a code with a doNotPerform of
            true would still indicate to NOT perform the action.

        timingTiming: The period, timing or frequency upon which the described activity is to occur.

        timingDateTime: The period, timing or frequency upon which the described activity is to occur.

        timingAge: The period, timing or frequency upon which the described activity is to occur.

        timingPeriod: The period, timing or frequency upon which the described activity is to occur.

        timingRange: The period, timing or frequency upon which the described activity is to occur.

        timingDuration: The period, timing or frequency upon which the described activity is to occur.

        location: Identifies the facility where the activity will occur; e.g. home, hospital,
            specific clinic, etc.

        participant: Indicates who should participate in performing the action described.

        productReference: Identifies the food, drug or other product being consumed or supplied in the
            activity.

        productCodeableConcept: Identifies the food, drug or other product being consumed or supplied in the
            activity.

        quantity: Identifies the quantity expected to be consumed at once (per dose, per meal,
            etc.).

        dosage: Provides detailed dosage instructions in the same way that they are described
            for MedicationRequest resources.

        bodySite: Indicates the sites on the subject's body where the procedure should be
            performed (I.e. the target sites).

        specimenRequirement: Defines specimen requirements for the action to be performed, such as required
            specimens for a lab test.

        observationRequirement: Defines observation requirements for the action to be performed, such as body
            weight or surface area.

        observationResultRequirement: Defines the observations that are expected to be produced by the action.

        transform: A reference to a StructureMap resource that defines a transform that can be
            executed to produce the intent resource using the ActivityDefinition instance
            as the input.

        dynamicValue: Dynamic values that will be evaluated to produce values for elements of the
            resulting resource. For example, if the dosage of a medication must be
            computed based on the patient's weight, a dynamic value would be used to
            specify an expression that calculated the weight, and the path on the request
            resource that would contain the result.

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
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.activitydefinition_participant import (
            AutoMapperElasticSearchActivityDefinition_Participant as ActivityDefinition_ParticipantSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.dosage import (
            AutoMapperElasticSearchDosage as DosageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.activitydefinition_dynamicvalue import (
            AutoMapperElasticSearchActivityDefinition_DynamicValue as ActivityDefinition_DynamicValueSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ActivityDefinition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ActivityDefinition"]
        schema = StructType(
            [
                # This is a ActivityDefinition resource
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
                # An absolute URI that is used to identify this activity definition when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this activity
                # definition is (or will be) published. This URL can be the target of a
                # canonical reference. It SHALL remain the same when the activity definition is
                # stored on different servers.
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
                # A formal identifier that is used to identify this activity definition when it
                # is represented in other formats, or referenced in a specification, model,
                # design or an instance.
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
                # The identifier that is used to identify this version of the activity
                # definition when it is referenced in a specification, model, design or
                # instance. This is an arbitrary value managed by the activity definition author
                # and is not expected to be globally unique. For example, it might be a
                # timestamp (e.g. yyyymmdd) if a managed version is not available. There is also
                # no expectation that versions can be placed in a lexicographical sequence. To
                # provide a version consistent with the Decision Support Service specification,
                # use the format Major.Minor.Revision (e.g. 1.0.0). For more information on
                # versioning knowledge assets, refer to the Decision Support Service
                # specification. Note that a version is required for non-experimental active
                # assets.
                StructField("version", StringType(), True),
                # A natural language name identifying the activity definition. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the activity definition.
                StructField("title", StringType(), True),
                # An explanatory or alternate title for the activity definition giving
                # additional information about its content.
                StructField("subtitle", StringType(), True),
                # The status of this activity definition. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this activity definition is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # A code or group definition that describes the intended subject of the activity
                # being defined.
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
                # A code or group definition that describes the intended subject of the activity
                # being defined.
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
                # The date  (and optionally time) when the activity definition was published.
                # The date must change when the business version changes and it must change if
                # the status code changes. In addition, it should change when the substantive
                # content of the activity definition changes.
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
                # The name of the organization or individual that published the activity
                # definition.
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
                # A free text natural language description of the activity definition from a
                # consumer's perspective.
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
                # may be used to assist with indexing and searching for appropriate activity
                # definition instances.
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
                # A legal or geographic region in which the activity definition is intended to
                # be used.
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
                # Explanation of why this activity definition is needed and why it has been
                # designed as it has.
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
                # A detailed description of how the activity definition is used from a clinical
                # perspective.
                StructField("usage", StringType(), True),
                # A copyright statement relating to the activity definition and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the activity definition.
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
                # The period during which the activity definition content was or is planned to
                # be in active use.
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
                # Descriptive topics related to the content of the activity. Topics provide a
                # high-level categorization of the activity that can be useful for filtering and
                # searching.
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
                # A reference to a Library resource containing any formal logic used by the
                # activity definition.
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
                # A description of the kind of resource the activity definition is representing.
                # For example, a MedicationRequest, a ServiceRequest, or a CommunicationRequest.
                # Typically, but not always, this is a Request resource.
                StructField(
                    "kind",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A profile to which the target of the activity definition is expected to
                # conform.
                StructField(
                    "profile",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Detailed description of the type of activity; e.g. What lab test, what
                # procedure, what kind of encounter.
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
                # Indicates the level of authority/intentionality associated with the activity
                # and where the request should fit into the workflow chain.
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
                # Indicates how quickly the activity  should be addressed with respect to other
                # requests.
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
                # Set this to true if the definition is to indicate that a particular activity
                # should NOT be performed. If true, this element should be interpreted to
                # reinforce a negative coding. For example NPO as a code with a doNotPerform of
                # true would still indicate to NOT perform the action.
                StructField("doNotPerform", BooleanType(), True),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField("timingDateTime", TimestampType(), True),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period, timing or frequency upon which the described activity is to occur.
                StructField(
                    "timingDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the facility where the activity will occur; e.g. home, hospital,
                # specific clinic, etc.
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
                # Indicates who should participate in performing the action described.
                StructField(
                    "participant",
                    ArrayType(
                        ActivityDefinition_ParticipantSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Identifies the food, drug or other product being consumed or supplied in the
                # activity.
                StructField(
                    "productReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the food, drug or other product being consumed or supplied in the
                # activity.
                StructField(
                    "productCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the quantity expected to be consumed at once (per dose, per meal,
                # etc.).
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
                # Provides detailed dosage instructions in the same way that they are described
                # for MedicationRequest resources.
                StructField(
                    "dosage",
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
                # Indicates the sites on the subject's body where the procedure should be
                # performed (I.e. the target sites).
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
                # Defines specimen requirements for the action to be performed, such as required
                # specimens for a lab test.
                StructField(
                    "specimenRequirement",
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
                # Defines observation requirements for the action to be performed, such as body
                # weight or surface area.
                StructField(
                    "observationRequirement",
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
                # Defines the observations that are expected to be produced by the action.
                StructField(
                    "observationResultRequirement",
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
                # A reference to a StructureMap resource that defines a transform that can be
                # executed to produce the intent resource using the ActivityDefinition instance
                # as the input.
                StructField(
                    "transform",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Dynamic values that will be evaluated to produce values for elements of the
                # resulting resource. For example, if the dosage of a medication must be
                # computed based on the patient's weight, a dynamic value would be used to
                # specify an expression that calculated the weight, and the path on the request
                # resource that would contain the result.
                StructField(
                    "dynamicValue",
                    ArrayType(
                        ActivityDefinition_DynamicValueSchema.schema(
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