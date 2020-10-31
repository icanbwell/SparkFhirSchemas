from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Goal_Target:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The parameter whose value is being tracked, e.g. body weight, blood pressure,
                # or hemoglobin A1c level.
                StructField(
                    "measure", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailRange", Range.get_schema(recursion_depth + 1), True
                ),
                # The target value of the focus to be achieved to signify the fulfillment of the
                # goal, e.g. 150 pounds, 7.0%. Either the high or low or both values of the
                # range can be specified. When a low value is missing, it indicates that the
                # goal is achieved at any focus value at or below the high value. Similarly, if
                # the high value is missing, it indicates that the goal is achieved at any focus
                # value at or above the low value.
                StructField(
                    "detailCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
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
                    "detailRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                # Indicates either the date or the duration after start by which the goal should
                # be met.
                StructField("dueDate", StringType(), True),
                # Indicates either the date or the duration after start by which the goal should
                # be met.
                StructField(
                    "dueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
