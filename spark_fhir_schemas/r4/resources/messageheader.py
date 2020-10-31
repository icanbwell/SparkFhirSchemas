from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.messageheader_destination import MessageHeader_Destination
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.messageheader_source import MessageHeader_Source
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.messageheader_response import MessageHeader_Response
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.canonical import canonical


class MessageHeader:
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
                StructField("eventCoding", Coding.get_schema(), True),
                StructField("eventUri", StringType(), True),
                StructField("destination",ArrayType(MessageHeader_Destination.get_schema()), True),
                StructField("sender", Reference.get_schema(), True),
                StructField("enterer", Reference.get_schema(), True),
                StructField("author", Reference.get_schema(), True),
                StructField("source", MessageHeader_Source.get_schema(), True),
                StructField("responsible", Reference.get_schema(), True),
                StructField("reason", CodeableConcept.get_schema(), True),
                StructField("response", MessageHeader_Response.get_schema(), True),
                StructField("focus",ArrayType(Reference.get_schema()), True),
                StructField("definition", canonical.get_schema(), True),]
        )

        return schema
