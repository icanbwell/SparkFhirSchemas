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
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.age import Age
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.age import Age
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.annotation import Annotation
from spark_fhir_schemas.r4.resources.familymemberhistory_condition import FamilyMemberHistory_Condition


class FamilyMemberHistory:
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
                StructField("instantiatesCanonical",ArrayType(canonical.get_schema()), True),
                StructField("instantiatesUri",ArrayType(uri.get_schema()), True),
                StructField("status", StringType(), True),
                StructField("dataAbsentReason", CodeableConcept.get_schema(), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("date", dateTime.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("relationship", CodeableConcept.get_schema(), True),
                StructField("sex", CodeableConcept.get_schema(), True),
                StructField("bornPeriod", Period.get_schema(), True),
                StructField("bornDate", StringType(), True),
                StructField("bornString", StringType(), True),
                StructField("ageAge", Age.get_schema(), True),
                StructField("ageRange", Range.get_schema(), True),
                StructField("ageString", StringType(), True),
                StructField("estimatedAge", BooleanType(), True),
                StructField("deceasedBoolean", BooleanType(), True),
                StructField("deceasedAge", Age.get_schema(), True),
                StructField("deceasedRange", Range.get_schema(), True),
                StructField("deceasedDate", StringType(), True),
                StructField("deceasedString", StringType(), True),
                StructField("reasonCode",ArrayType(CodeableConcept.get_schema()), True),
                StructField("reasonReference",ArrayType(Reference.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("condition",ArrayType(FamilyMemberHistory_Condition.get_schema()), True),]
        )

        return schema
