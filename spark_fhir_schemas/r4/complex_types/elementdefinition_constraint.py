from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ElementDefinition_Constraint:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
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
                StructField("key", id.get_schema(recursion_depth + 1), True),
                StructField("requirements", StringType(), True),
                StructField("severity", StringType(), True),
                StructField("human", StringType(), True),
                StructField("expression", StringType(), True),
                StructField("xpath", StringType(), True),
                StructField(
                    "source", canonical.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
