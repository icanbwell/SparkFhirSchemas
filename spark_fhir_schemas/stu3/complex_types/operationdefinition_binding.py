from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class OperationDefinition_BindingSchema:
    """
    A formal computable definition of an operation (on the RESTful interface) or a
    named query (using the search interaction).
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        A formal computable definition of an operation (on the RESTful interface) or a
        named query (using the search interaction).


        strength: Indicates the degree of conformance expectations associated with this binding
            - that is, the degree to which the provided value set must be adhered to in
            the instances.

        valueSetUri: Points to the value set or external definition (e.g. implicit value set) that
            identifies the set of codes to be used.

        valueSetReference: Points to the value set or external definition (e.g. implicit value set) that
            identifies the set of codes to be used.

        """
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        if (
            max_recursion_limit
            and nesting_list.count("OperationDefinition_Binding") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "OperationDefinition_Binding"
        ]
        schema = StructType(
            [
                # Indicates the degree of conformance expectations associated with this binding
                # - that is, the degree to which the provided value set must be adhered to in
                # the instances.
                StructField("strength", StringType(), True),
                # Points to the value set or external definition (e.g. implicit value set) that
                # identifies the set of codes to be used.
                StructField("valueSetUri", StringType(), True),
                # Points to the value set or external definition (e.g. implicit value set) that
                # identifies the set of codes to be used.
                StructField(
                    "valueSetReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema