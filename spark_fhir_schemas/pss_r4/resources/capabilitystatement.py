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
class AutoMapperElasticSearchCapabilityStatement(AutoMapperDataTypeComplexBase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR
    Server for a particular version of FHIR that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
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
        version: Optional[Any] = None,
        name: Optional[Any] = None,
        title: Optional[Any] = None,
        status: Optional[Any] = None,
        experimental: Optional[Any] = None,
        date: Optional[Any] = None,
        publisher: Optional[Any] = None,
        contact: Optional[Any] = None,
        description: Optional[Any] = None,
        useContext: Optional[Any] = None,
        jurisdiction: Optional[Any] = None,
        purpose: Optional[Any] = None,
        copyright_: Optional[Any] = None,
        kind: Optional[Any] = None,
        instantiates: Optional[Any] = None,
        imports: Optional[Any] = None,
        software: Optional[Any] = None,
        implementation: Optional[Any] = None,
        fhirVersion: Optional[Any] = None,
        format_: Optional[Any] = None,
        patchFormat: Optional[Any] = None,
        implementationGuide: Optional[Any] = None,
        rest: Optional[Any] = None,
        messaging: Optional[Any] = None,
        document: Optional[Any] = None,
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
            version=version,
            name=name,
            title=title,
            status=status,
            experimental=experimental,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            copyright_=copyright_,
            kind=kind,
            instantiates=instantiates,
            imports=imports,
            software=software,
            implementation=implementation,
            fhirVersion=fhirVersion,
            format_=format_,
            patchFormat=patchFormat,
            implementationGuide=implementationGuide,
            rest=rest,
            messaging=messaging,
            document=document,
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
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server for a particular version of FHIR that may be used as a statement of
        actual server functionality or a statement of required or desired server
        implementation.


        resourceType: This is a CapabilityStatement resource

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

        url: An absolute URI that is used to identify this capability statement when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this capability
            statement is (or will be) published. This URL can be the target of a canonical
            reference. It SHALL remain the same when the capability statement is stored on
            different servers.

        version: The identifier that is used to identify this version of the capability
            statement when it is referenced in a specification, model, design or instance.
            This is an arbitrary value managed by the capability statement author and is
            not expected to be globally unique. For example, it might be a timestamp (e.g.
            yyyymmdd) if a managed version is not available. There is also no expectation
            that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the capability statement. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the capability statement.

        status: The status of this capability statement. Enables tracking the life-cycle of
            the content.

        experimental: A Boolean value to indicate that this capability statement is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        date: The date  (and optionally time) when the capability statement was published.
            The date must change when the business version changes and it must change if
            the status code changes. In addition, it should change when the substantive
            content of the capability statement changes.

        publisher: The name of the organization or individual that published the capability
            statement.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the capability statement from a
            consumer's perspective. Typically, this is used when the capability statement
            describes a desired rather than an actual solution, for example as a formal
            expression of requirements as part of an RFP.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate capability
            statement instances.

        jurisdiction: A legal or geographic region in which the capability statement is intended to
            be used.

        purpose: Explanation of why this capability statement is needed and why it has been
            designed as it has.

        copyright: A copyright statement relating to the capability statement and/or its
            contents. Copyright statements are generally legal restrictions on the use and
            publishing of the capability statement.

        kind: The way that this statement is intended to be used, to describe an actual
            running instance of software, a particular product (kind, not instance of
            software) or a class of implementation (e.g. a desired purchase).

        instantiates: Reference to a canonical URL of another CapabilityStatement that this software
            implements. This capability statement is a published API description that
            corresponds to a business service. The server may actually implement a subset
            of the capability statement it claims to implement, so the capability
            statement must specify the full capability details.

        imports: Reference to a canonical URL of another CapabilityStatement that this software
            adds to. The capability statement automatically includes everything in the
            other statement, and it is not duplicated, though the server may repeat the
            same resources, interactions and operations to add additional details to them.

        software: Software that is covered by this capability statement.  It is used when the
            capability statement describes the capabilities of a particular software
            version, independent of an installation.

        implementation: Identifies a specific implementation instance that is described by the
            capability statement - i.e. a particular installation, rather than the
            capabilities of a software program.

        fhirVersion: The version of the FHIR specification that this CapabilityStatement describes
            (which SHALL be the same as the FHIR version of the CapabilityStatement
            itself). There is no default value.

        format: A list of the formats supported by this implementation using their content
            types.

        patchFormat: A list of the patch formats supported by this implementation using their
            content types.

        implementationGuide: A list of implementation guides that the server does (or should) support in
            their entirety.

        rest: A definition of the restful capabilities of the solution, if any.

        messaging: A description of the messaging capabilities of the solution.

        document: A document definition.

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
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_software import (
            AutoMapperElasticSearchCapabilityStatement_Software as CapabilityStatement_SoftwareSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_implementation import (
            AutoMapperElasticSearchCapabilityStatement_Implementation as CapabilityStatement_ImplementationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_rest import (
            AutoMapperElasticSearchCapabilityStatement_Rest as CapabilityStatement_RestSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_messaging import (
            AutoMapperElasticSearchCapabilityStatement_Messaging as CapabilityStatement_MessagingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_document import (
            AutoMapperElasticSearchCapabilityStatement_Document as CapabilityStatement_DocumentSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("CapabilityStatement") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CapabilityStatement"]
        schema = StructType(
            [
                # This is a CapabilityStatement resource
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
                # An absolute URI that is used to identify this capability statement when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this capability
                # statement is (or will be) published. This URL can be the target of a canonical
                # reference. It SHALL remain the same when the capability statement is stored on
                # different servers.
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
                # The identifier that is used to identify this version of the capability
                # statement when it is referenced in a specification, model, design or instance.
                # This is an arbitrary value managed by the capability statement author and is
                # not expected to be globally unique. For example, it might be a timestamp (e.g.
                # yyyymmdd) if a managed version is not available. There is also no expectation
                # that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the capability statement. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the capability statement.
                StructField("title", StringType(), True),
                # The status of this capability statement. Enables tracking the life-cycle of
                # the content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this capability statement is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the capability statement was published.
                # The date must change when the business version changes and it must change if
                # the status code changes. In addition, it should change when the substantive
                # content of the capability statement changes.
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
                # The name of the organization or individual that published the capability
                # statement.
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
                # A free text natural language description of the capability statement from a
                # consumer's perspective. Typically, this is used when the capability statement
                # describes a desired rather than an actual solution, for example as a formal
                # expression of requirements as part of an RFP.
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
                # may be used to assist with indexing and searching for appropriate capability
                # statement instances.
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
                # A legal or geographic region in which the capability statement is intended to
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
                # Explanation of why this capability statement is needed and why it has been
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
                # A copyright statement relating to the capability statement and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the capability statement.
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
                # The way that this statement is intended to be used, to describe an actual
                # running instance of software, a particular product (kind, not instance of
                # software) or a class of implementation (e.g. a desired purchase).
                StructField("kind", StringType(), True),
                # Reference to a canonical URL of another CapabilityStatement that this software
                # implements. This capability statement is a published API description that
                # corresponds to a business service. The server may actually implement a subset
                # of the capability statement it claims to implement, so the capability
                # statement must specify the full capability details.
                StructField(
                    "instantiates",
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
                # Reference to a canonical URL of another CapabilityStatement that this software
                # adds to. The capability statement automatically includes everything in the
                # other statement, and it is not duplicated, though the server may repeat the
                # same resources, interactions and operations to add additional details to them.
                StructField(
                    "imports",
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
                # Software that is covered by this capability statement.  It is used when the
                # capability statement describes the capabilities of a particular software
                # version, independent of an installation.
                StructField(
                    "software",
                    CapabilityStatement_SoftwareSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies a specific implementation instance that is described by the
                # capability statement - i.e. a particular installation, rather than the
                # capabilities of a software program.
                StructField(
                    "implementation",
                    CapabilityStatement_ImplementationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The version of the FHIR specification that this CapabilityStatement describes
                # (which SHALL be the same as the FHIR version of the CapabilityStatement
                # itself). There is no default value.
                StructField("fhirVersion", StringType(), True),
                # A list of the formats supported by this implementation using their content
                # types.
                StructField(
                    "format",
                    ArrayType(
                        codeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A list of the patch formats supported by this implementation using their
                # content types.
                StructField(
                    "patchFormat",
                    ArrayType(
                        codeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A list of implementation guides that the server does (or should) support in
                # their entirety.
                StructField(
                    "implementationGuide",
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
                # A definition of the restful capabilities of the solution, if any.
                StructField(
                    "rest",
                    ArrayType(
                        CapabilityStatement_RestSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A description of the messaging capabilities of the solution.
                StructField(
                    "messaging",
                    ArrayType(
                        CapabilityStatement_MessagingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A document definition.
                StructField(
                    "document",
                    ArrayType(
                        CapabilityStatement_DocumentSchema.schema(
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