from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Claim_SupportingInfo:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                    "sequence", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("timingDate", StringType(), True),
                StructField(
                    "timingPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueString", StringType(), True),
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "reason", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
