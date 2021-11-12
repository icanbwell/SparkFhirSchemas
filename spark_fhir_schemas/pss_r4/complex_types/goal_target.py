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
    BooleanType,
    IntegerType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchGoal_Target(AutoMapperDataTypeComplexBase):
    """
    Describes the intended objective(s) for a patient, group or organization care,
    for example, weight loss, restoring an activity of daily living, obtaining
    herd immunity via immunization, meeting a process improvement objective, etc.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        measure: Optional[Any] = None,
        detailQuantity: Optional[Any] = None,
        detailRange: Optional[Any] = None,
        detailCodeableConcept: Optional[Any] = None,
        detailString: Optional[Any] = None,
        detailBoolean: Optional[Any] = None,
        detailInteger: Optional[Any] = None,
        detailRatio: Optional[Any] = None,
        dueDate: Optional[Any] = None,
        dueDuration: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            measure=measure,
            detailQuantity=detailQuantity,
            detailRange=detailRange,
            detailCodeableConcept=detailCodeableConcept,
            detailString=detailString,
            detailBoolean=detailBoolean,
            detailInteger=detailInteger,
            detailRatio=detailRatio,
            dueDate=dueDate,
            dueDuration=dueDuration,
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
        Describes the intended objective(s) for a patient, group or organization care,
        for example, weight loss, restoring an activity of daily living, obtaining
        herd immunity via immunization, meeting a process improvement objective, etc.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        measure: The parameter whose value is being tracked, e.g. body weight, blood pressure,
            or hemoglobin A1c level.

        detailQuantity: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailRange: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailCodeableConcept: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailString: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailBoolean: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailInteger: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        detailRatio: The target value of the focus to be achieved to signify the fulfillment of the
            goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
            range can be specified. When a low value is missing, it indicates that the
            goal is achieved at any focus value at or below the high value. Similarly, if
            the high value is missing, it indicates that the goal is achieved at any focus
            value at or above the low value.

        dueDate: Indicates either the date or the duration after start by which the goal should
            be met.

        dueDuration: Indicates either the date or the duration after start by which the goal should
            be met.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Goal_Target") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Goal_Target"]
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
                # The parameter whose value is being tracked, e.g. body weight, blood pressure,
                # or hemoglobin A1c level.
                StructField(
                    "measure",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField("detailString", StringType(), True),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField("detailBoolean", BooleanType(), True),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField("detailInteger", IntegerType(), True),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates either the date or the duration after start by which the goal should
                # be met.
                StructField("dueDate", DateType(), True),
                # Indicates either the date or the duration after start by which the goal should
                # be met.
                StructField(
                    "dueDuration",
                    DurationSchema.schema(
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
