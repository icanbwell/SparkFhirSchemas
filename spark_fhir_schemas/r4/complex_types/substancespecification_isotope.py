from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SubstanceSpecification_Isotope:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.substancespecification_molecularweight import SubstanceSpecification_MolecularWeight
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
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "name", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "substitution",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "halfLife", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "molecularWeight",
                    SubstanceSpecification_MolecularWeight.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
