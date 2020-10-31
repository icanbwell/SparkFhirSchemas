from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class decimal:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A rational number with implicit precision


        """
        return IntegerType()
