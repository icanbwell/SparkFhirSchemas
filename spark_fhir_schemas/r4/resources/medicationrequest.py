from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

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
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.dosage import Dosage
from spark_fhir_schemas.r4.complex_types.medicationrequest_dispenserequest import MedicationRequest_DispenseRequest
from spark_fhir_schemas.r4.complex_types.medicationrequest_substitution import MedicationRequest_Substitution


# noinspection PyPep8Naming
class MedicationRequest:
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
                StructField("status", code.get_schema(), True),
                StructField(
                    "statusReason", CodeableConcept.get_schema(), True
                ),
                StructField("intent", code.get_schema(), True),
                StructField(
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("priority", code.get_schema(), True),
                StructField("doNotPerform", BooleanType(), True),
                StructField("reportedBoolean", BooleanType(), True),
                StructField("reportedReference", Reference.get_schema(), True),
                StructField(
                    "medicationCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "medicationReference", Reference.get_schema(), True
                ),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField(
                    "supportingInformation", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField("authoredOn", dateTime.get_schema(), True),
                StructField("requester", Reference.get_schema(), True),
                StructField("performer", Reference.get_schema(), True),
                StructField(
                    "performerType", CodeableConcept.get_schema(), True
                ),
                StructField("recorder", Reference.get_schema(), True),
                StructField(
                    "reasonCode", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "reasonReference", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "instantiatesCanonical", ArrayType(canonical.get_schema()),
                    True
                ),
                StructField(
                    "instantiatesUri", ArrayType(uri.get_schema()), True
                ),
                StructField(
                    "basedOn", ArrayType(Reference.get_schema()), True
                ),
                StructField("groupIdentifier", Identifier.get_schema(), True),
                StructField(
                    "courseOfTherapyType", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "insurance", ArrayType(Reference.get_schema()), True
                ),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField(
                    "dosageInstruction", ArrayType(Dosage.get_schema()), True
                ),
                StructField(
                    "dispenseRequest",
                    MedicationRequest_DispenseRequest.get_schema(), True
                ),
                StructField(
                    "substitution",
                    MedicationRequest_Substitution.get_schema(), True
                ),
                StructField("priorPrescription", Reference.get_schema(), True),
                StructField(
                    "detectedIssue", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "eventHistory", ArrayType(Reference.get_schema()), True
                ),
            ]
        )

        return schema
