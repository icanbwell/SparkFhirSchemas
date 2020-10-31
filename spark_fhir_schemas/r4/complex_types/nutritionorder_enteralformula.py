from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class NutritionOrder_EnteralFormula:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.nutritionorder_administration import NutritionOrder_Administration
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
                    "baseFormulaType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("baseFormulaProductName", StringType(), True),
                StructField(
                    "additiveType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("additiveProductName", StringType(), True),
                StructField(
                    "caloricDensity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "routeofAdministration",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "administration",
                    ArrayType(
                        NutritionOrder_Administration.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "maxVolumeToDeliver",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField("administrationInstruction", StringType(), True),
            ]
        )

        return schema
