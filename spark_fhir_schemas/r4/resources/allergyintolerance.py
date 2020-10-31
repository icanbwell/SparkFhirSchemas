from pyspark.sql.types import ArrayType, StringType, StructField, StructType

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
from spark_fhir_schemas.r4.complex_types.age import Age
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.allergyintolerance_reaction import AllergyIntolerance_Reaction


# noinspection PyPep8Naming
class AllergyIntolerance:
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
                    "clinicalStatus", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "verificationStatus", CodeableConcept.get_schema(), True
                ),
                StructField("type", StringType(), True),
                StructField("criticality", StringType(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("onsetDateTime", StringType(), True),
                StructField("onsetAge", Age.get_schema(), True),
                StructField("onsetPeriod", Period.get_schema(), True),
                StructField("onsetRange", Range.get_schema(), True),
                StructField("onsetString", StringType(), True),
                StructField("recordedDate", dateTime.get_schema(), True),
                StructField("recorder", Reference.get_schema(), True),
                StructField("asserter", Reference.get_schema(), True),
                StructField("lastOccurrence", dateTime.get_schema(), True),
                StructField("note", ArrayType(Annotation.get_schema()), True),
                StructField(
                    "reaction",
                    ArrayType(AllergyIntolerance_Reaction.get_schema()), True
                ),
            ]
        )

        return schema