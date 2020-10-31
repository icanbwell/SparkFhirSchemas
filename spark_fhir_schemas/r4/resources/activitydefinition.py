from pyspark.sql.types import ArrayType, BooleanType, DateType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.age import Age
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.duration import Duration
from spark_fhir_schemas.r4.complex_types.activitydefinition_participant import ActivityDefinition_Participant
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.dosage import Dosage
from spark_fhir_schemas.r4.complex_types.activitydefinition_dynamicvalue import ActivityDefinition_DynamicValue


# noinspection PyPep8Naming
class ActivityDefinition:
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
                StructField("subtitle", StringType(), True),
                StructField("status", StringType(), True),
                StructField("experimental", BooleanType(), True),
                StructField(
                    "subjectCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField("subjectReference", Reference.get_schema(), True),
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
                StructField("usage", StringType(), True),
                StructField("copyright", markdown.get_schema(), True),
                StructField("approvalDate", DateType(), True),
                StructField("lastReviewDate", DateType(), True),
                StructField("effectivePeriod", Period.get_schema(), True),
                StructField(
                    "topic", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "author", ArrayType(ContactDetail.get_schema()), True
                ),
                StructField(
                    "editor", ArrayType(ContactDetail.get_schema()), True
                ),
                StructField(
                    "reviewer", ArrayType(ContactDetail.get_schema()), True
                ),
                StructField(
                    "endorser", ArrayType(ContactDetail.get_schema()), True
                ),
                StructField(
                    "relatedArtifact", ArrayType(RelatedArtifact.get_schema()),
                    True
                ),
                StructField(
                    "library", ArrayType(canonical.get_schema()), True
                ),
                StructField("kind", code.get_schema(), True),
                StructField("profile", canonical.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("intent", code.get_schema(), True),
                StructField("priority", code.get_schema(), True),
                StructField("doNotPerform", BooleanType(), True),
                StructField("timingTiming", Timing.get_schema(), True),
                StructField("timingDateTime", StringType(), True),
                StructField("timingAge", Age.get_schema(), True),
                StructField("timingPeriod", Period.get_schema(), True),
                StructField("timingRange", Range.get_schema(), True),
                StructField("timingDuration", Duration.get_schema(), True),
                StructField("location", Reference.get_schema(), True),
                StructField(
                    "participant",
                    ArrayType(ActivityDefinition_Participant.get_schema()),
                    True
                ),
                StructField("productReference", Reference.get_schema(), True),
                StructField(
                    "productCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("dosage", ArrayType(Dosage.get_schema()), True),
                StructField(
                    "bodySite", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "specimenRequirement", ArrayType(Reference.get_schema()),
                    True
                ),
                StructField(
                    "observationRequirement",
                    ArrayType(Reference.get_schema()), True
                ),
                StructField(
                    "observationResultRequirement",
                    ArrayType(Reference.get_schema()), True
                ),
                StructField("transform", canonical.get_schema(), True),
                StructField(
                    "dynamicValue",
                    ArrayType(ActivityDefinition_DynamicValue.get_schema()),
                    True
                ),
            ]
        )

        return schema
