from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchValueSet_Expansion(AutoMapperDataTypeComplexBase):
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
        identifier: Optional[Any] = None,
        timestamp: Optional[Any] = None,
        total: Optional[Any] = None,
        offset: Optional[Any] = None,
        parameter: Optional[Any] = None,
        contains: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            identifier=identifier,
            timestamp=timestamp,
            total=total,
            offset=offset,
            parameter=parameter,
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

        identifier: An identifier that uniquely identifies this expansion of the valueset, based
            on a unique combination of the provided parameters, the system default
            parameters, and the underlying system code system versions etc. Systems may
            re-use the same identifier as long as those factors remain the same, and the
            expansion is the same, but are not required to do so. This is a business
            identifier.

        timestamp: The time at which the expansion was produced by the expanding system.

        total: The total number of concepts in the expansion. If the number of concept nodes
            in this resource is less than the stated number, then the server can return
            more using the offset parameter.

        offset: If paging is being used, the offset at which this resource starts.  I.e. this
            resource is a partial view into the expansion. If paging is not being used,
            this element SHALL NOT be present.

        parameter: A parameter that controlled the expansion process. These parameters may be
            used by users of expanded value sets to check whether the expansion is
            suitable for a particular purpose, or to pick the correct expansion.

        contains: The codes that are contained in the value set expansion.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.valueset_parameter import (
            AutoMapperElasticSearchValueSet_Parameter as ValueSet_ParameterSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.valueset_contains import (
            AutoMapperElasticSearchValueSet_Contains as ValueSet_ContainsSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ValueSet_Expansion") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet_Expansion"]
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
                # An identifier that uniquely identifies this expansion of the valueset, based
                # on a unique combination of the provided parameters, the system default
                # parameters, and the underlying system code system versions etc. Systems may
                # re-use the same identifier as long as those factors remain the same, and the
                # expansion is the same, but are not required to do so. This is a business
                # identifier.
                StructField(
                    "identifier",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The time at which the expansion was produced by the expanding system.
                StructField(
                    "timestamp",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The total number of concepts in the expansion. If the number of concept nodes
                # in this resource is less than the stated number, then the server can return
                # more using the offset parameter.
                StructField(
                    "total",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If paging is being used, the offset at which this resource starts.  I.e. this
                # resource is a partial view into the expansion. If paging is not being used,
                # this element SHALL NOT be present.
                StructField(
                    "offset",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A parameter that controlled the expansion process. These parameters may be
                # used by users of expanded value sets to check whether the expansion is
                # suitable for a particular purpose, or to pick the correct expansion.
                StructField(
                    "parameter",
                    ArrayType(
                        ValueSet_ParameterSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The codes that are contained in the value set expansion.
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
