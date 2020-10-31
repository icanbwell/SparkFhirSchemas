from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.provenance_agent import Provenance_Agent
from spark_fhir_schemas.r4.resources.provenance_entity import Provenance_Entity
from spark_fhir_schemas.r4.resources.signature import Signature


class Provenance:
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
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("target",ArrayType(Reference.get_schema()), True),
                StructField("occurredPeriod", Period.get_schema(), True),
                StructField("occurredDateTime", StringType(), True),
                StructField("recorded", instant.get_schema(), True),
                StructField("policy",ArrayType(uri.get_schema()), True),
                StructField("location", Reference.get_schema(), True),
                StructField("reason",ArrayType(CodeableConcept.get_schema()), True),
                StructField("activity", CodeableConcept.get_schema(), True),
                StructField("agent",ArrayType(Provenance_Agent.get_schema()), True),
                StructField("entity",ArrayType(Provenance_Entity.get_schema()), True),
                StructField("signature",ArrayType(Signature.get_schema()), True),]
        )

        return schema
