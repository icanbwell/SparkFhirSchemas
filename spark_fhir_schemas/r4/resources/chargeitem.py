from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ChargeItem:
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
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.chargeitem_performer import ChargeItem_Performer
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
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
                    "definitionUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "definitionCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "partOf",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "context", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("occurrenceDateTime", StringType(), True),
                StructField(
                    "occurrencePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "occurrenceTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "performer",
                    ArrayType(
                        ChargeItem_Performer.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "performingOrganization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "requestingOrganization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "costCenter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "bodysite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "factorOverride", decimal.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "priceOverride", Money.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("overrideReason", StringType(), True),
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "enteredDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "reason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "service",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "productReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "productCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "account",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "supportingInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
