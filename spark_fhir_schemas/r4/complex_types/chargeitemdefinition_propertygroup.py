from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ChargeItemDefinition_PropertyGroup:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        applicability: Expressions that describe applicability criteria for the priceComponent.

        priceComponent: The price for a ChargeItem may be calculated as a base price with
            surcharges/deductions that apply in certain conditions. A ChargeItemDefinition
            resource that defines the prices, factors and conditions that apply to a
            billing code is currently under development. The priceComponent element can be
            used to offer transparency to the recipient of the Invoice of how the prices
            have been calculated.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.chargeitemdefinition_applicability import ChargeItemDefinition_Applicability
        from spark_fhir_schemas.r4.complex_types.chargeitemdefinition_pricecomponent import ChargeItemDefinition_PriceComponent
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Expressions that describe applicability criteria for the priceComponent.
                StructField(
                    "applicability",
                    ArrayType(
                        ChargeItemDefinition_Applicability.
                        get_schema(recursion_depth + 1)
                    ), True
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
                        ChargeItemDefinition_PriceComponent.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
