from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

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
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.annotation import Annotation


# noinspection PyPep8Naming
class ServiceRequest:
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
                StructField(
                    "replaces", ArrayType(Reference.get_schema()), True
                ),
                StructField("requisition", Identifier.get_schema(), True),
                StructField("status", code.get_schema(), True),
                StructField("intent", code.get_schema(), True),
                StructField(
                    "category", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("priority", code.get_schema(), True),
                StructField("doNotPerform", BooleanType(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField(
                    "orderDetail", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("quantityQuantity", Quantity.get_schema(), True),
                StructField("quantityRatio", Ratio.get_schema(), True),
                StructField("quantityRange", Range.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("occurrenceDateTime", StringType(), True),
                StructField("occurrencePeriod", Period.get_schema(), True),
                StructField("occurrenceTiming", Timing.get_schema(), True),
                StructField("asNeededBoolean", BooleanType(), True),
                StructField(
                    "asNeededCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField("authoredOn", dateTime.get_schema(), True),
                StructField("requester", Reference.get_schema(), True),
                StructField(
                    "performerType", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "performer", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "locationCode", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "locationReference", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField(
                    "reasonCode", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "reasonReference", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "insurance", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "supportingInfo", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "specimen", ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "bodySite", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField("patientInstruction", StringType(), True),
                StructField(
                    "relevantHistory", ArrayType(Reference.get_schema()), True
                ),
            ]
        )

        return schema
