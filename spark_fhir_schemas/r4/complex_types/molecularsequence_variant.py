from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MolecularSequence_Variant:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                    "start", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "end", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("observedAllele", StringType(), True),
                StructField("referenceAllele", StringType(), True),
                StructField("cigar", StringType(), True),
                StructField(
                    "variantPointer",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
