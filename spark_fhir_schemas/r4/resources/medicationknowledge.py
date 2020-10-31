from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.medicationknowledge_relatedmedicationknowledge import MedicationKnowledge_RelatedMedicationKnowledge
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.medicationknowledge_monograph import MedicationKnowledge_Monograph
from spark_fhir_schemas.r4.complex_types.medicationknowledge_ingredient import MedicationKnowledge_Ingredient
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.medicationknowledge_cost import MedicationKnowledge_Cost
from spark_fhir_schemas.r4.complex_types.medicationknowledge_monitoringprogram import MedicationKnowledge_MonitoringProgram
from spark_fhir_schemas.r4.complex_types.medicationknowledge_administrationguidelines import MedicationKnowledge_AdministrationGuidelines
from spark_fhir_schemas.r4.complex_types.medicationknowledge_medicineclassification import MedicationKnowledge_MedicineClassification
from spark_fhir_schemas.r4.complex_types.medicationknowledge_packaging import MedicationKnowledge_Packaging
from spark_fhir_schemas.r4.complex_types.medicationknowledge_drugcharacteristic import MedicationKnowledge_DrugCharacteristic
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.medicationknowledge_regulatory import MedicationKnowledge_Regulatory
from spark_fhir_schemas.r4.complex_types.medicationknowledge_kinetics import MedicationKnowledge_Kinetics


class MedicationKnowledge:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("status", code.get_schema(), True),
                StructField("manufacturer", Reference.get_schema(), True),
                StructField("doseForm", CodeableConcept.get_schema(), True),
                StructField("amount", Quantity.get_schema(), True),
                StructField("synonym",ArrayType(string.get_schema()), True),
                StructField("relatedMedicationKnowledge",ArrayType(MedicationKnowledge_RelatedMedicationKnowledge.get_schema()), True),
                StructField("associatedMedication",ArrayType(Reference.get_schema()), True),
                StructField("productType",ArrayType(CodeableConcept.get_schema()), True),
                StructField("monograph",ArrayType(MedicationKnowledge_Monograph.get_schema()), True),
                StructField("ingredient",ArrayType(MedicationKnowledge_Ingredient.get_schema()), True),
                StructField("preparationInstruction", markdown.get_schema(), True),
                StructField("intendedRoute",ArrayType(CodeableConcept.get_schema()), True),
                StructField("cost",ArrayType(MedicationKnowledge_Cost.get_schema()), True),
                StructField("monitoringProgram",ArrayType(MedicationKnowledge_MonitoringProgram.get_schema()), True),
                StructField("administrationGuidelines",ArrayType(MedicationKnowledge_AdministrationGuidelines.get_schema()), True),
                StructField("medicineClassification",ArrayType(MedicationKnowledge_MedicineClassification.get_schema()), True),
                StructField("packaging", MedicationKnowledge_Packaging.get_schema(), True),
                StructField("drugCharacteristic",ArrayType(MedicationKnowledge_DrugCharacteristic.get_schema()), True),
                StructField("contraindication",ArrayType(Reference.get_schema()), True),
                StructField("regulatory",ArrayType(MedicationKnowledge_Regulatory.get_schema()), True),
                StructField("kinetics",ArrayType(MedicationKnowledge_Kinetics.get_schema()), True),
            ]
        )

        return schema
