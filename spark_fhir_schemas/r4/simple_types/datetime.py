from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class dateTime:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A date, date-time or partial date (e.g. just year or year + month).  If hours
        and minutes are specified, a time zone SHALL be populated. The format is a
        union of the schema types gYear, gYearMonth, date and dateTime. Seconds must
        be provided due to schema type constraints but may be zero-filled and may be
        ignored.                 Dates SHALL be valid dates.


        """
        return StringType()
