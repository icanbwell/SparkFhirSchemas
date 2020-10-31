from pyspark.sql.types import ArrayType, StringType, StructField, StructType

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
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.instant import instant
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.annotation import Annotation


# noinspection PyPep8Naming
class Media:
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
                StructField(
                    "basedOn", ArrayType(Reference.get_schema()), True
                ),
                StructField("partOf", ArrayType(Reference.get_schema()), True),
                StructField("status", code.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("modality", CodeableConcept.get_schema(), True),
                StructField("view", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("createdDateTime", StringType(), True),
                StructField("createdPeriod", Period.get_schema(), True),
                StructField("issued", instant.get_schema(), True),
                StructField("operator", Reference.get_schema(), True),
                StructField(
                    "reasonCode", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("bodySite", CodeableConcept.get_schema(), True),
                StructField("deviceName", StringType(), True),
                StructField("device", Reference.get_schema(), True),
                StructField("height", positiveInt.get_schema(), True),
                StructField("width", positiveInt.get_schema(), True),
                StructField("frames", positiveInt.get_schema(), True),
                StructField("duration", decimal.get_schema(), True),
                StructField("content", Attachment.get_schema(), True),
                StructField("note", ArrayType(Annotation.get_schema()), True),
            ]
        )

        return schema
