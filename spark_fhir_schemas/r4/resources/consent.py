from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Consent:
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
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.consent_policy import Consent_Policy
        from spark_fhir_schemas.r4.complex_types.consent_verification import Consent_Verification
        from spark_fhir_schemas.r4.complex_types.consent_provision import Consent_Provision
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
                StructField("status", StringType(), True),
                StructField(
                    "scope", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dateTime", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "performer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "organization",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "sourceAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sourceReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "policy",
                    ArrayType(Consent_Policy.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "policyRule",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "verification",
                    ArrayType(
                        Consent_Verification.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "provision",
                    Consent_Provision.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
