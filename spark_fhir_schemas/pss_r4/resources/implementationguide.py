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
class AutoMapperElasticSearchImplementationGuide(AutoMapperDataTypeComplexBase):
    """
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used to
    gather all the parts of an implementation guide into a logical whole and to
    publish a computable definition of all the parts.
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
        copyright_: Optional[Any] = None,
        packageId: Optional[Any] = None,
        license_: Optional[Any] = None,
        fhirVersion: Optional[Any] = None,
        dependsOn: Optional[Any] = None,
        global_: Optional[Any] = None,
        definition: Optional[Any] = None,
        manifest: Optional[Any] = None,
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
            copyright_=copyright_,
            packageId=packageId,
            license_=license_,
            fhirVersion=fhirVersion,
            dependsOn=dependsOn,
            global_=global_,
            definition=definition,
            manifest=manifest,
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
        A set of rules of how a particular interoperability or standards problem is
        solved - typically through the use of FHIR resources. This resource is used to
        gather all the parts of an implementation guide into a logical whole and to
        publish a computable definition of all the parts.


        resourceType: This is a ImplementationGuide resource

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

        url: An absolute URI that is used to identify this implementation guide when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this implementation
            guide is (or will be) published. This URL can be the target of a canonical
            reference. It SHALL remain the same when the implementation guide is stored on
            different servers.

        version: The identifier that is used to identify this version of the implementation
            guide when it is referenced in a specification, model, design or instance.
            This is an arbitrary value managed by the implementation guide author and is
            not expected to be globally unique. For example, it might be a timestamp (e.g.
            yyyymmdd) if a managed version is not available. There is also no expectation
            that versions can be placed in a lexicographical sequence.

        name: A natural language name identifying the implementation guide. This name should
            be usable as an identifier for the module by machine processing applications
            such as code generation.

        title: A short, descriptive, user-friendly title for the implementation guide.

        status: The status of this implementation guide. Enables tracking the life-cycle of
            the content.

        experimental: A Boolean value to indicate that this implementation guide is authored for
            testing purposes (or education/evaluation/marketing) and is not intended to be
            used for genuine usage.

        date: The date  (and optionally time) when the implementation guide was published.
            The date must change when the business version changes and it must change if
            the status code changes. In addition, it should change when the substantive
            content of the implementation guide changes.

        publisher: The name of the organization or individual that published the implementation
            guide.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the implementation guide from a
            consumer's perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate
            implementation guide instances.

        jurisdiction: A legal or geographic region in which the implementation guide is intended to
            be used.

        copyright: A copyright statement relating to the implementation guide and/or its
            contents. Copyright statements are generally legal restrictions on the use and
            publishing of the implementation guide.

        packageId: The NPM package name for this Implementation Guide, used in the NPM package
            distribution, which is the primary mechanism by which FHIR based tooling
            manages IG dependencies. This value must be globally unique, and should be
            assigned with care.

        license: The license that applies to this Implementation Guide, using an SPDX license
            code, or 'not-open-source'.

        fhirVersion: The version(s) of the FHIR specification that this ImplementationGuide targets
            - e.g. describes how to use. The value of this element is the formal version
            of the specification, without the revision number, e.g.
            [publication].[major].[minor], which is 4.0.1. for this version.

        dependsOn: Another implementation guide that this implementation depends on. Typically,
            an implementation guide uses value sets, profiles etc.defined in other
            implementation guides.

        global: A set of profiles that all resources covered by this implementation guide must
            conform to.

        definition: The information needed by an IG publisher tool to publish the whole
            implementation guide.

        manifest: Information about an assembled implementation guide, created by the
            publication tooling.

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
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_dependson import (
            AutoMapperElasticSearchImplementationGuide_DependsOn as ImplementationGuide_DependsOnSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_global import (
            AutoMapperElasticSearchImplementationGuide_Global as ImplementationGuide_GlobalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_definition import (
            AutoMapperElasticSearchImplementationGuide_Definition as ImplementationGuide_DefinitionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_manifest import (
            AutoMapperElasticSearchImplementationGuide_Manifest as ImplementationGuide_ManifestSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ImplementationGuide") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ImplementationGuide"]
        schema = StructType(
            [
                # This is a ImplementationGuide resource
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
                # An absolute URI that is used to identify this implementation guide when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this implementation
                # guide is (or will be) published. This URL can be the target of a canonical
                # reference. It SHALL remain the same when the implementation guide is stored on
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
                # The identifier that is used to identify this version of the implementation
                # guide when it is referenced in a specification, model, design or instance.
                # This is an arbitrary value managed by the implementation guide author and is
                # not expected to be globally unique. For example, it might be a timestamp (e.g.
                # yyyymmdd) if a managed version is not available. There is also no expectation
                # that versions can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the implementation guide. This name should
                # be usable as an identifier for the module by machine processing applications
                # such as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the implementation guide.
                StructField("title", StringType(), True),
                # The status of this implementation guide. Enables tracking the life-cycle of
                # the content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this implementation guide is authored for
                # testing purposes (or education/evaluation/marketing) and is not intended to be
                # used for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the implementation guide was published.
                # The date must change when the business version changes and it must change if
                # the status code changes. In addition, it should change when the substantive
                # content of the implementation guide changes.
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
                # The name of the organization or individual that published the implementation
                # guide.
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
                # A free text natural language description of the implementation guide from a
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
                # may be used to assist with indexing and searching for appropriate
                # implementation guide instances.
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
                # A legal or geographic region in which the implementation guide is intended to
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
                # A copyright statement relating to the implementation guide and/or its
                # contents. Copyright statements are generally legal restrictions on the use and
                # publishing of the implementation guide.
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
                # The NPM package name for this Implementation Guide, used in the NPM package
                # distribution, which is the primary mechanism by which FHIR based tooling
                # manages IG dependencies. This value must be globally unique, and should be
                # assigned with care.
                StructField(
                    "packageId",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The license that applies to this Implementation Guide, using an SPDX license
                # code, or 'not-open-source'.
                StructField("license", StringType(), True),
                # The version(s) of the FHIR specification that this ImplementationGuide targets
                # - e.g. describes how to use. The value of this element is the formal version
                # of the specification, without the revision number, e.g.
                # [publication].[major].[minor], which is 4.0.1. for this version.
                # Another implementation guide that this implementation depends on. Typically,
                # an implementation guide uses value sets, profiles etc.defined in other
                # implementation guides.
                StructField(
                    "dependsOn",
                    ArrayType(
                        ImplementationGuide_DependsOnSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A set of profiles that all resources covered by this implementation guide must
                # conform to.
                StructField(
                    "global",
                    ArrayType(
                        ImplementationGuide_GlobalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The information needed by an IG publisher tool to publish the whole
                # implementation guide.
                StructField(
                    "definition",
                    ImplementationGuide_DefinitionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Information about an assembled implementation guide, created by the
                # publication tooling.
                StructField(
                    "manifest",
                    ImplementationGuide_ManifestSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
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