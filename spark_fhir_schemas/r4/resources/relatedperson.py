from pyspark.sql.types import ArrayType, BooleanType, DateType, StringType, StructField, StructType

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
from spark_fhir_schemas.r4.complex_types.humanname import HumanName
from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
from spark_fhir_schemas.r4.complex_types.address import Address
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.relatedperson_communication import RelatedPerson_Communication


# noinspection PyPep8Naming
class RelatedPerson:
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
                StructField("patient", Reference.get_schema(), True),
                StructField(
                    "relationship", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("name", ArrayType(HumanName.get_schema()), True),
                StructField(
                    "telecom", ArrayType(ContactPoint.get_schema()), True
                ),
                StructField("gender", StringType(), True),
                StructField("birthDate", DateType(), True),
                StructField("address", ArrayType(Address.get_schema()), True),
                StructField("photo", ArrayType(Attachment.get_schema()), True),
                StructField("period", Period.get_schema(), True),
                StructField(
                    "communication",
                    ArrayType(RelatedPerson_Communication.get_schema()), True
                ),
            ]
        )

        return schema
