from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MeasureReport_Stratum:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.measurereport_component import MeasureReport_Component
        from spark_fhir_schemas.r4.complex_types.measurereport_population1 import MeasureReport_Population1
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
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
                    "value", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "component",
                    ArrayType(
                        MeasureReport_Component.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "population",
                    ArrayType(
                        MeasureReport_Population1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "measureScore", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
