from typing import List, Optional, Union
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, DataType, TimestampType

# noinspection PyPep8Naming
class AutoMapperElasticSearchdateTime(AutoMapperDataTypeComplexBase):
    """
    A date, date-time or partial date (e.g. just year or year + month).  If hours
    and minutes are specified, a time zone SHALL be populated. The format is a
    union of the schema types gYear, gYearMonth, date and dateTime. Seconds must
    be provided due to schema type constraints but may be zero-filled and may be
    ignored.                 Dates SHALL be valid dates.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
    ) -> None:
        super().__init__()
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
        A date, date-time or partial date (e.g. just year or year + month).  If hours
        and minutes are specified, a time zone SHALL be populated. The format is a
        union of the schema types gYear, gYearMonth, date and dateTime. Seconds must
        be provided due to schema type constraints but may be zero-filled and may be
        ignored.                 Dates SHALL be valid dates.


        """
        return TimestampType()
