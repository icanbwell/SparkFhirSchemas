from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class GraphDefinition_CompartmentSchema:
    """
    A formal computable definition of a graph of resources - that is, a coherent
    set of resources that form a graph by following references. The Graph
    Definition resource defines a set and makes rules about the set.
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
        A formal computable definition of a graph of resources - that is, a coherent
        set of resources that form a graph by following references. The Graph
        Definition resource defines a set and makes rules about the set.


        code: Identifies the compartment.

        rule: identical | matching | different | no-rule | custom.

        expression: Custom rule, as a FHIRPath expression.

        description: Documentation for FHIRPath expression.

        """
        if (
            max_recursion_limit
            and nesting_list.count("GraphDefinition_Compartment") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["GraphDefinition_Compartment"]
        schema = StructType(
            [
                # Identifies the compartment.
                StructField("code", StringType(), True),
                # identical | matching | different | no-rule | custom.
                StructField("rule", StringType(), True),
                # Custom rule, as a FHIRPath expression.
                StructField("expression", StringType(), True),
                # Documentation for FHIRPath expression.
                StructField("description", StringType(), True),
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