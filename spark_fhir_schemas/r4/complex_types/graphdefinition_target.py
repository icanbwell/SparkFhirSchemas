from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class GraphDefinition_Target:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.graphdefinition_compartment import GraphDefinition_Compartment
        from spark_fhir_schemas.r4.complex_types.graphdefinition_link import GraphDefinition_Link
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
                    "type", code.get_schema(recursion_depth + 1), True
                ),
                StructField("params", StringType(), True),
                StructField(
                    "profile", canonical.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "compartment",
                    ArrayType(
                        GraphDefinition_Compartment.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "link",
                    ArrayType(
                        GraphDefinition_Link.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
