from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.age import Age
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.age import Age
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.condition_stage import Condition_Stage
from spark_fhir_schemas.r4.resources.condition_evidence import Condition_Evidence
from spark_fhir_schemas.r4.resources.annotation import Annotation


class Condition:
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
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("clinicalStatus", CodeableConcept.get_schema(), True),
                StructField("verificationStatus", CodeableConcept.get_schema(), True),
                StructField("category",ArrayType(CodeableConcept.get_schema()), True),
                StructField("severity", CodeableConcept.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("bodySite",ArrayType(CodeableConcept.get_schema()), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("onsetDateTime", StringType(), True),
                StructField("onsetAge", Age.get_schema(), True),
                StructField("onsetPeriod", Period.get_schema(), True),
                StructField("onsetRange", Range.get_schema(), True),
                StructField("onsetString", StringType(), True),
                StructField("abatementDateTime", StringType(), True),
                StructField("abatementAge", Age.get_schema(), True),
                StructField("abatementPeriod", Period.get_schema(), True),
                StructField("abatementRange", Range.get_schema(), True),
                StructField("abatementString", StringType(), True),
                StructField("recordedDate", dateTime.get_schema(), True),
                StructField("recorder", Reference.get_schema(), True),
                StructField("asserter", Reference.get_schema(), True),
                StructField("stage",ArrayType(Condition_Stage.get_schema()), True),
                StructField("evidence",ArrayType(Condition_Evidence.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),]
        )

        return schema
