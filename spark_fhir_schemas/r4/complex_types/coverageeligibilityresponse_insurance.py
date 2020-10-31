from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class CoverageEligibilityResponse_Insurance:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_item import CoverageEligibilityResponse_Item
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
                    "coverage", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("inforce", BooleanType(), True),
                StructField(
                    "benefitPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "item",
                    ArrayType(
                        CoverageEligibilityResponse_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
