from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.triggerdefinition import TriggerDefinition
from spark_fhir_schemas.r4.complex_types.plandefinition_condition import PlanDefinition_Condition
from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
from spark_fhir_schemas.r4.complex_types.plandefinition_relatedaction import PlanDefinition_RelatedAction
from spark_fhir_schemas.r4.complex_types.age import Age
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.duration import Duration
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.plandefinition_participant import PlanDefinition_Participant
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.plandefinition_dynamicvalue import PlanDefinition_DynamicValue


# noinspection PyPep8Naming
class PlanDefinition_Action:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("prefix", StringType(), True),
                StructField("title", StringType(), True),
                StructField("description", StringType(), True),
                StructField("textEquivalent", StringType(), True),
                StructField("priority", code.get_schema(), True),
                StructField(
                    "code", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "reason", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "documentation", ArrayType(RelatedArtifact.get_schema()),
                    True
                ),
                StructField("goalId", ArrayType(id.get_schema()), True),
                StructField(
                    "subjectCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField("subjectReference", Reference.get_schema(), True),
                StructField(
                    "trigger", ArrayType(TriggerDefinition.get_schema()), True
                ),
                StructField(
                    "condition",
                    ArrayType(PlanDefinition_Condition.get_schema()), True
                ),
                StructField(
                    "input", ArrayType(DataRequirement.get_schema()), True
                ),
                StructField(
                    "output", ArrayType(DataRequirement.get_schema()), True
                ),
                StructField(
                    "relatedAction",
                    ArrayType(PlanDefinition_RelatedAction.get_schema()), True
                ),
                StructField("timingDateTime", StringType(), True),
                StructField("timingAge", Age.get_schema(), True),
                StructField("timingPeriod", Period.get_schema(), True),
                StructField("timingDuration", Duration.get_schema(), True),
                StructField("timingRange", Range.get_schema(), True),
                StructField("timingTiming", Timing.get_schema(), True),
                StructField(
                    "participant",
                    ArrayType(PlanDefinition_Participant.get_schema()), True
                ),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("groupingBehavior", StringType(), True),
                StructField("selectionBehavior", StringType(), True),
                StructField("requiredBehavior", StringType(), True),
                StructField("precheckBehavior", StringType(), True),
                StructField("cardinalityBehavior", StringType(), True),
                StructField("definitionCanonical", StringType(), True),
                StructField("definitionUri", StringType(), True),
                StructField("transform", canonical.get_schema(), True),
                StructField(
                    "dynamicValue",
                    ArrayType(PlanDefinition_DynamicValue.get_schema()), True
                ),
                StructField(
                    "action", ArrayType(PlanDefinition_Action.get_schema()),
                    True
                ),
            ]
        )

        return schema
