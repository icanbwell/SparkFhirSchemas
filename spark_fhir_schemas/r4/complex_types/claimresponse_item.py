from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ClaimResponse_Item:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.claimresponse_adjudication import ClaimResponse_Adjudication
        from spark_fhir_schemas.r4.complex_types.claimresponse_detail import ClaimResponse_Detail
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
                    "itemSequence",
                    positiveInt.get_schema(recursion_depth + 1), True
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
                    "detail",
                    ArrayType(
                        ClaimResponse_Detail.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
