from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Encounter_Hospitalization:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                    "preAdmissionIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "origin", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "admitSource",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "reAdmission",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dietPreference",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "specialCourtesy",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "specialArrangement",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "destination", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "dischargeDisposition",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
