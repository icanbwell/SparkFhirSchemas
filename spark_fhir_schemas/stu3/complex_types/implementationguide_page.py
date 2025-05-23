from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ImplementationGuide_PageSchema:
    """
    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole and to publish a computable definition of all the parts.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
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
            "valueQuantity",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        A set of rules of how FHIR is used to solve a particular problem. This
        resource is used to gather all the parts of an implementation guide into a
        logical whole and to publish a computable definition of all the parts.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        source: The source address for the page.

        title: A short title used to represent this page in navigational structures such as
            table of contents, bread crumbs, etc.

        kind: The kind of page that this is. Some pages are autogenerated (list, example),
            and other kinds are of interest so that tools can navigate the user to the
            page of interest.

        type: For constructed pages, what kind of resources to include in the list.

        package: For constructed pages, a list of packages to include in the page (or else
            empty for everything).

        format: The format of the page.

        page: Nested Pages/Sections under this page.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema

        if (
            max_recursion_limit
            and nesting_list.count("ImplementationGuide_Page") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ImplementationGuide_Page"]
        schema = StructType(
            [
                # unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
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
                        )
                    ),
                    True,
                ),
                # The source address for the page.
                StructField("source", StringType(), True),
                # A short title used to represent this page in navigational structures such as
                # table of contents, bread crumbs, etc.
                StructField("title", StringType(), True),
                # The kind of page that this is. Some pages are autogenerated (list, example),
                # and other kinds are of interest so that tools can navigate the user to the
                # page of interest.
                StructField("kind", StringType(), True),
                # For constructed pages, what kind of resources to include in the list.
                StructField("type", ArrayType(StringType()), True),
                # For constructed pages, a list of packages to include in the page (or else
                # empty for everything).
                StructField("package", ArrayType(StringType()), True),
                # The format of the page.
                StructField("format", StringType(), True),
                # Nested Pages/Sections under this page.
                StructField(
                    "page",
                    ArrayType(
                        ImplementationGuide_PageSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
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

        return schema
