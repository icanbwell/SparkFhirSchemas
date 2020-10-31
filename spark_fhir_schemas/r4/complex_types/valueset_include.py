from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ValueSet_Include:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.valueset_concept import ValueSet_Concept
        from spark_fhir_schemas.r4.complex_types.valueset_filter import ValueSet_Filter
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
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
                    "system", uri.get_schema(recursion_depth + 1), True
                ),
                StructField("version", StringType(), True),
                StructField(
                    "concept",
                    ArrayType(
                        ValueSet_Concept.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "filter",
                    ArrayType(ValueSet_Filter.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "valueSet",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
