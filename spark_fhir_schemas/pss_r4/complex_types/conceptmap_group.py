from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchConceptMap_Group(AutoMapperDataTypeComplexBase):
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
        source: Optional[Any] = None,
        sourceVersion: Optional[Any] = None,
        target: Optional[Any] = None,
        targetVersion: Optional[Any] = None,
        element: Optional[Any] = None,
        unmapped: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            source=source,
            sourceVersion=sourceVersion,
            target=target,
            targetVersion=targetVersion,
            element=element,
            unmapped=unmapped,
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

        source: An absolute URI that identifies the source system where the concepts to be
            mapped are defined.

        sourceVersion: The specific version of the code system, as determined by the code system
            authority.

        target: An absolute URI that identifies the target system that the concepts will be
            mapped to.

        targetVersion: The specific version of the code system, as determined by the code system
            authority.

        element: Mappings for an individual concept in the source to one or more concepts in
            the target.

        unmapped: What to do when there is no mapping for the source concept. "Unmapped" does
            not include codes that are unmatched, and the unmapped element is ignored in a
            code is specified to have equivalence = unmatched.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.conceptmap_element import (
            AutoMapperElasticSearchConceptMap_Element as ConceptMap_ElementSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.conceptmap_unmapped import (
            AutoMapperElasticSearchConceptMap_Unmapped as ConceptMap_UnmappedSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ConceptMap_Group") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ConceptMap_Group"]
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
                # An absolute URI that identifies the source system where the concepts to be
                # mapped are defined.
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
                # The specific version of the code system, as determined by the code system
                # authority.
                StructField("sourceVersion", StringType(), True),
                # An absolute URI that identifies the target system that the concepts will be
                # mapped to.
                StructField(
                    "target",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The specific version of the code system, as determined by the code system
                # authority.
                StructField("targetVersion", StringType(), True),
                # Mappings for an individual concept in the source to one or more concepts in
                # the target.
                StructField(
                    "element",
                    ArrayType(
                        ConceptMap_ElementSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # What to do when there is no mapping for the source concept. "Unmapped" does
                # not include codes that are unmatched, and the unmapped element is ignored in a
                # code is specified to have equivalence = unmatched.
                StructField(
                    "unmapped",
                    ConceptMap_UnmappedSchema.schema(
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