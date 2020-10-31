from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.relatedartifact import RelatedArtifact
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.triggerdefinition import TriggerDefinition
from spark_fhir_schemas.r4.resources.plandefinition_condition import PlanDefinition_Condition
from spark_fhir_schemas.r4.resources.datarequirement import DataRequirement
from spark_fhir_schemas.r4.resources.datarequirement import DataRequirement
from spark_fhir_schemas.r4.resources.plandefinition_relatedaction import PlanDefinition_RelatedAction
from spark_fhir_schemas.r4.resources.age import Age
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.timing import Timing
from spark_fhir_schemas.r4.resources.plandefinition_participant import PlanDefinition_Participant
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.plandefinition_dynamicvalue import PlanDefinition_DynamicValue
from spark_fhir_schemas.r4.resources.plandefinition_action import PlanDefinition_Action


class PlanDefinition_Action:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("prefix", StringType(), True),
                StructField("title", StringType(), True),
                StructField("description", StringType(), True),
                StructField("textEquivalent", StringType(), True),
                StructField("priority", code.get_schema(), True),
                StructField("code",ArrayType(CodeableConcept.get_schema()), True),
                StructField("reason",ArrayType(CodeableConcept.get_schema()), True),
                StructField("documentation",ArrayType(RelatedArtifact.get_schema()), True),
                StructField("goalId",ArrayType(id.get_schema()), True),
                StructField("subjectCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("subjectReference", Reference.get_schema(), True),
                StructField("trigger",ArrayType(TriggerDefinition.get_schema()), True),
                StructField("condition",ArrayType(PlanDefinition_Condition.get_schema()), True),
                StructField("input",ArrayType(DataRequirement.get_schema()), True),
                StructField("output",ArrayType(DataRequirement.get_schema()), True),
                StructField("relatedAction",ArrayType(PlanDefinition_RelatedAction.get_schema()), True),
                StructField("timingDateTime", StringType(), True),
                StructField("timingAge", Age.get_schema(), True),
                StructField("timingPeriod", Period.get_schema(), True),
                StructField("timingDuration", Duration.get_schema(), True),
                StructField("timingRange", Range.get_schema(), True),
                StructField("timingTiming", Timing.get_schema(), True),
                StructField("participant",ArrayType(PlanDefinition_Participant.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("groupingBehavior", StringType(), True),
                StructField("selectionBehavior", StringType(), True),
                StructField("requiredBehavior", StringType(), True),
                StructField("precheckBehavior", StringType(), True),
                StructField("cardinalityBehavior", StringType(), True),
                StructField("definitionCanonical", StringType(), True),
                StructField("definitionUri", StringType(), True),
                StructField("transform", canonical.get_schema(), True),
                StructField("dynamicValue",ArrayType(PlanDefinition_DynamicValue.get_schema()), True),
                StructField("action",ArrayType(PlanDefinition_Action.get_schema()), True),]
        )

        return schema
