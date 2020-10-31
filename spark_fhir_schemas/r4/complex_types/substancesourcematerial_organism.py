from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SubstanceSourceMaterial_Organism:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_author import SubstanceSourceMaterial_Author
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_hybrid import SubstanceSourceMaterial_Hybrid
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_organismgeneral import SubstanceSourceMaterial_OrganismGeneral
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
                    "family", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "genus", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "species", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "intraspecificType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("intraspecificDescription", StringType(), True),
                StructField(
                    "author",
                    ArrayType(
                        SubstanceSourceMaterial_Author.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "hybrid",
                    SubstanceSourceMaterial_Hybrid.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "organismGeneral",
                    SubstanceSourceMaterial_OrganismGeneral.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
