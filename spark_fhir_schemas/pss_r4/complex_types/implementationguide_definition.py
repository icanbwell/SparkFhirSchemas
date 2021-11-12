from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchImplementationGuide_Definition(
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
        grouping: Optional[Any] = None,
        resource: Optional[Any] = None,
        page: Optional[Any] = None,
        parameter: Optional[Any] = None,
        template: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            grouping=grouping,
            resource=resource,
            page=page,
            parameter=parameter,
            template=template,
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

        grouping: A logical group of resources. Logical groups can be used when building pages.

        resource: A resource that is part of the implementation guide. Conformance resources
            (value set, structure definition, capability statements etc.) are obvious
            candidates for inclusion, but any kind of resource can be included as an
            example resource.

        page: A page / section in the implementation guide. The root page is the
            implementation guide home page.

        parameter: Defines how IG is built by tools.

        template: A template for building resources.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_grouping import (
            AutoMapperElasticSearchImplementationGuide_Grouping as ImplementationGuide_GroupingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_resource import (
            AutoMapperElasticSearchImplementationGuide_Resource as ImplementationGuide_ResourceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_page import (
            AutoMapperElasticSearchImplementationGuide_Page as ImplementationGuide_PageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_parameter import (
            AutoMapperElasticSearchImplementationGuide_Parameter as ImplementationGuide_ParameterSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.implementationguide_template import (
            AutoMapperElasticSearchImplementationGuide_Template as ImplementationGuide_TemplateSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ImplementationGuide_Definition")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ImplementationGuide_Definition"]
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
                # A logical group of resources. Logical groups can be used when building pages.
                StructField(
                    "grouping",
                    ArrayType(
                        ImplementationGuide_GroupingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
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
                        ImplementationGuide_ResourceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A page / section in the implementation guide. The root page is the
                # implementation guide home page.
                StructField(
                    "page",
                    ImplementationGuide_PageSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Defines how IG is built by tools.
                StructField(
                    "parameter",
                    ArrayType(
                        ImplementationGuide_ParameterSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A template for building resources.
                StructField(
                    "template",
                    ArrayType(
                        ImplementationGuide_TemplateSchema.schema(
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
