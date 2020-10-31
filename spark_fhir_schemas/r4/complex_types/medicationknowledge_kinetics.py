from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicationKnowledge_Kinetics:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.duration import Duration
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
                    "areaUnderCurve",
                    ArrayType(Quantity.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "lethalDose50",
                    ArrayType(Quantity.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "halfLifePeriod", Duration.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
