from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicationKnowledge_Regulatory:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_substitution import MedicationKnowledge_Substitution
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_schedule import MedicationKnowledge_Schedule
        from spark_fhir_schemas.r4.complex_types.medicationknowledge_maxdispense import MedicationKnowledge_MaxDispense
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
                    "regulatoryAuthority",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "substitution",
                    ArrayType(
                        MedicationKnowledge_Substitution.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "schedule",
                    ArrayType(
                        MedicationKnowledge_Schedule.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "maxDispense",
                    MedicationKnowledge_MaxDispense.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
