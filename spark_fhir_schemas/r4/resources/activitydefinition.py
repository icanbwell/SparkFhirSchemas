from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ActivityDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.activitydefinition_participant import ActivityDefinition_Participant
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.dosage import Dosage
        from spark_fhir_schemas.r4.complex_types.activitydefinition_dynamicvalue import ActivityDefinition_DynamicValue
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("version", StringType(), True),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("subtitle", StringType(), True),
                StructField("status", StringType(), True),
                StructField("experimental", BooleanType(), True),
                StructField(
                    "subjectCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subjectReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField("publisher", StringType(), True),
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField("usage", StringType(), True),
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField("approvalDate", DateType(), True),
                StructField("lastReviewDate", DateType(), True),
                StructField(
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "topic",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "author",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "editor",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "reviewer",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "endorser",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "relatedArtifact",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "library",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "kind", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "profile", canonical.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                StructField("doNotPerform", BooleanType(), True),
                StructField(
                    "timingTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("timingDateTime", StringType(), True),
                StructField(
                    "timingAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "timingPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "timingRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "timingDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "participant",
                    ArrayType(
                        ActivityDefinition_Participant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "productReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "productCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dosage",
                    ArrayType(Dosage.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "bodySite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "specimenRequirement",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "observationRequirement",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "observationResultRequirement",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "transform", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "dynamicValue",
                    ArrayType(
                        ActivityDefinition_DynamicValue.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
