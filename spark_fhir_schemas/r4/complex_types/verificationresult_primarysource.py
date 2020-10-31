from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class VerificationResult_PrimarySource:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
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
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "communicationMethod",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "validationStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "validationDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "canPushUpdates",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "pushTypeAvailable",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
