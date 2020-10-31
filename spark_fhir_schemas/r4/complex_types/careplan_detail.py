from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CarePlan_Detail:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "kind", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
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
                    "goal",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "statusReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("doNotPerform", BooleanType(), True),
                StructField(
                    "scheduledTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "scheduledPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("scheduledString", StringType(), True),
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "performer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "productCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "productReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dailyAmount", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField("description", StringType(), True),
            ]
        )
        return schema
