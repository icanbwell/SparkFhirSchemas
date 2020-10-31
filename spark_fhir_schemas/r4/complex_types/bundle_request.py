from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Bundle_Request:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.instant import instant
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
                StructField("method", StringType(), True),
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField("ifNoneMatch", StringType(), True),
                StructField(
                    "ifModifiedSince", instant.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("ifMatch", StringType(), True),
                StructField("ifNoneExist", StringType(), True),
            ]
        )

        return schema
