from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ConformanceSchema:
    """
    A conformance statement is a set of capabilities of a FHIR Server that may be
    used as a statement of actual server functionality or a statement of required
    or desired server implementation.
    If the element is present, it must have either a @value, an @id, or extensions
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    A conformance statement is a set of capabilities of a FHIR Server that may be
    used as a statement of actual server functionality or a statement of required
    or desired server implementation.
    If the element is present, it must have either a @value, an @id, or extensions


        id: The logical id of the resource, as used in the URL for the resource. Once
    assigned, this value never changes.
        meta: The metadata about the resource. This is content that is maintained by the
    infrastructure. Changes to the content may not always be associated with
    version changes to the resource.
        implicitRules: A reference to a set of rules that were followed when the resource was
    constructed, and which must be understood when processing the content.
        language: The base language in which the resource is written.
        text: A human-readable narrative that contains a summary of the resource, and may be
    used to represent the content of the resource to a human. The narrative need
    not encode all the structured data, but is required to contain sufficient
    detail to make it "clinically safe" for a human to just read the narrative.
    Resource definitions may define what content should be represented in the
    narrative to ensure clinical safety.
        contained: These resources do not have an independent existence apart from the resource
    that contains them - they cannot be identified independently, and nor can they
    have their own independent transaction scope.
        extension: May be used to represent additional information that is not part of the basic
    definition of the resource. In order to make the use of extensions safe and
    manageable, there is a strict set of governance  applied to the definition and
    use of extensions. Though any implementer is allowed to define an extension,
    there is a set of requirements that SHALL be met as part of the definition of
    the extension.
        modifierExtension: May be used to represent additional information that is not part of the basic
    definition of the resource, and that modifies the understanding of the element
    that contains it. Usually modifier elements provide negation or qualification.
    In order to make the use of extensions safe and manageable, there is a strict
    set of governance applied to the definition and use of extensions. Though any
    implementer is allowed to define an extension, there is a set of requirements
    that SHALL be met as part of the definition of the extension. Applications
    processing a resource are required to check for modifier extensions.
        url: An absolute URL that is used to identify this conformance statement when it is
    referenced in a specification, model, design or an instance. This SHALL be a
    URL, SHOULD be globally unique, and SHOULD be an address at which this
    conformance statement is (or will be) published.
        version: The identifier that is used to identify this version of the conformance
    statement when it is referenced in a specification, model, design or instance.
    This is an arbitrary value managed by the profile author manually and the
    value should be a timestamp.
        name: A free text natural language name identifying the conformance statement.
        status: The status of this conformance statement.
        experimental: A flag to indicate that this conformance statement is authored for testing
    purposes (or education/evaluation/marketing), and is not intended to be used
    for genuine usage.
        publisher: The name of the individual or organization that published the conformance.
        contact: Contacts to assist a user in finding and communicating with the publisher.
        date: The date  (and optionally time) when the conformance statement was published.
    The date must change when the business version changes, if it does, and it
    must change if the status code changes. In addition, it should change when the
    substantive content of the conformance statement changes.
        description: A free text natural language description of the conformance statement and its
    use. Typically, this is used when the conformance statement describes a
    desired rather than an actual solution, for example as a formal expression of
    requirements as part of an RFP.
        requirements: Explains why this conformance statement is needed and why it's been
    constrained as it has.
        copyright: A copyright statement relating to the conformance statement and/or its
    contents. Copyright statements are generally legal restrictions on the use and
    publishing of the details of the system described by the conformance
    statement.
        kind: The way that this statement is intended to be used, to describe an actual
    running instance of software, a particular product (kind not instance of
    software) or a class of implementation (e.g. a desired purchase).
        software: Software that is covered by this conformance statement.  It is used when the
    conformance statement describes the capabilities of a particular software
    version, independent of an installation.
        implementation: Identifies a specific implementation instance that is described by the
    conformance statement - i.e. a particular installation, rather than the
    capabilities of a software program.
        fhirVersion: The version of the FHIR specification on which this conformance statement is
    based.
        acceptUnknown: A code that indicates whether the application accepts unknown elements or
    extensions when reading resources.
        format: A list of the formats supported by this implementation using their content
    types.
        profile: A list of profiles that represent different use cases supported by the system.
    For a server, "supported by the system" means the system hosts/produces a set
    of resources that are conformant to a particular profile, and allows clients
    that use its services to search using this profile and to find appropriate
    data. For a client, it means the system will search by this profile and
    process data according to the guidance implicit in the profile. See further
    discussion in [Using Profiles]{profiling.html#profile-uses}.
        rest: A definition of the restful capabilities of the solution, if any.
        messaging: A description of the messaging capabilities of the solution.
        document: A document definition.
        """
            # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # meta
        from spark_fhir_schemas.dstu2.complex_types.meta import MetaSchema
            # implicitRules
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema
            # language
        from spark_fhir_schemas.dstu2.simple_types.code import codeSchema
            # text
        from spark_fhir_schemas.dstu2.complex_types.narrative import NarrativeSchema
            # contained
        Not mapped: ResourceContainer
            # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # modifierExtension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema
            # url
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema
            # version
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # name
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # status
        from spark_fhir_schemas.dstu2.simple_types.code import codeSchema
            # experimental
        from spark_fhir_schemas.dstu2.simple_types.boolean import booleanSchema
            # publisher
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # contact
        Not mapped: ConformanceContact
            # date
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema
            # description
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # requirements
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # copyright
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # kind
        from spark_fhir_schemas.dstu2.simple_types.conformancestatementkind import ConformanceStatementKindSchema
            # software
        Not mapped: ConformanceSoftware
            # implementation
        Not mapped: ConformanceImplementation
            # fhirVersion
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # acceptUnknown
        from spark_fhir_schemas.dstu2.simple_types.unknowncontentcode import UnknownContentCodeSchema
            # format
        from spark_fhir_schemas.dstu2.simple_types.code import codeSchema
            # profile
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # rest
        Not mapped: ConformanceRest
            # messaging
        Not mapped: ConformanceMessaging
            # document
        Not mapped: ConformanceDocument
        if (max_recursion_limit and nesting_list.count("Conformance") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["Conformance"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", idSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField("meta", MetaSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField("implicitRules", StringType(), True),
                # The base language in which the resource is written.
                StructField("language", codeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField("text", NarrativeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField("contained", ResourceContainerSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField("extension", ExtensionSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource, and that modifies the understanding of the element
                # that contains it. Usually modifier elements provide negation or qualification.
                # In order to make the use of extensions safe and manageable, there is a strict
                # set of governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                StructField("modifierExtension", ExtensionSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # An absolute URL that is used to identify this conformance statement when it is
                # referenced in a specification, model, design or an instance. This SHALL be a
                # URL, SHOULD be globally unique, and SHOULD be an address at which this
                # conformance statement is (or will be) published.
                StructField("url", StringType(), True),
                # The identifier that is used to identify this version of the conformance
                # statement when it is referenced in a specification, model, design or instance.
                # This is an arbitrary value managed by the profile author manually and the
                # value should be a timestamp.
                StructField("version", StringType(), True),
                # A free text natural language name identifying the conformance statement.
                StructField("name", StringType(), True),
                # The status of this conformance statement.
                StructField("status", codeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A flag to indicate that this conformance statement is authored for testing
                # purposes (or education/evaluation/marketing), and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The name of the individual or organization that published the conformance.
                StructField("publisher", StringType(), True),
                # Contacts to assist a user in finding and communicating with the publisher.
                StructField("contact", ConformanceContactSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The date  (and optionally time) when the conformance statement was published.
                # The date must change when the business version changes, if it does, and it
                # must change if the status code changes. In addition, it should change when the
                # substantive content of the conformance statement changes.
                StructField("date", dateTimeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A free text natural language description of the conformance statement and its
                # use. Typically, this is used when the conformance statement describes a
                # desired rather than an actual solution, for example as a formal expression of
                # requirements as part of an RFP.
                StructField("description", StringType(), True),
                # Explains why this conformance statement is needed and why it's been
                # constrained as it has.
                StructField("requirements", StringType(), True),
                # A copyright statement relating to the conformance statement and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the details of the system described by the conformance
                # statement.
                StructField("copyright", StringType(), True),
                # The way that this statement is intended to be used, to describe an actual
                # running instance of software, a particular product (kind not instance of
                # software) or a class of implementation (e.g. a desired purchase).
                StructField("kind", StringType(), True),
                # Software that is covered by this conformance statement.  It is used when the
                # conformance statement describes the capabilities of a particular software
                # version, independent of an installation.
                StructField("software", ConformanceSoftwareSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # Identifies a specific implementation instance that is described by the
                # conformance statement - i.e. a particular installation, rather than the
                # capabilities of a software program.
                StructField("implementation", ConformanceImplementationSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # The version of the FHIR specification on which this conformance statement is
                # based.
                StructField("fhirVersion", idSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A code that indicates whether the application accepts unknown elements or
                # extensions when reading resources.
                StructField("acceptUnknown", StringType(), True),
                # A list of the formats supported by this implementation using their content
                # types.
                StructField("format", codeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A list of profiles that represent different use cases supported by the system.
                # For a server, "supported by the system" means the system hosts/produces a set
                # of resources that are conformant to a particular profile, and allows clients
                # that use its services to search using this profile and to find appropriate
                # data. For a client, it means the system will search by this profile and
                # process data according to the guidance implicit in the profile. See further
                # discussion in [Using Profiles]{profiling.html#profile-uses}.
                StructField("profile", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A definition of the restful capabilities of the solution, if any.
                StructField("rest", ConformanceRestSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A description of the messaging capabilities of the solution.
                StructField("messaging", ConformanceMessagingSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # A document definition.
                StructField("document", ConformanceDocumentSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        return schema