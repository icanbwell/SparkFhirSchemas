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
class AutoMapperElasticSearchSearchParameter(AutoMapperDataTypeComplexBase):
    """
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
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
        derivedFrom: Optional[Any] = None,
        status: Optional[Any] = None,
        experimental: Optional[Any] = None,
        date: Optional[Any] = None,
        publisher: Optional[Any] = None,
        contact: Optional[Any] = None,
        description: Optional[Any] = None,
        useContext: Optional[Any] = None,
        jurisdiction: Optional[Any] = None,
        purpose: Optional[Any] = None,
        code: Optional[Any] = None,
        base: Optional[Any] = None,
        type_: Optional[Any] = None,
        expression: Optional[Any] = None,
        xpath: Optional[Any] = None,
        xpathUsage: Optional[Any] = None,
        target: Optional[Any] = None,
        multipleOr: Optional[Any] = None,
        multipleAnd: Optional[Any] = None,
        comparator: Optional[Any] = None,
        modifier: Optional[Any] = None,
        chain: Optional[Any] = None,
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
            url=url,
            version=version,
            name=name,
            derivedFrom=derivedFrom,
            status=status,
            experimental=experimental,
            date=date,
            publisher=publisher,
            contact=contact,
            description=description,
            useContext=useContext,
            jurisdiction=jurisdiction,
            purpose=purpose,
            code=code,
            base=base,
            type_=type_,
            expression=expression,
            xpath=xpath,
            xpathUsage=xpathUsage,
            target=target,
            multipleOr=multipleOr,
            multipleAnd=multipleAnd,
            comparator=comparator,
            modifier=modifier,
            chain=chain,
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
        A search parameter that defines a named search item that can be used to
        search/filter on a resource.


        resourceType: This is a SearchParameter resource

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

        url: An absolute URI that is used to identify this search parameter when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this search parameter
            is (or will be) published. This URL can be the target of a canonical
            reference. It SHALL remain the same when the search parameter is stored on
            different servers.

        version: The identifier that is used to identify this version of the search parameter
            when it is referenced in a specification, model, design or instance. This is
            an arbitrary value managed by the search parameter author and is not expected
            to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
            a managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the search parameter. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        derivedFrom: Where this search parameter is originally defined. If a derivedFrom is
            provided, then the details in the search parameter must be consistent with the
            definition from which it is defined. i.e. the parameter should have the same
            meaning, and (usually) the functionality should be a proper subset of the
            underlying search parameter.

        status: The status of this search parameter. Enables tracking the life-cycle of the
            content.

        experimental: A Boolean value to indicate that this search parameter is authored for testing
            purposes (or education/evaluation/marketing) and is not intended to be used
            for genuine usage.

        date: The date  (and optionally time) when the search parameter was published. The
            date must change when the business version changes and it must change if the
            status code changes. In addition, it should change when the substantive
            content of the search parameter changes.

        publisher: The name of the organization or individual that published the search
            parameter.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: And how it used.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate search
            parameter instances.

        jurisdiction: A legal or geographic region in which the search parameter is intended to be
            used.

        purpose: Explanation of why this search parameter is needed and why it has been
            designed as it has.

        code: The code used in the URL or the parameter name in a parameters resource for
            this search parameter.

        base: The base resource type(s) that this search parameter can be used against.

        type: The type of value that a search parameter may contain, and how the content is
            interpreted.

        expression: A FHIRPath expression that returns a set of elements for the search parameter.

        xpath: An XPath expression that returns a set of elements for the search parameter.

        xpathUsage: How the search parameter relates to the set of elements returned by evaluating
            the xpath query.

        target: Types of resource (if a resource is referenced).

        multipleOr: Whether multiple values are allowed for each time the parameter exists. Values
            are separated by commas, and the parameter matches if any of the values match.

        multipleAnd: Whether multiple parameters are allowed - e.g. more than one parameter with
            the same name. The search matches if all the parameters match.

        comparator: Comparators supported for the search parameter.

        modifier: A modifier supported for the search parameter.

        chain: Contains the names of any search parameters which may be chained to the
            containing search parameter. Chained parameters may be added to search
            parameters of type reference and specify that resources will only be returned
            if they contain a reference to a resource which matches the chained parameter
            value. Values for this field should be drawn from SearchParameter.code for a
            parameter on the target resource type.

        component: Used to define the parts of a composite search parameter.

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
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
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
        from spark_fhir_schemas.pss_r4.complex_types.searchparameter_component import (
            AutoMapperElasticSearchSearchParameter_Component as SearchParameter_ComponentSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SearchParameter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SearchParameter"]
        schema = StructType(
            [
                # This is a SearchParameter resource
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
                # An absolute URI that is used to identify this search parameter when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this search parameter
                # is (or will be) published. This URL can be the target of a canonical
                # reference. It SHALL remain the same when the search parameter is stored on
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
                # The identifier that is used to identify this version of the search parameter
                # when it is referenced in a specification, model, design or instance. This is
                # an arbitrary value managed by the search parameter author and is not expected
                # to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if
                # a managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the search parameter. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # Where this search parameter is originally defined. If a derivedFrom is
                # provided, then the details in the search parameter must be consistent with the
                # definition from which it is defined. i.e. the parameter should have the same
                # meaning, and (usually) the functionality should be a proper subset of the
                # underlying search parameter.
                StructField(
                    "derivedFrom",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The status of this search parameter. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this search parameter is authored for testing
                # purposes (or education/evaluation/marketing) and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the search parameter was published. The
                # date must change when the business version changes and it must change if the
                # status code changes. In addition, it should change when the substantive
                # content of the search parameter changes.
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
                # The name of the organization or individual that published the search
                # parameter.
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
                # And how it used.
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
                # may be used to assist with indexing and searching for appropriate search
                # parameter instances.
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
                # A legal or geographic region in which the search parameter is intended to be
                # used.
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
                # Explanation of why this search parameter is needed and why it has been
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
                # The code used in the URL or the parameter name in a parameters resource for
                # this search parameter.
                StructField(
                    "code",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The base resource type(s) that this search parameter can be used against.
                StructField(
                    "base",
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
                # The type of value that a search parameter may contain, and how the content is
                # interpreted.
                StructField("type", StringType(), True),
                # A FHIRPath expression that returns a set of elements for the search parameter.
                StructField("expression", StringType(), True),
                # An XPath expression that returns a set of elements for the search parameter.
                StructField("xpath", StringType(), True),
                # How the search parameter relates to the set of elements returned by evaluating
                # the xpath query.
                StructField("xpathUsage", StringType(), True),
                # Types of resource (if a resource is referenced).
                StructField(
                    "target",
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
                # Whether multiple values are allowed for each time the parameter exists. Values
                # are separated by commas, and the parameter matches if any of the values match.
                StructField("multipleOr", BooleanType(), True),
                # Whether multiple parameters are allowed - e.g. more than one parameter with
                # the same name. The search matches if all the parameters match.
                StructField("multipleAnd", BooleanType(), True),
                # Comparators supported for the search parameter.
                # A modifier supported for the search parameter.
                # Contains the names of any search parameters which may be chained to the
                # containing search parameter. Chained parameters may be added to search
                # parameters of type reference and specify that resources will only be returned
                # if they contain a reference to a resource which matches the chained parameter
                # value. Values for this field should be drawn from SearchParameter.code for a
                # parameter on the target resource type.
                StructField("chain", ArrayType(StringType()), True),
                # Used to define the parts of a composite search parameter.
                StructField(
                    "component",
                    ArrayType(
                        SearchParameter_ComponentSchema.schema(
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