from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicationRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
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
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                StructField("doNotPerform", BooleanType(), True),
                StructField("reportedBoolean", BooleanType(), True),
                StructField(
                    "reportedReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "medicationCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "medicationReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "supportingInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "authoredOn", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "requester", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "performerType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "recorder", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "groupIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "courseOfTherapyType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "insurance",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "dosageInstruction",
                    ArrayType(Dosage.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "dispenseRequest",
                    MedicationRequest_DispenseRequest.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "substitution",
                    MedicationRequest_Substitution.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "priorPrescription",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "detectedIssue",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "eventHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )

        return schema
