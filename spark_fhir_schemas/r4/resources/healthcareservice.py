from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
from spark_fhir_schemas.r4.complex_types.healthcareservice_eligibility import HealthcareService_Eligibility
from spark_fhir_schemas.r4.complex_types.healthcareservice_availabletime import HealthcareService_AvailableTime
from spark_fhir_schemas.r4.complex_types.healthcareservice_notavailable import HealthcareService_NotAvailable


# noinspection PyPep8Naming
class HealthcareService:
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
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("active", BooleanType(), True),
                StructField("providedBy", Reference.get_schema(), True),
                StructField(
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "type", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "specialty", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "location", ArrayType(Reference.get_schema()), True
                ),
                StructField("name", StringType(), True),
                StructField("comment", StringType(), True),
                StructField("extraDetails", markdown.get_schema(), True),
                StructField("photo", Attachment.get_schema(), True),
                StructField(
                    "telecom", ArrayType(ContactPoint.get_schema()), True
                ),
                StructField(
                    "coverageArea", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "serviceProvisionCode",
                    ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "eligibility",
                    ArrayType(HealthcareService_Eligibility.get_schema()), True
                ),
                StructField(
                    "program", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "characteristic", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "communication", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "referralMethod", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("appointmentRequired", BooleanType(), True),
                StructField(
                    "availableTime",
                    ArrayType(HealthcareService_AvailableTime.get_schema()),
                    True
                ),
                StructField(
                    "notAvailable",
                    ArrayType(HealthcareService_NotAvailable.get_schema()),
                    True
                ),
                StructField("availabilityExceptions", StringType(), True),
                StructField(
                    "endpoint", ArrayType(Reference.get_schema()), True
                ),
            ]
        )

        return schema
