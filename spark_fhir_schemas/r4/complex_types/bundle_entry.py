from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Bundle_Entry:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.bundle_link import Bundle_Link
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.bundle_search import Bundle_Search
        from spark_fhir_schemas.r4.complex_types.bundle_request import Bundle_Request
        from spark_fhir_schemas.r4.complex_types.bundle_response import Bundle_Response
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
                    "link",
                    ArrayType(Bundle_Link.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "fullUrl", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resource", ResourceList.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "search", Bundle_Search.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "request", Bundle_Request.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "response",
                    Bundle_Response.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
