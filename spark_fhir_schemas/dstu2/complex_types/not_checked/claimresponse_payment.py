from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ClaimResponse_PaymentSchema:
    """
    This resource provides the adjudication details from the processing of a Claim
    resource.
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
        This resource provides the adjudication details from the processing of a Claim
        resource.


        type: Whether this represents partial or complete payment of the claim.

        adjustment: Adjustment to the payment of this transaction which is not related to
            adjudication of this transaction.

        adjustmentReason: Reason for the payment adjustment.

        date: Estimated payment data.

        amount: Payable less any payment adjustment.

        identifier: Payment identifier.

        """
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.dstu2.complex_types.not_checked.money import MoneySchema
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema

        if (
            max_recursion_limit
            and nesting_list.count("ClaimResponse_Payment") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ClaimResponse_Payment"]
        schema = StructType(
            [
                # Whether this represents partial or complete payment of the claim.
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
                # Adjustment to the payment of this transaction which is not related to
                # adjudication of this transaction.
                StructField(
                    "adjustment",
                    MoneySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Reason for the payment adjustment.
                StructField(
                    "adjustmentReason",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated payment data.
                StructField("date", StringType(), True),
                # Payable less any payment adjustment.
                StructField(
                    "amount",
                    MoneySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Payment identifier.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
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