from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchChargeItemDefinition_PropertyGroup(
    AutoMapperDataTypeComplexBase
):
    """
    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives only
    a rough structure and requires profiling for each type of billing code system.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        applicability: Optional[Any] = None,
        priceComponent: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            applicability=applicability,
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
        The ChargeItemDefinition resource provides the properties that apply to the
        (billing) codes necessary to calculate costs and prices. The properties may
        differ largely depending on type and realm, therefore this resource gives only
        a rough structure and requires profiling for each type of billing code system.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        applicability: Expressions that describe applicability criteria for the priceComponent.

        priceComponent: The price for a ChargeItem may be calculated as a base price with
            surcharges/deductions that apply in certain conditions. A ChargeItemDefinition
            resource that defines the prices, factors and conditions that apply to a
            billing code is currently under development. The priceComponent element can be
            used to offer transparency to the recipient of the Invoice of how the prices
            have been calculated.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.chargeitemdefinition_applicability import (
            AutoMapperElasticSearchChargeItemDefinition_Applicability as ChargeItemDefinition_ApplicabilitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.chargeitemdefinition_pricecomponent import (
            AutoMapperElasticSearchChargeItemDefinition_PriceComponent as ChargeItemDefinition_PriceComponentSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ChargeItemDefinition_PropertyGroup")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ChargeItemDefinition_PropertyGroup"
        ]
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
                # Expressions that describe applicability criteria for the priceComponent.
                StructField(
                    "applicability",
                    ArrayType(
                        ChargeItemDefinition_ApplicabilitySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The price for a ChargeItem may be calculated as a base price with
                # surcharges/deductions that apply in certain conditions. A ChargeItemDefinition
                # resource that defines the prices, factors and conditions that apply to a
                # billing code is currently under development. The priceComponent element can be
                # used to offer transparency to the recipient of the Invoice of how the prices
                # have been calculated.
                StructField(
                    "priceComponent",
                    ArrayType(
                        ChargeItemDefinition_PriceComponentSchema.schema(
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
