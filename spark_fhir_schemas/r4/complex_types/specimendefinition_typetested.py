from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SpecimenDefinition_TypeTested:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.specimendefinition_container import SpecimenDefinition_Container
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.specimendefinition_handling import SpecimenDefinition_Handling
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
                StructField("isDerived", BooleanType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("preference", StringType(), True),
                StructField(
                    "container",
                    SpecimenDefinition_Container.
                    get_schema(recursion_depth + 1), True
                ),
                StructField("requirement", StringType(), True),
                StructField(
                    "retentionTime", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "rejectionCriterion",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "handling",
                    ArrayType(
                        SpecimenDefinition_Handling.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
