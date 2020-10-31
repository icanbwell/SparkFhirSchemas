from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.age import Age
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.procedure_performer import Procedure_Performer
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.procedure_focaldevice import Procedure_FocalDevice


# noinspection PyPep8Naming
class Procedure:
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
                    "instantiatesCanonical", ArrayType(canonical.get_schema()),
                    True
                ),
                StructField(
                    "instantiatesUri", ArrayType(uri.get_schema()), True
                ),
                StructField(
                    "basedOn", ArrayType(Reference.get_schema()), True
                ),
                StructField("partOf", ArrayType(Reference.get_schema()), True),
                StructField("status", code.get_schema(), True),
                StructField(
                    "statusReason", CodeableConcept.get_schema(), True
                ),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("performedDateTime", StringType(), True),
                StructField("performedPeriod", Period.get_schema(), True),
                StructField("performedString", StringType(), True),
                StructField("performedAge", Age.get_schema(), True),
                StructField("performedRange", Range.get_schema(), True),
                StructField("recorder", Reference.get_schema(), True),
                StructField("asserter", Reference.get_schema(), True),
                StructField(
                    "performer", ArrayType(Procedure_Performer.get_schema()),
                    True
                ),
                StructField("location", Reference.get_schema(), True),
                StructField(
                    "reasonCode", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "reasonReference", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "bodySite", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("outcome", CodeableConcept.get_schema(), True),
                StructField("report", ArrayType(Reference.get_schema()), True),
                StructField(
                    "complication", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "complicationDetail", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField(
                    "followUp", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField(
                    "focalDevice",
                    ArrayType(Procedure_FocalDevice.get_schema()), True
                ),
                StructField(
                    "usedReference", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "usedCode", ArrayType(CodeableConcept.get_schema()), True
                ),
            ]
        )

        return schema
