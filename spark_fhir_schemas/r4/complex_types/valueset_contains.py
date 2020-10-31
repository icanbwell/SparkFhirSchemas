from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ValueSet_Contains:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.valueset_designation import ValueSet_Designation
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
                    "system", uri.get_schema(recursion_depth + 1), True
                ),
                StructField("abstract", BooleanType(), True),
                StructField("inactive", BooleanType(), True),
                StructField("version", StringType(), True),
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
                StructField("display", StringType(), True),
                StructField(
                    "designation",
                    ArrayType(
                        ValueSet_Designation.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "contains",
                    ArrayType(
                        ValueSet_Contains.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
