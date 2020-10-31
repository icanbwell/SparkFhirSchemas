from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class EvidenceVariable_Characteristic:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.expression import Expression
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
        from spark_fhir_schemas.r4.complex_types.triggerdefinition import TriggerDefinition
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.timing import Timing
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
                StructField("description", StringType(), True),
                StructField(
                    "definitionReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("definitionCanonical", StringType(), True),
                StructField(
                    "definitionCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "definitionExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "definitionDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "definitionTriggerDefinition",
                    TriggerDefinition.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "usageContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("exclude", BooleanType(), True),
                StructField(
                    "participantEffectiveDateTime", StringType(), True
                ),
                StructField(
                    "participantEffectivePeriod",
                    Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "participantEffectiveDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "participantEffectiveTiming",
                    Timing.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "timeFromStart", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("groupMeasure", StringType(), True),
            ]
        )

        return schema
