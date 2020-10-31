from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class PlanDefinition_Action:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.simple_types.id import id
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
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.plandefinition_dynamicvalue import PlanDefinition_DynamicValue
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField("prefix", StringType(), True),
                StructField("title", StringType(), True),
                StructField("description", StringType(), True),
                StructField("textEquivalent", StringType(), True),
                StructField(
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "code",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "reason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "documentation",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "goalId", ArrayType(id.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "subjectCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subjectReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "trigger",
                    ArrayType(
                        TriggerDefinition.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "condition",
                    ArrayType(
                        PlanDefinition_Condition.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "input",
                    ArrayType(DataRequirement.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "output",
                    ArrayType(DataRequirement.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "relatedAction",
                    ArrayType(
                        PlanDefinition_RelatedAction.
                        get_schema(recursion_depth + 1)
                    ), True
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
                    "timingDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "timingRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "timingTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "participant",
                    ArrayType(
                        PlanDefinition_Participant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("groupingBehavior", StringType(), True),
                StructField("selectionBehavior", StringType(), True),
                StructField("requiredBehavior", StringType(), True),
                StructField("precheckBehavior", StringType(), True),
                StructField("cardinalityBehavior", StringType(), True),
                StructField("definitionCanonical", StringType(), True),
                StructField("definitionUri", StringType(), True),
                StructField(
                    "transform", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "dynamicValue",
                    ArrayType(
                        PlanDefinition_DynamicValue.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "action",
                    ArrayType(
                        PlanDefinition_Action.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
