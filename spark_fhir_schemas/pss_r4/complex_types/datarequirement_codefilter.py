from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchDataRequirement_CodeFilter(AutoMapperDataTypeComplexBase):
    """
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        path: Optional[Any] = None,
        searchParam: Optional[Any] = None,
        valueSet: Optional[Any] = None,
        code: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            path=path,
            searchParam=searchParam,
            valueSet=valueSet,
            code=code,
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
        Describes a required data item for evaluation in terms of the type of data,
        and optional code or date-based filters of the data.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        path: The code-valued attribute of the filter. The specified path SHALL be a
            FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
            consist only of identifiers, constant indexers, and .resolve(). The path is
            allowed to contain qualifiers (.) to traverse sub-elements, as well as
            indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
            FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
            must be an integer constant. The path must resolve to an element of type code,
            Coding, or CodeableConcept.

        searchParam: A token parameter that refers to a search parameter defined on the specified
            type of the DataRequirement, and which searches on elements of type code,
            Coding, or CodeableConcept.

        valueSet: The valueset for the code filter. The valueSet and code elements are additive.
            If valueSet is specified, the filter will return only those data items for
            which the value of the code-valued element specified in the path is a member
            of the specified valueset.

        code: The codes for the code filter. If values are given, the filter will return
            only those data items for which the code-valued attribute specified by the
            path has a value that is one of the specified codes. If codes are specified in
            addition to a value set, the filter returns items matching a code in the value
            set or one of the specified codes.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("DataRequirement_CodeFilter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["DataRequirement_CodeFilter"]
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
                # The code-valued attribute of the filter. The specified path SHALL be a
                # FHIRPath resolveable on the specified type of the DataRequirement, and SHALL
                # consist only of identifiers, constant indexers, and .resolve(). The path is
                # allowed to contain qualifiers (.) to traverse sub-elements, as well as
                # indexers ([x]) to traverse multiple-cardinality sub-elements (see the [Simple
                # FHIRPath Profile](fhirpath.html#simple) for full details). Note that the index
                # must be an integer constant. The path must resolve to an element of type code,
                # Coding, or CodeableConcept.
                StructField("path", StringType(), True),
                # A token parameter that refers to a search parameter defined on the specified
                # type of the DataRequirement, and which searches on elements of type code,
                # Coding, or CodeableConcept.
                StructField("searchParam", StringType(), True),
                # The valueset for the code filter. The valueSet and code elements are additive.
                # If valueSet is specified, the filter will return only those data items for
                # which the value of the code-valued element specified in the path is a member
                # of the specified valueset.
                StructField(
                    "valueSet",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The codes for the code filter. If values are given, the filter will return
                # only those data items for which the code-valued attribute specified by the
                # path has a value that is one of the specified codes. If codes are specified in
                # addition to a value set, the filter returns items matching a code in the value
                # set or one of the specified codes.
                StructField(
                    "code",
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