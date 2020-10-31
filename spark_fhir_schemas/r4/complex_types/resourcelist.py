from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ResourceList:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        return StringType()
