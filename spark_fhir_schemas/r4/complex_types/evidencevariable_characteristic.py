from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

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


# noinspection PyPep8Naming
class EvidenceVariable_Characteristic:
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
                StructField("description", StringType(), True),
                StructField(
                    "definitionReference", Reference.get_schema(), True
                ),
                StructField("definitionCanonical", StringType(), True),
                StructField(
                    "definitionCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "definitionExpression", Expression.get_schema(), True
                ),
                StructField(
                    "definitionDataRequirement", DataRequirement.get_schema(),
                    True
                ),
                StructField(
                    "definitionTriggerDefinition",
                    TriggerDefinition.get_schema(), True
                ),
                StructField(
                    "usageContext", ArrayType(UsageContext.get_schema()), True
                ),
                StructField("exclude", BooleanType(), True),
                StructField(
                    "participantEffectiveDateTime", StringType(), True
                ),
                StructField(
                    "participantEffectivePeriod", Period.get_schema(), True
                ),
                StructField(
                    "participantEffectiveDuration", Duration.get_schema(), True
                ),
                StructField(
                    "participantEffectiveTiming", Timing.get_schema(), True
                ),
                StructField("timeFromStart", Duration.get_schema(), True),
                StructField("groupMeasure", StringType(), True),
            ]
        )

        return schema
