from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.instant import instant
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.auditevent_agent import AuditEvent_Agent
from spark_fhir_schemas.r4.complex_types.auditevent_source import AuditEvent_Source
from spark_fhir_schemas.r4.complex_types.auditevent_entity import AuditEvent_Entity


# noinspection PyPep8Naming
class AuditEvent:
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
                StructField("type", Coding.get_schema(), True),
                StructField("subtype", ArrayType(Coding.get_schema()), True),
                StructField("action", StringType(), True),
                StructField("period", Period.get_schema(), True),
                StructField("recorded", instant.get_schema(), True),
                StructField("outcome", StringType(), True),
                StructField("outcomeDesc", StringType(), True),
                StructField(
                    "purposeOfEvent", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "agent", ArrayType(AuditEvent_Agent.get_schema()), True
                ),
                StructField("source", AuditEvent_Source.get_schema(), True),
                StructField(
                    "entity", ArrayType(AuditEvent_Entity.get_schema()), True
                ),
            ]
        )

        return schema
