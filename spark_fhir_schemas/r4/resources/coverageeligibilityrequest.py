from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CoverageEligibilityRequest:
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
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_supportinginfo import CoverageEligibilityRequest_SupportingInfo
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_insurance import CoverageEligibilityRequest_Insurance
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_item import CoverageEligibilityRequest_Item
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
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "priority",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("servicedDate", StringType(), True),
                StructField(
                    "servicedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "provider", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "insurer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "facility", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "supportingInfo",
                    ArrayType(
                        CoverageEligibilityRequest_SupportingInfo.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "insurance",
                    ArrayType(
                        CoverageEligibilityRequest_Insurance.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "item",
                    ArrayType(
                        CoverageEligibilityRequest_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
