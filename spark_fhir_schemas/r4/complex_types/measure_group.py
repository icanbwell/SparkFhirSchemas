from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Measure_Group:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.measure_population import Measure_Population
        from spark_fhir_schemas.r4.complex_types.measure_stratifier import Measure_Stratifier
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
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "population",
                    ArrayType(
                        Measure_Population.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "stratifier",
                    ArrayType(
                        Measure_Stratifier.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
