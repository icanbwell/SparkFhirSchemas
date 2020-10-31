from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ClaimResponse_Detail1:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.claimresponse_adjudication import ClaimResponse_Adjudication
        from spark_fhir_schemas.r4.complex_types.claimresponse_subdetail1 import ClaimResponse_SubDetail1
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
                    "productOrService",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "modifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "unitPrice", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "net", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "noteNumber",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "adjudication",
                    ArrayType(
                        ClaimResponse_Adjudication.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "subDetail",
                    ArrayType(
                        ClaimResponse_SubDetail1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
