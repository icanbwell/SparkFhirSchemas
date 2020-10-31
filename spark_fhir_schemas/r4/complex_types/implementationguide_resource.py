from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ImplementationGuide_Resource:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                    "reference", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField("exampleBoolean", BooleanType(), True),
                StructField("exampleCanonical", StringType(), True),
                StructField(
                    "groupingId", id.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
