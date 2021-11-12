from typing import List, Optional, Union
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StringType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchid(AutoMapperDataTypeComplexBase):
    """
    Any combination of letters, numerals, "-" and ".", with a length limit of 64
    characters.  (This might be an integer, an unprefixed OID, UUID or any other
    identifier pattern that meets these constraints.)  Ids are case-insensitive.
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
        Any combination of letters, numerals, "-" and ".", with a length limit of 64
        characters.  (This might be an integer, an unprefixed OID, UUID or any other
        identifier pattern that meets these constraints.)  Ids are case-insensitive.


        """
        return StringType()
