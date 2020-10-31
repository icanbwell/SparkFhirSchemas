from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TestScript_Operation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.testscript_requestheader import TestScript_RequestHeader
        from spark_fhir_schemas.r4.complex_types.id import id
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
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
                    "type", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resource", code.get_schema(recursion_depth + 1), True
                ),
                StructField("label", StringType(), True),
                StructField("description", StringType(), True),
                StructField(
                    "accept", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contentType", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "destination", integer.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("encodeRequestUrl", BooleanType(), True),
                StructField("method", StringType(), True),
                StructField(
                    "origin", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("params", StringType(), True),
                StructField(
                    "requestHeader",
                    ArrayType(
                        TestScript_RequestHeader.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "requestId", id.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "responseId", id.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sourceId", id.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "targetId", id.get_schema(recursion_depth + 1), True
                ),
                StructField("url", StringType(), True),
            ]
        )

        return schema
