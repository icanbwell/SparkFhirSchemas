from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class NutritionOrder_SupplementSchema:
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
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
        A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.


        type: The kind of nutritional supplement product required such as a high protein or
            pediatric clear liquid supplement.

        productName: The product or brand name of the nutritional supplement such as "Acme Protein
            Shake".

        schedule: The time period and frequency at which the supplement(s) should be given.  The
            supplement should be given for the combination of all schedules if more than
            one schedule is present.

        quantity: The amount of the nutritional supplement to be given.

        instruction: Free text or additional instructions or information pertaining to the oral
            supplement.

        """
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.dstu2.complex_types.not_checked.timing import TimingSchema
        from spark_fhir_schemas.dstu2.complex_types.not_checked.quantity import QuantitySchema

        if (
            max_recursion_limit
            and nesting_list.count("NutritionOrder_Supplement") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["NutritionOrder_Supplement"]
        schema = StructType(
            [
                # The kind of nutritional supplement product required such as a high protein or
                # pediatric clear liquid supplement.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The product or brand name of the nutritional supplement such as "Acme Protein
                # Shake".
                StructField("productName", StringType(), True),
                # The time period and frequency at which the supplement(s) should be given.  The
                # supplement should be given for the combination of all schedules if more than
                # one schedule is present.
                StructField(
                    "schedule",
                    ArrayType(
                        TimingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The amount of the nutritional supplement to be given.
                StructField(
                    "quantity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Free text or additional instructions or information pertaining to the oral
                # supplement.
                StructField("instruction", StringType(), True),
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