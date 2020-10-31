from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.consent_policy import Consent_Policy
from spark_fhir_schemas.r4.complex_types.consent_verification import Consent_Verification
from spark_fhir_schemas.r4.complex_types.consent_provision import Consent_Provision


# noinspection PyPep8Naming
class Consent:
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
                StructField("status", StringType(), True),
                StructField("scope", CodeableConcept.get_schema(), True),
                StructField(
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("patient", Reference.get_schema(), True),
                StructField("dateTime", dateTime.get_schema(), True),
                StructField(
                    "performer", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "organization", ArrayType(Reference.get_schema()), True
                ),
                StructField("sourceAttachment", Attachment.get_schema(), True),
                StructField("sourceReference", Reference.get_schema(), True),
                StructField(
                    "policy", ArrayType(Consent_Policy.get_schema()), True
                ),
                StructField("policyRule", CodeableConcept.get_schema(), True),
                StructField(
                    "verification",
                    ArrayType(Consent_Verification.get_schema()), True
                ),
                StructField("provision", Consent_Provision.get_schema(), True),
            ]
        )

        return schema
