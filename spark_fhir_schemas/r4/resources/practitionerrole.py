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
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.contactpoint import ContactPoint
from spark_fhir_schemas.r4.resources.practitionerrole_availabletime import PractitionerRole_AvailableTime
from spark_fhir_schemas.r4.resources.practitionerrole_notavailable import PractitionerRole_NotAvailable
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference


class PractitionerRole:
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
                StructField("active", BooleanType(), True),
                StructField("period", Period.get_schema(), True),
                StructField("practitioner", Reference.get_schema(), True),
                StructField("organization", Reference.get_schema(), True),
                StructField("code",ArrayType(CodeableConcept.get_schema()), True),
                StructField("specialty",ArrayType(CodeableConcept.get_schema()), True),
                StructField("location",ArrayType(Reference.get_schema()), True),
                StructField("healthcareService",ArrayType(Reference.get_schema()), True),
                StructField("telecom",ArrayType(ContactPoint.get_schema()), True),
                StructField("availableTime",ArrayType(PractitionerRole_AvailableTime.get_schema()), True),
                StructField("notAvailable",ArrayType(PractitionerRole_NotAvailable.get_schema()), True),
                StructField("availabilityExceptions", StringType(), True),
                StructField("endpoint",ArrayType(Reference.get_schema()), True),]
        )

        return schema
