from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchStructureMap_Target(AutoMapperDataTypeComplexBase):
    """
    A Map of relationships between 2 structures that can be used to transform
    data.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        context: Optional[Any] = None,
        contextType: Optional[Any] = None,
        element: Optional[Any] = None,
        variable: Optional[Any] = None,
        listMode: Optional[Any] = None,
        listRuleId: Optional[Any] = None,
        transform: Optional[Any] = None,
        parameter: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            context=context,
            contextType=contextType,
            element=element,
            variable=variable,
            listMode=listMode,
            listRuleId=listRuleId,
            transform=transform,
            parameter=parameter,
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
        A Map of relationships between 2 structures that can be used to transform
        data.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        context: Type or variable this rule applies to.

        contextType: How to interpret the context.

        element: Field to create in the context.

        variable: Named context for field, if desired, and a field is specified.

        listMode: If field is a list, how to manage the list.

        listRuleId: Internal rule reference for shared list items.

        transform: How the data is copied / created.

        parameter: Parameters to the transform.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.structuremap_parameter import (
            AutoMapperElasticSearchStructureMap_Parameter as StructureMap_ParameterSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("StructureMap_Target") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["StructureMap_Target"]
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
                # Type or variable this rule applies to.
                StructField(
                    "context",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # How to interpret the context.
                StructField("contextType", StringType(), True),
                # Field to create in the context.
                StructField("element", StringType(), True),
                # Named context for field, if desired, and a field is specified.
                StructField(
                    "variable",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If field is a list, how to manage the list.
                # Internal rule reference for shared list items.
                StructField(
                    "listRuleId",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # How the data is copied / created.
                StructField("transform", StringType(), True),
                # Parameters to the transform.
                StructField(
                    "parameter",
                    ArrayType(
                        StructureMap_ParameterSchema.schema(
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