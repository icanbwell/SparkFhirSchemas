from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class HealthcareService:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.healthcareservice_eligibility import HealthcareService_Eligibility
        from spark_fhir_schemas.r4.complex_types.healthcareservice_availabletime import HealthcareService_AvailableTime
        from spark_fhir_schemas.r4.complex_types.healthcareservice_notavailable import HealthcareService_NotAvailable
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    "providedBy", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "specialty",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "location",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("name", StringType(), True),
                StructField("comment", StringType(), True),
                StructField(
                    "extraDetails", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "photo", Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "telecom",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "coverageArea",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "serviceProvisionCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "eligibility",
                    ArrayType(
                        HealthcareService_Eligibility.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "program",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "characteristic",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "communication",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "referralMethod",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("appointmentRequired", BooleanType(), True),
                StructField(
                    "availableTime",
                    ArrayType(
                        HealthcareService_AvailableTime.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "notAvailable",
                    ArrayType(
                        HealthcareService_NotAvailable.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("availabilityExceptions", StringType(), True),
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
