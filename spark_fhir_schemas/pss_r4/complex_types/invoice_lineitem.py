from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchInvoice_LineItem(AutoMapperDataTypeComplexBase):
    """
    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        sequence: Optional[Any] = None,
        chargeItemReference: Optional[Any] = None,
        chargeItemCodeableConcept: Optional[Any] = None,
        priceComponent: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            chargeItemReference=chargeItemReference,
            chargeItemCodeableConcept=chargeItemCodeableConcept,
            priceComponent=priceComponent,
        )
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
        Invoice containing collected ChargeItems from an Account with calculated
        individual and total price for Billing purpose.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        sequence: Sequence in which the items appear on the invoice.

        chargeItemReference: The ChargeItem contains information such as the billing code, date, amount
            etc. If no further details are required for the lineItem, inline billing codes
            can be added using the CodeableConcept data type instead of the Reference.

        chargeItemCodeableConcept: The ChargeItem contains information such as the billing code, date, amount
            etc. If no further details are required for the lineItem, inline billing codes
            can be added using the CodeableConcept data type instead of the Reference.

        priceComponent: The price for a ChargeItem may be calculated as a base price with
            surcharges/deductions that apply in certain conditions. A ChargeItemDefinition
            resource that defines the prices, factors and conditions that apply to a
            billing code is currently under development. The priceComponent element can be
            used to offer transparency to the recipient of the Invoice as to how the
            prices have been calculated.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.positiveint import (
            AutoMapperElasticSearchpositiveInt as positiveIntSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.invoice_pricecomponent import (
            AutoMapperElasticSearchInvoice_PriceComponent as Invoice_PriceComponentSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Invoice_LineItem") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Invoice_LineItem"]
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Sequence in which the items appear on the invoice.
                StructField(
                    "sequence",
                    positiveIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The ChargeItem contains information such as the billing code, date, amount
                # etc. If no further details are required for the lineItem, inline billing codes
                # can be added using the CodeableConcept data type instead of the Reference.
                StructField(
                    "chargeItemReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The ChargeItem contains information such as the billing code, date, amount
                # etc. If no further details are required for the lineItem, inline billing codes
                # can be added using the CodeableConcept data type instead of the Reference.
                StructField(
                    "chargeItemCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The price for a ChargeItem may be calculated as a base price with
                # surcharges/deductions that apply in certain conditions. A ChargeItemDefinition
                # resource that defines the prices, factors and conditions that apply to a
                # billing code is currently under development. The priceComponent element can be
                # used to offer transparency to the recipient of the Invoice as to how the
                # prices have been calculated.
                StructField(
                    "priceComponent",
                    ArrayType(
                        Invoice_PriceComponentSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
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