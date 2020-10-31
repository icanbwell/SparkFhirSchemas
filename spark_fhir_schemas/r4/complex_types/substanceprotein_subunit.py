from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceProtein_Subunit:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
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
                    "subunit", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("sequence", StringType(), True),
                StructField(
                    "length", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sequenceAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "nTerminalModificationId",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField("nTerminalModification", StringType(), True),
                StructField(
                    "cTerminalModificationId",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField("cTerminalModification", StringType(), True),
            ]
        )
        return schema
