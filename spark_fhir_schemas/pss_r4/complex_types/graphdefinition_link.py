from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchGraphDefinition_Link(AutoMapperDataTypeComplexBase):
    """
    A formal computable definition of a graph of resources - that is, a coherent
    set of resources that form a graph by following references. The Graph
    Definition resource defines a set and makes rules about the set.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        path: Optional[Any] = None,
        sliceName: Optional[Any] = None,
        min_: Optional[Any] = None,
        max_: Optional[Any] = None,
        description: Optional[Any] = None,
        target: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            path=path,
            sliceName=sliceName,
            min_=min_,
            max_=max_,
            description=description,
            target=target,
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
        A formal computable definition of a graph of resources - that is, a coherent
        set of resources that form a graph by following references. The Graph
        Definition resource defines a set and makes rules about the set.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        path: A FHIR expression that identifies one of FHIR References to other resources.

        sliceName: Which slice (if profiled).

        min: Minimum occurrences for this link.

        max: Maximum occurrences for this link.

        description: Information about why this link is of interest in this graph definition.

        target: Potential target for the link.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.graphdefinition_target import (
            AutoMapperElasticSearchGraphDefinition_Target as GraphDefinition_TargetSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("GraphDefinition_Link") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["GraphDefinition_Link"]
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
                # A FHIR expression that identifies one of FHIR References to other resources.
                StructField("path", StringType(), True),
                # Which slice (if profiled).
                StructField("sliceName", StringType(), True),
                # Minimum occurrences for this link.
                StructField(
                    "min",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Maximum occurrences for this link.
                StructField("max", StringType(), True),
                # Information about why this link is of interest in this graph definition.
                StructField("description", StringType(), True),
                # Potential target for the link.
                StructField(
                    "target",
                    ArrayType(
                        GraphDefinition_TargetSchema.schema(
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
