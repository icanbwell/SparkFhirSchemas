from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicinalProductPharmaceutical_RouteOfAdministration:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.medicinalproductpharmaceutical_targetspecies import MedicinalProductPharmaceutical_TargetSpecies
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
                StructField(
                    "firstDose", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "maxSingleDose", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "maxDosePerDay", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "maxDosePerTreatmentPeriod",
                    Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "maxTreatmentPeriod",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "targetSpecies",
                    ArrayType(
                        MedicinalProductPharmaceutical_TargetSpecies.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
