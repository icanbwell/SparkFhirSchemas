from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SubstancePolymer_RepeatUnit:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substanceamount import SubstanceAmount
        from spark_fhir_schemas.r4.complex_types.substancepolymer_degreeofpolymerisation import SubstancePolymer_DegreeOfPolymerisation
        from spark_fhir_schemas.r4.complex_types.substancepolymer_structuralrepresentation import SubstancePolymer_StructuralRepresentation
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
                    "orientationOfPolymerisation",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("repeatUnit", StringType(), True),
                StructField(
                    "amount", SubstanceAmount.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "degreeOfPolymerisation",
                    ArrayType(
                        SubstancePolymer_DegreeOfPolymerisation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "structuralRepresentation",
                    ArrayType(
                        SubstancePolymer_StructuralRepresentation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
