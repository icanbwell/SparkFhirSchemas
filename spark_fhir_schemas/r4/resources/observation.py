from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Observation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.sampleddata import SampledData
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.observation_referencerange import Observation_ReferenceRange
        from spark_fhir_schemas.r4.complex_types.observation_component import Observation_Component
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "basedOn",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "focus",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("effectiveDateTime", StringType(), True),
                StructField(
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "effectiveTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("effectiveInstant", StringType(), True),
                StructField(
                    "issued", instant.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "performer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("valueString", StringType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                StructField("valueTime", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dataAbsentReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "interpretation",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "bodySite",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "method", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "specimen", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "device", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "referenceRange",
                    ArrayType(
                        Observation_ReferenceRange.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "hasMember",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "derivedFrom",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "component",
                    ArrayType(
                        Observation_Component.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
