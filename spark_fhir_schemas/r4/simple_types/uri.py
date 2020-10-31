from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class uri:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        String of characters used to identify a name or a resource


        """
        return StringType()
