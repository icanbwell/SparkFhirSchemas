from typing import List, Optional, Union
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StringType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchcode(AutoMapperDataTypeComplexBase):
    """
    A string which has at least one character and no leading or trailing
    whitespace and where there is no whitespace other than single spaces in the
    contents
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
        A string which has at least one character and no leading or trailing
        whitespace and where there is no whitespace other than single spaces in the
        contents


        """
        return StringType()
