from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchConceptMap_Target(AutoMapperDataTypeComplexBase):
    """
    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        code: Optional[Any] = None,
        display: Optional[Any] = None,
        equivalence: Optional[Any] = None,
        comment: Optional[Any] = None,
        dependsOn: Optional[Any] = None,
        product: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            display=display,
            equivalence=equivalence,
            comment=comment,
            dependsOn=dependsOn,
            product=product,
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
        A statement of relationships from one set of concepts to one or more other
        concepts - either concepts in code systems, or data element/data element
        concepts, or classes in class models.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        code: Identity (code or path) or the element/item that the map refers to.

        display: The display for the code. The display is only provided to help editors when
            editing the concept map.

        equivalence: The equivalence between the source and target concepts (counting for the
            dependencies and products). The equivalence is read from target to source
            (e.g. the target is 'wider' than the source).

        comment: A description of status/issues in mapping that conveys additional information
            not represented in  the structured data.

        dependsOn: A set of additional dependencies for this mapping to hold. This mapping is
            only applicable if the specified element can be resolved, and it has the
            specified value.

        product: A set of additional outcomes from this mapping to other elements. To properly
            execute this mapping, the specified element must be mapped to some data
            element or source that is in context. The mapping may still be useful without
            a place for the additional data elements, but the equivalence cannot be relied
            on.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.conceptmap_dependson import (
            AutoMapperElasticSearchConceptMap_DependsOn as ConceptMap_DependsOnSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ConceptMap_Target") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ConceptMap_Target"]
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
                # Identity (code or path) or the element/item that the map refers to.
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
                # The display for the code. The display is only provided to help editors when
                # editing the concept map.
                StructField("display", StringType(), True),
                # The equivalence between the source and target concepts (counting for the
                # dependencies and products). The equivalence is read from target to source
                # (e.g. the target is 'wider' than the source).
                StructField("equivalence", StringType(), True),
                # A description of status/issues in mapping that conveys additional information
                # not represented in  the structured data.
                StructField("comment", StringType(), True),
                # A set of additional dependencies for this mapping to hold. This mapping is
                # only applicable if the specified element can be resolved, and it has the
                # specified value.
                StructField(
                    "dependsOn",
                    ArrayType(
                        ConceptMap_DependsOnSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A set of additional outcomes from this mapping to other elements. To properly
                # execute this mapping, the specified element must be mapped to some data
                # element or source that is in context. The mapping may still be useful without
                # a place for the additional data elements, but the equivalence cannot be relied
                # on.
                StructField(
                    "product",
                    ArrayType(
                        ConceptMap_DependsOnSchema.schema(
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
