from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Condition:
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
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.condition_stage import Condition_Stage
        from spark_fhir_schemas.r4.complex_types.condition_evidence import Condition_Evidence
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
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
                    "clinicalStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "verificationStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "severity",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "bodySite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("onsetDateTime", StringType(), True),
                StructField(
                    "onsetAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "onsetPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "onsetRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField("onsetString", StringType(), True),
                StructField("abatementDateTime", StringType(), True),
                StructField(
                    "abatementAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "abatementPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "abatementRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("abatementString", StringType(), True),
                StructField(
                    "recordedDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "recorder", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "asserter", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "stage",
                    ArrayType(Condition_Stage.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "evidence",
                    ArrayType(
                        Condition_Evidence.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
