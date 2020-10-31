from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class RequestGroup_Action:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.complex_types.requestgroup_condition import RequestGroup_Condition
        from spark_fhir_schemas.r4.complex_types.requestgroup_relatedaction import RequestGroup_RelatedAction
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
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
                    "documentation",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "condition",
                    ArrayType(
                        RequestGroup_Condition.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "relatedAction",
                    ArrayType(
                        RequestGroup_RelatedAction.
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
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "groupingBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "selectionBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "requiredBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "precheckBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "cardinalityBehavior",
                    code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resource", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "action",
                    ArrayType(
                        RequestGroup_Action.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
