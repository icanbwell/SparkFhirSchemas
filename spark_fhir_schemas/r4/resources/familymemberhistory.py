from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class FamilyMemberHistory:
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
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.familymemberhistory_condition import FamilyMemberHistory_Condition
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
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "dataAbsentReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField("name", StringType(), True),
                StructField(
                    "relationship",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sex", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "bornPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField("bornDate", StringType(), True),
                StructField("bornString", StringType(), True),
                StructField(
                    "ageAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "ageRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField("ageString", StringType(), True),
                StructField("estimatedAge", BooleanType(), True),
                StructField("deceasedBoolean", BooleanType(), True),
                StructField(
                    "deceasedAge", Age.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "deceasedRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("deceasedDate", StringType(), True),
                StructField("deceasedString", StringType(), True),
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "condition",
                    ArrayType(
                        FamilyMemberHistory_Condition.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
