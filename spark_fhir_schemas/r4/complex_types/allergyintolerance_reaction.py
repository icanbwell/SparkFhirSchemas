from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class AllergyIntolerance_Reaction:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
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
                    "substance",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "manifestation",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "onset", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField("severity", StringType(), True),
                StructField(
                    "exposureRoute",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
