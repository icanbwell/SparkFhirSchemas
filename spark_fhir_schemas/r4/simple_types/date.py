from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class date:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A date or partial date (e.g. just year or year + month). There is no time
        zone. The format is a union of the schema types gYear, gYearMonth and date.
        Dates SHALL be valid dates.


        """
        return StringType()
