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
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.dosage import Dosage


# noinspection PyPep8Naming
class MedicationStatement:
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
                StructField(
                    "statusReason", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField(
                    "medicationCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "medicationReference", Reference.get_schema(), True
                ),
                StructField("subject", Reference.get_schema(), True),
                StructField("context", Reference.get_schema(), True),
                StructField("effectiveDateTime", StringType(), True),
                StructField("effectivePeriod", Period.get_schema(), True),
                StructField("dateAsserted", dateTime.get_schema(), True),
                StructField("informationSource", Reference.get_schema(), True),
                StructField(
                    "derivedFrom", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "reasonCode", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "reasonReference", ArrayType(Reference.get_schema()), True
                ),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField("dosage", ArrayType(Dosage.get_schema()), True),
            ]
        )

        return schema
