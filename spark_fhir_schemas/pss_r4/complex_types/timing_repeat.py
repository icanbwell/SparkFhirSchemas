from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchTiming_Repeat(AutoMapperDataTypeComplexBase):
    """
    Specifies an event that may occur multiple times. Timing schedules are used to
    record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        boundsDuration: Optional[Any] = None,
        boundsRange: Optional[Any] = None,
        boundsPeriod: Optional[Any] = None,
        count: Optional[Any] = None,
        countMax: Optional[Any] = None,
        duration: Optional[Any] = None,
        durationMax: Optional[Any] = None,
        durationUnit: Optional[Any] = None,
        frequency: Optional[Any] = None,
        frequencyMax: Optional[Any] = None,
        period: Optional[Any] = None,
        periodMax: Optional[Any] = None,
        periodUnit: Optional[Any] = None,
        dayOfWeek: Optional[Any] = None,
        timeOfDay: Optional[Any] = None,
        when: Optional[Any] = None,
        offset: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            boundsDuration=boundsDuration,
            boundsRange=boundsRange,
            boundsPeriod=boundsPeriod,
            count=count,
            countMax=countMax,
            duration=duration,
            durationMax=durationMax,
            durationUnit=durationUnit,
            frequency=frequency,
            frequencyMax=frequencyMax,
            period=period,
            periodMax=periodMax,
            periodUnit=periodUnit,
            dayOfWeek=dayOfWeek,
            timeOfDay=timeOfDay,
            when=when,
            offset=offset,
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
        Specifies an event that may occur multiple times. Timing schedules are used to
        record when things are planned, expected or requested to occur. The most
        common usage is in dosage instructions for medications. They are also used
        when planning care of various kinds, and may be used for reporting the
        schedule to which past regular activities were carried out.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        boundsDuration: Either a duration for the length of the timing schedule, a range of possible
            length, or outer bounds for start and/or end limits of the timing schedule.

        boundsRange: Either a duration for the length of the timing schedule, a range of possible
            length, or outer bounds for start and/or end limits of the timing schedule.

        boundsPeriod: Either a duration for the length of the timing schedule, a range of possible
            length, or outer bounds for start and/or end limits of the timing schedule.

        count: A total count of the desired number of repetitions across the duration of the
            entire timing specification. If countMax is present, this element indicates
            the lower bound of the allowed range of count values.

        countMax: If present, indicates that the count is a range - so to perform the action
            between [count] and [countMax] times.

        duration: How long this thing happens for when it happens. If durationMax is present,
            this element indicates the lower bound of the allowed range of the duration.

        durationMax: If present, indicates that the duration is a range - so to perform the action
            between [duration] and [durationMax] time length.

        durationUnit: The units of time for the duration, in UCUM units.

        frequency: The number of times to repeat the action within the specified period. If
            frequencyMax is present, this element indicates the lower bound of the allowed
            range of the frequency.

        frequencyMax: If present, indicates that the frequency is a range - so to repeat between
            [frequency] and [frequencyMax] times within the period or period range.

        period: Indicates the duration of time over which repetitions are to occur; e.g. to
            express "3 times per day", 3 would be the frequency and "1 day" would be the
            period. If periodMax is present, this element indicates the lower bound of the
            allowed range of the period length.

        periodMax: If present, indicates that the period is a range from [period] to [periodMax],
            allowing expressing concepts such as "do this once every 3-5 days.

        periodUnit: The units of time for the period in UCUM units.

        dayOfWeek: If one or more days of week is provided, then the action happens only on the
            specified day(s).

        timeOfDay: Specified time of day for action to take place.

        when: An approximate time period during the day, potentially linked to an event of
            daily living that indicates when the action should occur.

        offset: The number of minutes from the event. If the event code does not indicate
            whether the minutes is before or after the event, then the offset is assumed
            to be after the event.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.positiveint import (
            AutoMapperElasticSearchpositiveInt as positiveIntSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.decimal import (
            AutoMapperElasticSearchdecimal as decimalSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.time import (
            AutoMapperElasticSearchtime as timeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Timing_Repeat") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Timing_Repeat"]
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
                # Either a duration for the length of the timing schedule, a range of possible
                # length, or outer bounds for start and/or end limits of the timing schedule.
                StructField(
                    "boundsDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Either a duration for the length of the timing schedule, a range of possible
                # length, or outer bounds for start and/or end limits of the timing schedule.
                StructField(
                    "boundsRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Either a duration for the length of the timing schedule, a range of possible
                # length, or outer bounds for start and/or end limits of the timing schedule.
                StructField(
                    "boundsPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A total count of the desired number of repetitions across the duration of the
                # entire timing specification. If countMax is present, this element indicates
                # the lower bound of the allowed range of count values.
                StructField(
                    "count",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If present, indicates that the count is a range - so to perform the action
                # between [count] and [countMax] times.
                StructField(
                    "countMax",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # How long this thing happens for when it happens. If durationMax is present,
                # this element indicates the lower bound of the allowed range of the duration.
                StructField(
                    "duration",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If present, indicates that the duration is a range - so to perform the action
                # between [duration] and [durationMax] time length.
                StructField(
                    "durationMax",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The units of time for the duration, in UCUM units.
                StructField("durationUnit", StringType(), True),
                # The number of times to repeat the action within the specified period. If
                # frequencyMax is present, this element indicates the lower bound of the allowed
                # range of the frequency.
                StructField(
                    "frequency",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If present, indicates that the frequency is a range - so to repeat between
                # [frequency] and [frequencyMax] times within the period or period range.
                StructField(
                    "frequencyMax",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the duration of time over which repetitions are to occur; e.g. to
                # express "3 times per day", 3 would be the frequency and "1 day" would be the
                # period. If periodMax is present, this element indicates the lower bound of the
                # allowed range of the period length.
                StructField(
                    "period",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If present, indicates that the period is a range from [period] to [periodMax],
                # allowing expressing concepts such as "do this once every 3-5 days.
                StructField(
                    "periodMax",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The units of time for the period in UCUM units.
                StructField("periodUnit", StringType(), True),
                # If one or more days of week is provided, then the action happens only on the
                # specified day(s).
                StructField(
                    "dayOfWeek",
                    ArrayType(
                        codeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Specified time of day for action to take place.
                StructField(
                    "timeOfDay",
                    ArrayType(
                        timeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An approximate time period during the day, potentially linked to an event of
                # daily living that indicates when the action should occur.
                # The number of minutes from the event. If the event code does not indicate
                # whether the minutes is before or after the event, then the offset is assumed
                # to be after the event.
                StructField(
                    "offset",
                    unsignedIntSchema.schema(
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
