from pyspark.sql.types import ArrayType, StringType, StructField, StructType

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


# noinspection PyPep8Naming
class RequestGroup_Action:
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
                    "documentation", ArrayType(RelatedArtifact.get_schema()),
                    True
                ),
                StructField(
                    "condition",
                    ArrayType(RequestGroup_Condition.get_schema()), True
                ),
                StructField(
                    "relatedAction",
                    ArrayType(RequestGroup_RelatedAction.get_schema()), True
                ),
                StructField("timingDateTime", StringType(), True),
                StructField("timingAge", Age.get_schema(), True),
                StructField("timingPeriod", Period.get_schema(), True),
                StructField("timingDuration", Duration.get_schema(), True),
                StructField("timingRange", Range.get_schema(), True),
                StructField("timingTiming", Timing.get_schema(), True),
                StructField(
                    "participant", ArrayType(Reference.get_schema()), True
                ),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("groupingBehavior", code.get_schema(), True),
                StructField("selectionBehavior", code.get_schema(), True),
                StructField("requiredBehavior", code.get_schema(), True),
                StructField("precheckBehavior", code.get_schema(), True),
                StructField("cardinalityBehavior", code.get_schema(), True),
                StructField("resource", Reference.get_schema(), True),
                StructField(
                    "action", ArrayType(RequestGroup_Action.get_schema()), True
                ),
            ]
        )

        return schema
