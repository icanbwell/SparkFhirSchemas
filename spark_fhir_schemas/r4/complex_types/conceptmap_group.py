from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ConceptMap_Group:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.conceptmap_element import ConceptMap_Element
        from spark_fhir_schemas.r4.complex_types.conceptmap_unmapped import ConceptMap_Unmapped
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
                    "source", uri.get_schema(recursion_depth + 1), True
                ),
                StructField("sourceVersion", StringType(), True),
                StructField(
                    "target", uri.get_schema(recursion_depth + 1), True
                ),
                StructField("targetVersion", StringType(), True),
                StructField(
                    "element",
                    ArrayType(
                        ConceptMap_Element.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "unmapped",
                    ConceptMap_Unmapped.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
