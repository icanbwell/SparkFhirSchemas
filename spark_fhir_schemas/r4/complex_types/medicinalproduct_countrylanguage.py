from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicinalProduct_CountryLanguage:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
                    "country", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "jurisdiction",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
