from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    DataType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchTriggerDefinition(AutoMapperDataTypeComplexBase):
    """
    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        name: Optional[Any] = None,
        timingTiming: Optional[Any] = None,
        timingReference: Optional[Any] = None,
        timingDate: Optional[Any] = None,
        timingDateTime: Optional[Any] = None,
        data: Optional[Any] = None,
        condition: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            name=name,
            timingTiming=timingTiming,
            timingReference=timingReference,
            timingDate=timingDate,
            timingDateTime=timingDateTime,
            data=data,
            condition=condition,
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
        A description of a triggering event. Triggering events can be named events,
        data events, or periodic, as determined by the type element.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: The type of triggering event.

        name: A formal name for the event. This may be an absolute URI that identifies the
            event formally (e.g. from a trigger registry), or a simple relative URI that
            identifies the event in a local context.

        timingTiming: The timing of the event (if this is a periodic trigger).

        timingReference: The timing of the event (if this is a periodic trigger).

        timingDate: The timing of the event (if this is a periodic trigger).

        timingDateTime: The timing of the event (if this is a periodic trigger).

        data: The triggering data of the event (if this is a data trigger). If more than one
            data is requirement is specified, then all the data requirements must be true.

        condition: A boolean-valued expression that is evaluated in the context of the container
            of the trigger definition and returns whether or not the trigger fires.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.datarequirement import (
            AutoMapperElasticSearchDataRequirement as DataRequirementSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.expression import (
            AutoMapperElasticSearchExpression as ExpressionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("TriggerDefinition") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TriggerDefinition"]
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
                # The type of triggering event.
                StructField("type", StringType(), True),
                # A formal name for the event. This may be an absolute URI that identifies the
                # event formally (e.g. from a trigger registry), or a simple relative URI that
                # identifies the event in a local context.
                StructField("name", StringType(), True),
                # The timing of the event (if this is a periodic trigger).
                StructField(
                    "timingTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The timing of the event (if this is a periodic trigger).
                StructField(
                    "timingReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The timing of the event (if this is a periodic trigger).
                StructField("timingDate", DateType(), True),
                # The timing of the event (if this is a periodic trigger).
                StructField("timingDateTime", TimestampType(), True),
                # The triggering data of the event (if this is a data trigger). If more than one
                # data is requirement is specified, then all the data requirements must be true.
                StructField(
                    "data",
                    ArrayType(
                        DataRequirementSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A boolean-valued expression that is evaluated in the context of the container
                # of the trigger definition and returns whether or not the trigger fires.
                StructField(
                    "condition",
                    ExpressionSchema.schema(
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
