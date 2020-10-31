from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicinalProduct_SpecialDesignation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
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
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "intendedUse",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "indicationCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "indicationReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "species", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
