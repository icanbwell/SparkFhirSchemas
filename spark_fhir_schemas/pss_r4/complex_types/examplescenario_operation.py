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
class AutoMapperElasticSearchExampleScenario_Operation(AutoMapperDataTypeComplexBase):
    """
    Example of workflow instance.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        number: Optional[Any] = None,
        type_: Optional[Any] = None,
        name: Optional[Any] = None,
        initiator: Optional[Any] = None,
        receiver: Optional[Any] = None,
        description: Optional[Any] = None,
        initiatorActive: Optional[Any] = None,
        receiverActive: Optional[Any] = None,
        request: Optional[Any] = None,
        response: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            number=number,
            type_=type_,
            name=name,
            initiator=initiator,
            receiver=receiver,
            description=description,
            initiatorActive=initiatorActive,
            receiverActive=receiverActive,
            request=request,
            response=response,
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
        Example of workflow instance.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        number: The sequential number of the interaction, e.g. 1.2.5.

        type: The type of operation - CRUD.

        name: The human-friendly name of the interaction.

        initiator: Who starts the transaction.

        receiver: Who receives the transaction.

        description: A comment to be inserted in the diagram.

        initiatorActive: Whether the initiator is deactivated right after the transaction.

        receiverActive: Whether the receiver is deactivated right after the transaction.

        request: Each resource instance used by the initiator.

        response: Each resource instance used by the responder.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.examplescenario_containedinstance import (
            AutoMapperElasticSearchExampleScenario_ContainedInstance as ExampleScenario_ContainedInstanceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ExampleScenario_Operation") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ExampleScenario_Operation"]
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
                # The sequential number of the interaction, e.g. 1.2.5.
                StructField("number", StringType(), True),
                # The type of operation - CRUD.
                StructField("type", StringType(), True),
                # The human-friendly name of the interaction.
                StructField("name", StringType(), True),
                # Who starts the transaction.
                StructField("initiator", StringType(), True),
                # Who receives the transaction.
                StructField("receiver", StringType(), True),
                # A comment to be inserted in the diagram.
                StructField(
                    "description",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Whether the initiator is deactivated right after the transaction.
                StructField("initiatorActive", BooleanType(), True),
                # Whether the receiver is deactivated right after the transaction.
                StructField("receiverActive", BooleanType(), True),
                # Each resource instance used by the initiator.
                StructField(
                    "request",
                    ExampleScenario_ContainedInstanceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Each resource instance used by the responder.
                StructField(
                    "response",
                    ExampleScenario_ContainedInstanceSchema.schema(
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
