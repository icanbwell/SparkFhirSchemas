from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.marketingstatus import MarketingStatus
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.medicinalproduct_name import MedicinalProduct_Name
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.medicinalproduct_manufacturingbusinessoperation import MedicinalProduct_ManufacturingBusinessOperation
from spark_fhir_schemas.r4.resources.medicinalproduct_specialdesignation import MedicinalProduct_SpecialDesignation


class MedicinalProduct:
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
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("domain", Coding.get_schema(), True),
                StructField("combinedPharmaceuticalDoseForm", CodeableConcept.get_schema(), True),
                StructField("legalStatusOfSupply", CodeableConcept.get_schema(), True),
                StructField("additionalMonitoringIndicator", CodeableConcept.get_schema(), True),
                StructField("specialMeasures",ArrayType(string.get_schema()), True),
                StructField("paediatricUseIndicator", CodeableConcept.get_schema(), True),
                StructField("productClassification",ArrayType(CodeableConcept.get_schema()), True),
                StructField("marketingStatus",ArrayType(MarketingStatus.get_schema()), True),
                StructField("pharmaceuticalProduct",ArrayType(Reference.get_schema()), True),
                StructField("packagedMedicinalProduct",ArrayType(Reference.get_schema()), True),
                StructField("attachedDocument",ArrayType(Reference.get_schema()), True),
                StructField("masterFile",ArrayType(Reference.get_schema()), True),
                StructField("contact",ArrayType(Reference.get_schema()), True),
                StructField("clinicalTrial",ArrayType(Reference.get_schema()), True),
                StructField("name",ArrayType(MedicinalProduct_Name.get_schema()), True),
                StructField("crossReference",ArrayType(Identifier.get_schema()), True),
                StructField("manufacturingBusinessOperation",ArrayType(MedicinalProduct_ManufacturingBusinessOperation.get_schema()), True),
                StructField("specialDesignation",ArrayType(MedicinalProduct_SpecialDesignation.get_schema()), True),]
        )

        return schema
