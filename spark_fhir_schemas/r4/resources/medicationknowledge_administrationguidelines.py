from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.medicationknowledge_dosage import MedicationKnowledge_Dosage
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.medicationknowledge_patientcharacteristics import MedicationKnowledge_PatientCharacteristics


class MedicationKnowledge_AdministrationGuidelines:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("dosage",ArrayType(MedicationKnowledge_Dosage.get_schema()), True),
                StructField("indicationCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("indicationReference", Reference.get_schema(), True),
                StructField("patientCharacteristics",ArrayType(MedicationKnowledge_PatientCharacteristics.get_schema()), True),]
        )

        return schema
