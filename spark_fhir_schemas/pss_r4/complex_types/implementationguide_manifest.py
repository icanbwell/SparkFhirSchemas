from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchImplementationGuide_Manifest(
    AutoMapperDataTypeComplexBase
):
    """
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used to
    gather all the parts of an implementation guide into a logical whole and to
    publish a computable definition of all the parts.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        rendering: Optional[Any] = None,
        resource: Optional[Any] = None,
        page: Optional[Any] = None,
        image: Optional[Any] = None,
        other: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            rendering=rendering,
            resource=resource,
            page=page,
            image=image,
            other=other,
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


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        rendering: A pointer to official web page, PDF or other rendering of the implementation
            guide.

        resource: A resource that is part of the implementation guide. Conformance resources
            (value set, structure definition, capability statements etc.) are obvious
            candidates for inclusion, but any kind of resource can be included as an
            example resource.

        page: Information about a page within the IG.

        image: Indicates a relative path to an image that exists within the IG.

        other: Indicates the relative path of an additional non-page, non-image file that is
            part of the IG - e.g. zip, jar and similar files that could be the target of a
            hyperlink in a derived IG.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.url import (
            AutoMapperElasticSearchurl as urlSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_resource1 import (
            AutoMapperElasticSearchImplementationGuide_Resource1 as ImplementationGuide_Resource1Schema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_page1 import (
            AutoMapperElasticSearchImplementationGuide_Page1 as ImplementationGuide_Page1Schema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ImplementationGuide_Manifest")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ImplementationGuide_Manifest"]
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
                # A pointer to official web page, PDF or other rendering of the implementation
                # guide.
                StructField(
                    "rendering",
                    urlSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A resource that is part of the implementation guide. Conformance resources
                # (value set, structure definition, capability statements etc.) are obvious
                # candidates for inclusion, but any kind of resource can be included as an
                # example resource.
                StructField(
                    "resource",
                    ArrayType(
                        ImplementationGuide_Resource1Schema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Information about a page within the IG.
                StructField(
                    "page",
                    ArrayType(
                        ImplementationGuide_Page1Schema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates a relative path to an image that exists within the IG.
                StructField("image", ArrayType(StringType()), True),
                # Indicates the relative path of an additional non-page, non-image file that is
                # part of the IG - e.g. zip, jar and similar files that could be the target of a
                # hyperlink in a derived IG.
                StructField("other", ArrayType(StringType()), True),
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
