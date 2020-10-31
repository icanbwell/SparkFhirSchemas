from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImplementationGuide_Manifest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.url import url
        from spark_fhir_schemas.r4.complex_types.implementationguide_resource1 import ImplementationGuide_Resource1
        from spark_fhir_schemas.r4.complex_types.implementationguide_page1 import ImplementationGuide_Page1
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
                    "rendering", url.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resource",
                    ArrayType(
                        ImplementationGuide_Resource1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "page",
                    ArrayType(
                        ImplementationGuide_Page1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("image", ArrayType(StringType()), True),
                StructField("other", ArrayType(StringType()), True),
            ]
        )
        return schema
