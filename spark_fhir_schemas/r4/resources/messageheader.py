from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.messageheader_destination import MessageHeader_Destination
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.messageheader_source import MessageHeader_Source
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.messageheader_response import MessageHeader_Response
from spark_fhir_schemas.r4.complex_types.canonical import canonical


# noinspection PyPep8Naming
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
                StructField("eventCoding", Coding.get_schema(), True),
                StructField("eventUri", StringType(), True),
                StructField(
                    "destination",
                    ArrayType(MessageHeader_Destination.get_schema()), True
                ),
                StructField("sender", Reference.get_schema(), True),
                StructField("enterer", Reference.get_schema(), True),
                StructField("author", Reference.get_schema(), True),
                StructField("source", MessageHeader_Source.get_schema(), True),
                StructField("responsible", Reference.get_schema(), True),
                StructField("reason", CodeableConcept.get_schema(), True),
                StructField(
                    "response", MessageHeader_Response.get_schema(), True
                ),
                StructField("focus", ArrayType(Reference.get_schema()), True),
                StructField("definition", canonical.get_schema(), True),
            ]
        )

        return schema
