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
class AutoMapperElasticSearchCoding(AutoMapperDataTypeComplexBase):
    """
    A reference to a code defined by a terminology system.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        system: Optional[Any] = None,
        version: Optional[Any] = None,
        code: Optional[Any] = None,
        display: Optional[Any] = None,
        userSelected: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            system=system,
            version=version,
            code=code,
            display=display,
            userSelected=userSelected,
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
        A reference to a code defined by a terminology system.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        system: The identification of the code system that defines the meaning of the symbol
            in the code.

        version: The version of the code system which was used when choosing this code. Note
            that a well-maintained code system does not need the version reported, because
            the meaning of codes is consistent across versions. However this cannot
            consistently be assured, and when the meaning is not guaranteed to be
            consistent, the version SHOULD be exchanged.

        code: A symbol in syntax defined by the system. The symbol may be a predefined code
            or an expression in a syntax defined by the coding system (e.g. post-
            coordination).

        display: A representation of the meaning of the code in the system, following the rules
            of the system.

        userSelected: Indicates that this coding was chosen by a user directly - e.g. off a pick
            list of available items (codes or displays).

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

        if (
            max_recursion_limit and nesting_list.count("Coding") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Coding"]
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
                # The identification of the code system that defines the meaning of the symbol
                # in the code.
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
                # The version of the code system which was used when choosing this code. Note
                # that a well-maintained code system does not need the version reported, because
                # the meaning of codes is consistent across versions. However this cannot
                # consistently be assured, and when the meaning is not guaranteed to be
                # consistent, the version SHOULD be exchanged.
                StructField("version", StringType(), True),
                # A symbol in syntax defined by the system. The symbol may be a predefined code
                # or an expression in a syntax defined by the coding system (e.g. post-
                # coordination).
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
                # A representation of the meaning of the code in the system, following the rules
                # of the system.
                StructField("display", StringType(), True),
                # Indicates that this coding was chosen by a user directly - e.g. off a pick
                # list of available items (codes or displays).
                StructField("userSelected", BooleanType(), True),
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