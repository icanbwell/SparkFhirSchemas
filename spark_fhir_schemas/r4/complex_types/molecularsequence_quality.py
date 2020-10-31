from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MolecularSequence_Quality:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.molecularsequence_roc import MolecularSequence_Roc
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
                StructField("type", StringType(), True),
                StructField(
                    "standardSequence",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "start", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "end", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "score", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "method", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "truthTP", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "queryTP", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "truthFN", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "queryFP", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "gtFP", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "precision", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "recall", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fScore", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "roc",
                    MolecularSequence_Roc.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
