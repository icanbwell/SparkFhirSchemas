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
from spark_fhir_schemas.r4.complex_types.diagnosticreport_media import DiagnosticReport_Media
from spark_fhir_schemas.r4.complex_types.attachment import Attachment


# noinspection PyPep8Naming
class DiagnosticReport:
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
                StructField("status", StringType(), True),
                StructField(
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("effectiveDateTime", StringType(), True),
                StructField("effectivePeriod", Period.get_schema(), True),
                StructField("issued", instant.get_schema(), True),
                StructField(
                    "performer", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "resultsInterpreter", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField(
                    "specimen", ArrayType(Reference.get_schema()), True
                ),
                StructField("result", ArrayType(Reference.get_schema()), True),
                StructField(
                    "imagingStudy", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "media", ArrayType(DiagnosticReport_Media.get_schema()),
                    True
                ),
                StructField("conclusion", StringType(), True),
                StructField(
                    "conclusionCode", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "presentedForm", ArrayType(Attachment.get_schema()), True
                ),
            ]
        )

        return schema
