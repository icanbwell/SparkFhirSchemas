from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Invoice_LineItem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.invoice_pricecomponent import Invoice_PriceComponent
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
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
                    "sequence", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "chargeItemReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "chargeItemCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "priceComponent",
                    ArrayType(
                        Invoice_PriceComponent.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
