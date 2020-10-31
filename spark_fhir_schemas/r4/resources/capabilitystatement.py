from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.capabilitystatement_software import CapabilityStatement_Software
from spark_fhir_schemas.r4.complex_types.capabilitystatement_implementation import CapabilityStatement_Implementation
from spark_fhir_schemas.r4.complex_types.capabilitystatement_rest import CapabilityStatement_Rest
from spark_fhir_schemas.r4.complex_types.capabilitystatement_messaging import CapabilityStatement_Messaging
from spark_fhir_schemas.r4.complex_types.capabilitystatement_document import CapabilityStatement_Document


# noinspection PyPep8Naming
class CapabilityStatement:
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
                StructField("url", uri.get_schema(), True),
                StructField("version", StringType(), True),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("status", StringType(), True),
                StructField("experimental", BooleanType(), True),
                StructField("date", dateTime.get_schema(), True),
                StructField("publisher", StringType(), True),
                StructField(
                    "contact", ArrayType(ContactDetail.get_schema()), True
                ),
                StructField("description", markdown.get_schema(), True),
                StructField(
                    "useContext", ArrayType(UsageContext.get_schema()), True
                ),
                StructField(
                    "jurisdiction", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("purpose", markdown.get_schema(), True),
                StructField("copyright", markdown.get_schema(), True),
                StructField("kind", StringType(), True),
                StructField(
                    "instantiates", ArrayType(canonical.get_schema()), True
                ),
                StructField(
                    "imports", ArrayType(canonical.get_schema()), True
                ),
                StructField(
                    "software", CapabilityStatement_Software.get_schema(), True
                ),
                StructField(
                    "implementation",
                    CapabilityStatement_Implementation.get_schema(), True
                ),
                StructField("fhirVersion", StringType(), True),
                StructField("format", ArrayType(code.get_schema()), True),
                StructField("patchFormat", ArrayType(code.get_schema()), True),
                StructField(
                    "implementationGuide", ArrayType(canonical.get_schema()),
                    True
                ),
                StructField(
                    "rest", ArrayType(CapabilityStatement_Rest.get_schema()),
                    True
                ),
                StructField(
                    "messaging",
                    ArrayType(CapabilityStatement_Messaging.get_schema()), True
                ),
                StructField(
                    "document",
                    ArrayType(CapabilityStatement_Document.get_schema()), True
                ),
            ]
        )

        return schema
