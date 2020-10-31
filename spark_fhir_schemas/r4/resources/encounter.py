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
from spark_fhir_schemas.r4.resources.encounter_statushistory import Encounter_StatusHistory
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.encounter_classhistory import Encounter_ClassHistory
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.encounter_participant import Encounter_Participant
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.encounter_diagnosis import Encounter_Diagnosis
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.encounter_hospitalization import Encounter_Hospitalization
from spark_fhir_schemas.r4.resources.encounter_location import Encounter_Location
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference


class Encounter:
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
                StructField("status", StringType(), True),
                StructField("statusHistory",ArrayType(Encounter_StatusHistory.get_schema()), True),
                StructField("class", Coding.get_schema(), True),
                StructField("classHistory",ArrayType(Encounter_ClassHistory.get_schema()), True),
                StructField("type",ArrayType(CodeableConcept.get_schema()), True),
                StructField("serviceType", CodeableConcept.get_schema(), True),
                StructField("priority", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("episodeOfCare",ArrayType(Reference.get_schema()), True),
                StructField("basedOn",ArrayType(Reference.get_schema()), True),
                StructField("participant",ArrayType(Encounter_Participant.get_schema()), True),
                StructField("appointment",ArrayType(Reference.get_schema()), True),
                StructField("period", Period.get_schema(), True),
                StructField("length", Duration.get_schema(), True),
                StructField("reasonCode",ArrayType(CodeableConcept.get_schema()), True),
                StructField("reasonReference",ArrayType(Reference.get_schema()), True),
                StructField("diagnosis",ArrayType(Encounter_Diagnosis.get_schema()), True),
                StructField("account",ArrayType(Reference.get_schema()), True),
                StructField("hospitalization", Encounter_Hospitalization.get_schema(), True),
                StructField("location",ArrayType(Encounter_Location.get_schema()), True),
                StructField("serviceProvider", Reference.get_schema(), True),
                StructField("partOf", Reference.get_schema(), True),]
        )

        return schema
