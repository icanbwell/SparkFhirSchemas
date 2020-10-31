from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicationKnowledge_AdministrationGuidelines:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_dosage import MedicationKnowledge_Dosage
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_patientcharacteristics import MedicationKnowledge_PatientCharacteristics
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
                    "dosage",
                    ArrayType(
                        MedicationKnowledge_Dosage.
                        get_schema(recursion_depth + 1)
                    ), True
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
                    "patientCharacteristics",
                    ArrayType(
                        MedicationKnowledge_PatientCharacteristics.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
