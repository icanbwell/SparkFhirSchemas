from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Meta:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.coding import Coding
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
                    "versionId", id.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "lastUpdated", instant.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "source", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "profile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "security",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "tag", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )

        return schema
