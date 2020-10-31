from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SpecimenDefinition_Container:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.specimendefinition_additive import SpecimenDefinition_Additive
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
                    "material",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "cap", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "capacity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "minimumVolumeQuantity",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField("minimumVolumeString", StringType(), True),
                StructField(
                    "additive",
                    ArrayType(
                        SpecimenDefinition_Additive.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("preparation", StringType(), True),
            ]
        )

        return schema
