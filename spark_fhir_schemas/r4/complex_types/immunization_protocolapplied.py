from pyspark.sql.types import ArrayType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Immunization_ProtocolApplied:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
                StructField("series", StringType(), True),
                StructField(
                    "authority", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "targetDisease",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("doseNumberPositiveInt", IntegerType(), True),
                StructField("doseNumberString", StringType(), True),
                StructField("seriesDosesPositiveInt", IntegerType(), True),
                StructField("seriesDosesString", StringType(), True),
            ]
        )

        return schema
