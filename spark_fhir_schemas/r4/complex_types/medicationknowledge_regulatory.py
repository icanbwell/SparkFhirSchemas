from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.medicationknowledge_substitution import MedicationKnowledge_Substitution
from spark_fhir_schemas.r4.complex_types.medicationknowledge_schedule import MedicationKnowledge_Schedule
from spark_fhir_schemas.r4.complex_types.medicationknowledge_maxdispense import MedicationKnowledge_MaxDispense


# noinspection PyPep8Naming
class MedicationKnowledge_Regulatory:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "regulatoryAuthority", Reference.get_schema(), True
                ),
                StructField(
                    "substitution",
                    ArrayType(MedicationKnowledge_Substitution.get_schema()),
                    True
                ),
                StructField(
                    "schedule",
                    ArrayType(MedicationKnowledge_Schedule.get_schema()), True
                ),
                StructField(
                    "maxDispense",
                    MedicationKnowledge_MaxDispense.get_schema(), True
                ),
            ]
        )

        return schema
