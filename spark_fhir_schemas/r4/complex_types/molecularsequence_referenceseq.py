from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence_ReferenceSeq:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.integer import integer
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
                    "chromosome",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("genomeBuild", StringType(), True),
                StructField("orientation", StringType(), True),
                StructField(
                    "referenceSeqId",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "referenceSeqPointer",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("referenceSeqString", StringType(), True),
                StructField("strand", StringType(), True),
                StructField(
                    "windowStart", integer.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "windowEnd", integer.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
