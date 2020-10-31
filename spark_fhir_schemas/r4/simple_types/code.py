from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class code:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A string which has at least one character and no leading or trailing
        whitespace and where there is no whitespace other than single spaces in the
        contents


        """
        return StringType()
