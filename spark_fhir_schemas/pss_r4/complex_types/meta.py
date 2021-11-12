from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMeta(AutoMapperDataTypeComplexBase):
    """
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always be
    associated with version changes to the resource.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        versionId: Optional[Any] = None,
        lastUpdated: Optional[Any] = None,
        source: Optional[Any] = None,
        profile: Optional[Any] = None,
        security: Optional[Any] = None,
        tag: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            versionId=versionId,
            lastUpdated=lastUpdated,
            source=source,
            profile=profile,
            security=security,
            tag=tag,
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
        The metadata about a resource. This is content in the resource that is
        maintained by the infrastructure. Changes to the content might not always be
        associated with version changes to the resource.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        versionId: The version specific identifier, as it appears in the version portion of the
            URL. This value changes when the resource is created, updated, or deleted.

        lastUpdated: When the resource last changed - e.g. when the version changed.

        source: A uri that identifies the source system of the resource. This provides a
            minimal amount of [[[Provenance]]] information that can be used to track or
            differentiate the source of information in the resource. The source may
            identify another FHIR server, document, message, database, etc.

        profile: A list of profiles (references to [[[StructureDefinition]]] resources) that
            this resource claims to conform to. The URL is a reference to
            [[[StructureDefinition.url]]].

        security: Security labels applied to this resource. These tags connect specific
            resources to the overall security policy and infrastructure.

        tag: Tags applied to this resource. Tags are intended to be used to identify and
            relate resources to process and workflow, and applications are not required to
            consider the tags when interpreting the meaning of a resource.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.instant import (
            AutoMapperElasticSearchinstant as instantSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Meta") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Meta"]
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
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
                # The version specific identifier, as it appears in the version portion of the
                # URL. This value changes when the resource is created, updated, or deleted.
                StructField(
                    "versionId",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # When the resource last changed - e.g. when the version changed.
                StructField(
                    "lastUpdated",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A uri that identifies the source system of the resource. This provides a
                # minimal amount of [[[Provenance]]] information that can be used to track or
                # differentiate the source of information in the resource. The source may
                # identify another FHIR server, document, message, database, etc.
                StructField(
                    "source",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A list of profiles (references to [[[StructureDefinition]]] resources) that
                # this resource claims to conform to. The URL is a reference to
                # [[[StructureDefinition.url]]].
                StructField(
                    "profile",
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
                # Security labels applied to this resource. These tags connect specific
                # resources to the overall security policy and infrastructure.
                StructField(
                    "security",
                    ArrayType(
                        CodingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Tags applied to this resource. Tags are intended to be used to identify and
                # relate resources to process and workflow, and applications are not required to
                # consider the tags when interpreting the meaning of a resource.
                StructField(
                    "tag",
                    ArrayType(
                        CodingSchema.schema(
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
