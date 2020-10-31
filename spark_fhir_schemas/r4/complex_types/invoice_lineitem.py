from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.invoice_pricecomponent import Invoice_PriceComponent


# noinspection PyPep8Naming
class Invoice_LineItem:
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
                StructField("sequence", positiveInt.get_schema(), True),
                StructField(
                    "chargeItemReference", Reference.get_schema(), True
                ),
                StructField(
                    "chargeItemCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "priceComponent",
                    ArrayType(Invoice_PriceComponent.get_schema()), True
                ),
            ]
        )

        return schema
