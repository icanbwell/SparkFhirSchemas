from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SampledData:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A series of measurements taken by a device, with upper and lower limits. There
        may be more than one dimension in the data.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        origin: The base quantity that a measured value of zero represents. In addition, this
            provides the units of the entire measurement series.

        period: The length of time between sampling times, measured in milliseconds.

        factor: A correction factor that is applied to the sampled data points before they are
            added to the origin.

        lowerLimit: The lower limit of detection of the measured points. This is needed if any of
            the data points have the value "L" (lower than detection limit).

        upperLimit: The upper limit of detection of the measured points. This is needed if any of
            the data points have the value "U" (higher than detection limit).

        dimensions: The number of sample points at each time point. If this value is greater than
            one, then the dimensions will be interlaced - all the sample points for a
            point in time will be recorded at once.

        data: A series of data points which are decimal values separated by a single space
            (character u20). The special values "E" (error), "L" (below detection limit)
            and "U" (above detection limit) can also be used in place of a decimal value.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
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
                # The base quantity that a measured value of zero represents. In addition, this
                # provides the units of the entire measurement series.
                StructField(
                    "origin", Quantity.get_schema(recursion_depth + 1), True
                ),
                # The length of time between sampling times, measured in milliseconds.
                StructField(
                    "period", decimal.get_schema(recursion_depth + 1), True
                ),
                # A correction factor that is applied to the sampled data points before they are
                # added to the origin.
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                # The lower limit of detection of the measured points. This is needed if any of
                # the data points have the value "L" (lower than detection limit).
                StructField(
                    "lowerLimit", decimal.get_schema(recursion_depth + 1), True
                ),
                # The upper limit of detection of the measured points. This is needed if any of
                # the data points have the value "U" (higher than detection limit).
                StructField(
                    "upperLimit", decimal.get_schema(recursion_depth + 1), True
                ),
                # The number of sample points at each time point. If this value is greater than
                # one, then the dimensions will be interlaced - all the sample points for a
                # point in time will be recorded at once.
                StructField(
                    "dimensions", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                # A series of data points which are decimal values separated by a single space
                # (character u20). The special values "E" (error), "L" (below detection limit)
                # and "U" (above detection limit) can also be used in place of a decimal value.
                StructField("data", StringType(), True),
            ]
        )
        return schema
