from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.chargeitemdefinition_applicability import ChargeItemDefinition_Applicability
from spark_fhir_schemas.r4.complex_types.chargeitemdefinition_pricecomponent import ChargeItemDefinition_PriceComponent


# noinspection PyPep8Naming
class ChargeItemDefinition_PropertyGroup:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "applicability",
                    ArrayType(ChargeItemDefinition_Applicability.get_schema()),
                    True
                ),
                StructField(
                    "priceComponent",
                    ArrayType(
                        ChargeItemDefinition_PriceComponent.get_schema()
                    ), True
                ),
            ]
        )

        return schema
