from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.instant import instant
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.sampleddata import SampledData
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.observation_referencerange import Observation_ReferenceRange
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.observation_component import Observation_Component


class Observation:
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
                StructField("basedOn",ArrayType(Reference.get_schema()), True),
                StructField("partOf",ArrayType(Reference.get_schema()), True),
                StructField("status", StringType(), True),
                StructField("category",ArrayType(CodeableConcept.get_schema()), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("focus",ArrayType(Reference.get_schema()), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("effectiveDateTime", StringType(), True),
                StructField("effectivePeriod", Period.get_schema(), True),
                StructField("effectiveTiming", Timing.get_schema(), True),
                StructField("effectiveInstant", StringType(), True),
                StructField("issued", instant.get_schema(), True),
                StructField("performer",ArrayType(Reference.get_schema()), True),
                StructField("valueQuantity", Quantity.get_schema(), True),
                StructField("valueCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("valueString", StringType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueRange", Range.get_schema(), True),
                StructField("valueRatio", Ratio.get_schema(), True),
                StructField("valueSampledData", SampledData.get_schema(), True),
                StructField("valueTime", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField("valuePeriod", Period.get_schema(), True),
                StructField("dataAbsentReason", CodeableConcept.get_schema(), True),
                StructField("interpretation",ArrayType(CodeableConcept.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("bodySite", CodeableConcept.get_schema(), True),
                StructField("method", CodeableConcept.get_schema(), True),
                StructField("specimen", Reference.get_schema(), True),
                StructField("device", Reference.get_schema(), True),
                StructField("referenceRange",ArrayType(Observation_ReferenceRange.get_schema()), True),
                StructField("hasMember",ArrayType(Reference.get_schema()), True),
                StructField("derivedFrom",ArrayType(Reference.get_schema()), True),
                StructField("component",ArrayType(Observation_Component.get_schema()), True),
            ]
        )

        return schema
