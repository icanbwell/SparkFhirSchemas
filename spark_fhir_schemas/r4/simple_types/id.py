from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class id:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Any combination of letters, numerals, "-" and ".", with a length limit of 64
        characters.  (This might be an integer, an unprefixed OID, UUID or any other
        identifier pattern that meets these constraints.)  Ids are case-insensitive.


        """
        return StringType()
