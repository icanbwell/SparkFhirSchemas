from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.medicinalproductcontraindication_othertherapy import MedicinalProductContraindication_OtherTherapy
from spark_fhir_schemas.r4.resources.population import Population


class MedicinalProductContraindication:
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
                StructField("subject",ArrayType(Reference.get_schema()), True),
                StructField("disease", CodeableConcept.get_schema(), True),
                StructField("diseaseStatus", CodeableConcept.get_schema(), True),
                StructField("comorbidity",ArrayType(CodeableConcept.get_schema()), True),
                StructField("therapeuticIndication",ArrayType(Reference.get_schema()), True),
                StructField("otherTherapy",ArrayType(MedicinalProductContraindication_OtherTherapy.get_schema()), True),
                StructField("population",ArrayType(Population.get_schema()), True),]
        )

        return schema
