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
class AutoMapperElasticSearchElementDefinition_Slicing(AutoMapperDataTypeComplexBase):
    """
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        discriminator: Optional[Any] = None,
        description: Optional[Any] = None,
        ordered: Optional[Any] = None,
        rules: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            discriminator=discriminator,
            description=description,
            ordered=ordered,
            rules=rules,
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
        Captures constraints on each element within the resource, profile, or
        extension.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        discriminator: Designates which child elements are used to discriminate between the slices
            when processing an instance. If one or more discriminators are provided, the
            value of the child elements in the instance data SHALL completely distinguish
            which slice the element in the resource matches based on the allowed values
            for those elements in each of the slices.

        description: A human-readable text description of how the slicing works. If there is no
            discriminator, this is required to be present to provide whatever information
            is possible about how the slices can be differentiated.

        ordered: If the matching elements have to occur in the same order as defined in the
            profile.

        rules: Whether additional slices are allowed or not. When the slices are ordered,
            profile authors can also say that additional slices are only allowed at the
            end.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.elementdefinition_discriminator import (
            AutoMapperElasticSearchElementDefinition_Discriminator as ElementDefinition_DiscriminatorSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ElementDefinition_Slicing") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ElementDefinition_Slicing"]
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
                # Designates which child elements are used to discriminate between the slices
                # when processing an instance. If one or more discriminators are provided, the
                # value of the child elements in the instance data SHALL completely distinguish
                # which slice the element in the resource matches based on the allowed values
                # for those elements in each of the slices.
                StructField(
                    "discriminator",
                    ArrayType(
                        ElementDefinition_DiscriminatorSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A human-readable text description of how the slicing works. If there is no
                # discriminator, this is required to be present to provide whatever information
                # is possible about how the slices can be differentiated.
                StructField("description", StringType(), True),
                # If the matching elements have to occur in the same order as defined in the
                # profile.
                StructField("ordered", BooleanType(), True),
                # Whether additional slices are allowed or not. When the slices are ordered,
                # profile authors can also say that additional slices are only allowed at the
                # end.
                StructField("rules", StringType(), True),
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