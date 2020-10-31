from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.structuredefinition_mapping import StructureDefinition_Mapping
from spark_fhir_schemas.r4.complex_types.structuredefinition_context import StructureDefinition_Context
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.structuredefinition_snapshot import StructureDefinition_Snapshot
from spark_fhir_schemas.r4.complex_types.structuredefinition_differential import StructureDefinition_Differential


# noinspection PyPep8Naming
class StructureDefinition:
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
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
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
                StructField("keyword", ArrayType(Coding.get_schema()), True),
                StructField("fhirVersion", StringType(), True),
                StructField(
                    "mapping",
                    ArrayType(StructureDefinition_Mapping.get_schema()), True
                ),
                StructField("kind", StringType(), True),
                StructField("abstract", BooleanType(), True),
                StructField(
                    "context",
                    ArrayType(StructureDefinition_Context.get_schema()), True
                ),
                StructField("contextInvariant", ArrayType(StringType()), True),
                StructField("type", uri.get_schema(), True),
                StructField("baseDefinition", canonical.get_schema(), True),
                StructField("derivation", StringType(), True),
                StructField(
                    "snapshot", StructureDefinition_Snapshot.get_schema(), True
                ),
                StructField(
                    "differential",
                    StructureDefinition_Differential.get_schema(), True
                ),
            ]
        )

        return schema
