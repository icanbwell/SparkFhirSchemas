from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MolecularSequence_Roc:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
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
                    "score",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "numTP",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "numFP",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "numFN",
                    ArrayType(integer.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "precision",
                    ArrayType(decimal.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "sensitivity",
                    ArrayType(decimal.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "fMeasure",
                    ArrayType(decimal.get_schema(recursion_depth + 1)), True
                ),
            ]
        )

        return schema
