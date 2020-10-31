from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CapabilityStatement_Resource:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_interaction import CapabilityStatement_Interaction
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_searchparam import CapabilityStatement_SearchParam
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_operation import CapabilityStatement_Operation
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
                StructField(
                    "profile", canonical.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "supportedProfile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "documentation", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "interaction",
                    ArrayType(
                        CapabilityStatement_Interaction.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("versioning", StringType(), True),
                StructField("readHistory", BooleanType(), True),
                StructField("updateCreate", BooleanType(), True),
                StructField("conditionalCreate", BooleanType(), True),
                StructField("conditionalRead", StringType(), True),
                StructField("conditionalUpdate", BooleanType(), True),
                StructField("conditionalDelete", StringType(), True),
                StructField("searchInclude", ArrayType(StringType()), True),
                StructField("searchRevInclude", ArrayType(StringType()), True),
                StructField(
                    "searchParam",
                    ArrayType(
                        CapabilityStatement_SearchParam.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "operation",
                    ArrayType(
                        CapabilityStatement_Operation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
