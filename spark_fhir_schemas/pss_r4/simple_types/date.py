from typing import List, Optional, Union
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, DateType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchdate(AutoMapperDataTypeComplexBase):
    """
    A date or partial date (e.g. just year or year + month). There is no time
    zone. The format is a union of the schema types gYear, gYearMonth and date.
    Dates SHALL be valid dates.
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
        A date or partial date (e.g. just year or year + month). There is no time
        zone. The format is a union of the schema types gYear, gYearMonth and date.
        Dates SHALL be valid dates.


        """
        return DateType()
