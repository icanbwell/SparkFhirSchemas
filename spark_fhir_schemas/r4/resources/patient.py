from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


# noinspection PyPep8Naming
class Patient:
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
        from spark_fhir_schemas.r4.complex_types.humanname import HumanName
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.patient_contact import Patient_Contact
        from spark_fhir_schemas.r4.complex_types.patient_communication import Patient_Communication
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.patient_link import Patient_Link
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
                StructField("active", BooleanType(), True),
                StructField(
                    "name",
                    ArrayType(HumanName.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "telecom",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("gender", StringType(), True),
                StructField("birthDate", DateType(), True),
                StructField("deceasedBoolean", BooleanType(), True),
                StructField("deceasedDateTime", StringType(), True),
                StructField(
                    "address",
                    ArrayType(Address.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "maritalStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("multipleBirthBoolean", BooleanType(), True),
                StructField("multipleBirthInteger", IntegerType(), True),
                StructField(
                    "photo",
                    ArrayType(Attachment.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "contact",
                    ArrayType(Patient_Contact.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "communication",
                    ArrayType(
                        Patient_Communication.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "generalPractitioner",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "managingOrganization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "link",
                    ArrayType(Patient_Link.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )

        return schema
