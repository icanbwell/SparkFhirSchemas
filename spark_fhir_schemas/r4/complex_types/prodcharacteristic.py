from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ProdCharacteristic:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
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
                    "height", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "width", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "depth", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "weight", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "nominalVolume", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "externalDiameter",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField("shape", StringType(), True),
                StructField("color", ArrayType(StringType()), True),
                StructField("imprint", ArrayType(StringType()), True),
                StructField(
                    "image",
                    ArrayType(Attachment.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "scoring", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
