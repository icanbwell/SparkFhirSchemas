from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ElementDefinition_MappingSchema:
    """
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
        """
        Captures constraints on each element within the resource, profile, or
        extension.


        identity: An internal reference to the definition of a mapping.

        language: Identifies the computable language in which mapping.map is expressed.

        map: Expresses what part of the target specification corresponds to this element.

        comment: Comments that provide information about the mapping or its use.

        """
        if (
            max_recursion_limit
            and nesting_list.count("ElementDefinition_Mapping") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ElementDefinition_Mapping"]
        schema = StructType(
            [
                # An internal reference to the definition of a mapping.
                StructField("identity", StringType(), True),
                # Identifies the computable language in which mapping.map is expressed.
                StructField("language", StringType(), True),
                # Expresses what part of the target specification corresponds to this element.
                StructField("map", StringType(), True),
                # Comments that provide information about the mapping or its use.
                StructField("comment", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema