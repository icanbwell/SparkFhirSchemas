from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class unsignedInt:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An integer with a value that is not negative (e.g. >= 0)


        """
        return IntegerType()
