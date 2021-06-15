from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSampledData(AutoMapperDataTypeComplexBase):
    """
    A series of measurements taken by a device, with upper and lower limits. There
    may be more than one dimension in the data.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        origin: Optional[Any] = None,
        period: Optional[Any] = None,
        factor: Optional[Any] = None,
        lowerLimit: Optional[Any] = None,
        upperLimit: Optional[Any] = None,
        dimensions: Optional[Any] = None,
        data: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            origin=origin,
            period=period,
            factor=factor,
            lowerLimit=lowerLimit,
            upperLimit=upperLimit,
            dimensions=dimensions,
            data=data,
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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.decimal import (
            AutoMapperElasticSearchdecimal as decimalSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.positiveint import (
            AutoMapperElasticSearchpositiveInt as positiveIntSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SampledData") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SampledData"]
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
                # The base quantity that a measured value of zero represents. In addition, this
                # provides the units of the entire measurement series.
                StructField(
                    "origin",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The length of time between sampling times, measured in milliseconds.
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
                # A correction factor that is applied to the sampled data points before they are
                # added to the origin.
                StructField(
                    "factor",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The lower limit of detection of the measured points. This is needed if any of
                # the data points have the value "L" (lower than detection limit).
                StructField(
                    "lowerLimit",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The upper limit of detection of the measured points. This is needed if any of
                # the data points have the value "U" (higher than detection limit).
                StructField(
                    "upperLimit",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The number of sample points at each time point. If this value is greater than
                # one, then the dimensions will be interlaced - all the sample points for a
                # point in time will be recorded at once.
                StructField(
                    "dimensions",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A series of data points which are decimal values separated by a single space
                # (character u20). The special values "E" (error), "L" (below detection limit)
                # and "U" (above detection limit) can also be used in place of a decimal value.
                StructField("data", StringType(), True),
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
