from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Timing:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        event: Identifies specific times when the event occurs.

        repeat: A set of rules that describe when the event is scheduled.

        code: A code for the timing schedule (or just text in code.text). Some codes such as
            BID are ubiquitous, but many institutions define their own additional codes.
            If a code is provided, the code is understood to be a complete statement of
            whatever is specified in the structured timing data, and either the code or
            the data may be used to interpret the Timing, with the exception that
            .repeat.bounds still applies over the code (and is not contained in the code).

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.timing_repeat import Timing_Repeat
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
                # Identifies specific times when the event occurs.
                StructField(
                    "event",
                    ArrayType(dateTime.get_schema(recursion_depth + 1)), True
                ),
                # A set of rules that describe when the event is scheduled.
                StructField(
                    "repeat", Timing_Repeat.get_schema(recursion_depth + 1),
                    True
                ),
                # A code for the timing schedule (or just text in code.text). Some codes such as
                # BID are ubiquitous, but many institutions define their own additional codes.
                # If a code is provided, the code is understood to be a complete statement of
                # whatever is specified in the structured timing data, and either the code or
                # the data may be used to interpret the Timing, with the exception that
                # .repeat.bounds still applies over the code (and is not contained in the code).
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
