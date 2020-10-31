from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicinalProductIngredient_Strength:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.medicinalproductingredient_referencestrength import MedicinalProductIngredient_ReferenceStrength
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
                    "presentation", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "presentationLowLimit",
                    Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "concentration", Ratio.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "concentrationLowLimit",
                    Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField("measurementPoint", StringType(), True),
                StructField(
                    "country",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "referenceStrength",
                    ArrayType(
                        MedicinalProductIngredient_ReferenceStrength.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
