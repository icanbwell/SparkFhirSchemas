from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class MetaSchema:
    """
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always be
    associated with version changes to the resource.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = None,
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
        include_modifierExtension: Optional[bool] = False,
        use_date_for: Optional[List[str]] = None,
        parent_path: Optional[str] = "",
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
        if extension_fields is None:
            extension_fields = [
                "valueBoolean",
                "valueCode",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueId",
                "valueInteger",
                "valuePositiveInt",
                "valueString",
                "valueTime",
                "valueUnsignedInt",
                "valueUri",
                "valueUrl",
                "valueReference",
                "valueCodeableConcept",
                "valueAddress",
            ]
        from spark_fhir_schemas.r4b.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4b.simple_types.id import idSchema
        from spark_fhir_schemas.r4b.simple_types.instant import instantSchema
        from spark_fhir_schemas.r4b.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4b.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4b.complex_types.coding import CodingSchema

        if (
            max_recursion_limit and nesting_list.count("Meta") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Meta"]
        my_parent_path = parent_path + ".meta" if parent_path else "meta"
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
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # The version specific identifier, as it appears in the version portion of the
                # URL. This value changes when the resource is created, updated, or deleted.
                StructField(
                    "versionId",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".versionid",
                    ),
                    True,
                ),
                # When the resource last changed - e.g. when the version changed.
                StructField(
                    "lastUpdated",
                    instantSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".lastupdated",
                    ),
                    True,
                ),
                # A uri that identifies the source system of the resource. This provides a
                # minimal amount of [[[Provenance]]] information that can be used to track or
                # differentiate the source of information in the resource. The source may
                # identify another FHIR server, document, message, database, etc.
                StructField(
                    "source",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".source",
                    ),
                    True,
                ),
                # A list of profiles (references to [[[StructureDefinition]]] resources) that
                # this resource claims to conform to. The URL is a reference to
                # [[[StructureDefinition.url]]].
                StructField(
                    "profile",
                    ArrayType(
                        canonicalSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # Security labels applied to this resource. These tags connect specific
                # resources to the overall security policy and infrastructure.
                StructField(
                    "security",
                    ArrayType(
                        CodingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
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
                        CodingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                (
                    c
                    if c.name != "extension"
                    else StructField("extension", StringType(), True)
                )
                for c in schema.fields
            ]

        if not include_modifierExtension:
            schema.fields = [
                (
                    c
                    if c.name != "modifierExtension"
                    else StructField("modifierExtension", StringType(), True)
                )
                for c in schema.fields
            ]

        return schema
