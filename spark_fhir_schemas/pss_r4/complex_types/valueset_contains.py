from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchValueSet_Contains(AutoMapperDataTypeComplexBase):
    """
    A ValueSet resource instance specifies a set of codes drawn from one or more
    code systems, intended for use in a particular context. Value sets link
    between [[[CodeSystem]]] definitions and their use in [coded
    elements](terminologies.html).
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        system: Optional[Any] = None,
        abstract: Optional[Any] = None,
        inactive: Optional[Any] = None,
        version: Optional[Any] = None,
        code: Optional[Any] = None,
        display: Optional[Any] = None,
        designation: Optional[Any] = None,
        contains: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            system=system,
            abstract=abstract,
            inactive=inactive,
            version=version,
            code=code,
            display=display,
            designation=designation,
            contains=contains,
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
        A ValueSet resource instance specifies a set of codes drawn from one or more
        code systems, intended for use in a particular context. Value sets link
        between [[[CodeSystem]]] definitions and their use in [coded
        elements](terminologies.html).


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        system: An absolute URI which is the code system in which the code for this item in
            the expansion is defined.

        abstract: If true, this entry is included in the expansion for navigational purposes,
            and the user cannot select the code directly as a proper value.

        inactive: If the concept is inactive in the code system that defines it. Inactive codes
            are those that are no longer to be used, but are maintained by the code system
            for understanding legacy data. It might not be known or specified whether an
            concept is inactive (and it may depend on the context of use).

        version: The version of the code system from this code was taken. Note that a well-
            maintained code system does not need the version reported, because the meaning
            of codes is consistent across versions. However this cannot consistently be
            assured, and when the meaning is not guaranteed to be consistent, the version
            SHOULD be exchanged.

        code: The code for this item in the expansion hierarchy. If this code is missing the
            entry in the hierarchy is a place holder (abstract) and does not represent a
            valid code in the value set.

        display: The recommended display for this item in the expansion.

        designation: Additional representations for this item - other languages, aliases,
            specialized purposes, used for particular purposes, etc. These are relevant
            when the conditions of the expansion do not fix to a single correct
            representation.

        contains: Other codes and entries contained under this entry in the hierarchy.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.valueset_designation import (
            AutoMapperElasticSearchValueSet_Designation as ValueSet_DesignationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ValueSet_Contains") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet_Contains"]
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
                # An absolute URI which is the code system in which the code for this item in
                # the expansion is defined.
                StructField(
                    "system",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If true, this entry is included in the expansion for navigational purposes,
                # and the user cannot select the code directly as a proper value.
                StructField("abstract", BooleanType(), True),
                # If the concept is inactive in the code system that defines it. Inactive codes
                # are those that are no longer to be used, but are maintained by the code system
                # for understanding legacy data. It might not be known or specified whether an
                # concept is inactive (and it may depend on the context of use).
                StructField("inactive", BooleanType(), True),
                # The version of the code system from this code was taken. Note that a well-
                # maintained code system does not need the version reported, because the meaning
                # of codes is consistent across versions. However this cannot consistently be
                # assured, and when the meaning is not guaranteed to be consistent, the version
                # SHOULD be exchanged.
                StructField("version", StringType(), True),
                # The code for this item in the expansion hierarchy. If this code is missing the
                # entry in the hierarchy is a place holder (abstract) and does not represent a
                # valid code in the value set.
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
                # The recommended display for this item in the expansion.
                StructField("display", StringType(), True),
                # Additional representations for this item - other languages, aliases,
                # specialized purposes, used for particular purposes, etc. These are relevant
                # when the conditions of the expansion do not fix to a single correct
                # representation.
                StructField(
                    "designation",
                    ArrayType(
                        ValueSet_DesignationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Other codes and entries contained under this entry in the hierarchy.
                StructField(
                    "contains",
                    ArrayType(
                        ValueSet_ContainsSchema.schema(
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
