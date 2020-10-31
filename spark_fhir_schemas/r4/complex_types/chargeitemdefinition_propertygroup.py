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
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.chargeitemdefinition_applicability import ChargeItemDefinition_Applicability
        from spark_fhir_schemas.r4.complex_types.chargeitemdefinition_pricecomponent import ChargeItemDefinition_PriceComponent
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "applicability",
                    ArrayType(
                        ChargeItemDefinition_Applicability.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
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
