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
    IntegerType,
    DataType,
    FloatType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchValueSet_Parameter(AutoMapperDataTypeComplexBase):
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
        name: Optional[Any] = None,
        valueString: Optional[Any] = None,
        valueBoolean: Optional[Any] = None,
        valueInteger: Optional[Any] = None,
        valueDecimal: Optional[Any] = None,
        valueUri: Optional[Any] = None,
        valueCode: Optional[Any] = None,
        valueDateTime: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            name=name,
            valueString=valueString,
            valueBoolean=valueBoolean,
            valueInteger=valueInteger,
            valueDecimal=valueDecimal,
            valueUri=valueUri,
            valueCode=valueCode,
            valueDateTime=valueDateTime,
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

        name: Name of the input parameter to the $expand operation; may be a server-assigned
            name for additional default or other server-supplied parameters used to
            control the expansion process.

        valueString: The value of the parameter.

        valueBoolean: The value of the parameter.

        valueInteger: The value of the parameter.

        valueDecimal: The value of the parameter.

        valueUri: The value of the parameter.

        valueCode: The value of the parameter.

        valueDateTime: The value of the parameter.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ValueSet_Parameter") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ValueSet_Parameter"]
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
                # Name of the input parameter to the $expand operation; may be a server-assigned
                # name for additional default or other server-supplied parameters used to
                # control the expansion process.
                StructField("name", StringType(), True),
                # The value of the parameter.
                StructField("valueString", StringType(), True),
                # The value of the parameter.
                StructField("valueBoolean", BooleanType(), True),
                # The value of the parameter.
                StructField("valueInteger", IntegerType(), True),
                # The value of the parameter.
                StructField("valueDecimal", FloatType(), True),
                # The value of the parameter.
                StructField("valueUri", StringType(), True),
                # The value of the parameter.
                StructField("valueCode", StringType(), True),
                # The value of the parameter.
                StructField("valueDateTime", TimestampType(), True),
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