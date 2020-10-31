from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MedicationDispense:
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
        from spark_fhir_schemas.r4.complex_types.medicationdispense_performer import MedicationDispense_Performer
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.dosage import Dosage
        from spark_fhir_schemas.r4.complex_types.medicationdispense_substitution import MedicationDispense_Substitution
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
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "statusReasonCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "statusReasonReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
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
                    "context", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "supportingInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "performer",
                    ArrayType(
                        MedicationDispense_Performer.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "authorizingPrescription",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "daysSupply", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "whenPrepared", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "whenHandedOver", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "destination", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "receiver",
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
                    "substitution",
                    MedicationDispense_Substitution.
                    get_schema(recursion_depth + 1), True
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
