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
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.date import date
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.immunization_performer import Immunization_Performer
from spark_fhir_schemas.r4.resources.annotation import Annotation
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.immunization_education import Immunization_Education
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.immunization_reaction import Immunization_Reaction
from spark_fhir_schemas.r4.resources.immunization_protocolapplied import Immunization_ProtocolApplied


class Immunization:
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
                StructField("status", code.get_schema(), True),
                StructField("statusReason", CodeableConcept.get_schema(), True),
                StructField("vaccineCode", CodeableConcept.get_schema(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("occurrenceDateTime", StringType(), True),
                StructField("occurrenceString", StringType(), True),
                StructField("recorded", dateTime.get_schema(), True),
                StructField("primarySource", BooleanType(), True),
                StructField("reportOrigin", CodeableConcept.get_schema(), True),
                StructField("location", Reference.get_schema(), True),
                StructField("manufacturer", Reference.get_schema(), True),
                StructField("lotNumber", StringType(), True),
                StructField("expirationDate", DateType(), True),
                StructField("site", CodeableConcept.get_schema(), True),
                StructField("route", CodeableConcept.get_schema(), True),
                StructField("doseQuantity", Quantity.get_schema(), True),
                StructField("performer",ArrayType(Immunization_Performer.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("reasonCode",ArrayType(CodeableConcept.get_schema()), True),
                StructField("reasonReference",ArrayType(Reference.get_schema()), True),
                StructField("isSubpotent", BooleanType(), True),
                StructField("subpotentReason",ArrayType(CodeableConcept.get_schema()), True),
                StructField("education",ArrayType(Immunization_Education.get_schema()), True),
                StructField("programEligibility",ArrayType(CodeableConcept.get_schema()), True),
                StructField("fundingSource", CodeableConcept.get_schema(), True),
                StructField("reaction",ArrayType(Immunization_Reaction.get_schema()), True),
                StructField("protocolApplied",ArrayType(Immunization_ProtocolApplied.get_schema()), True),]
        )

        return schema
