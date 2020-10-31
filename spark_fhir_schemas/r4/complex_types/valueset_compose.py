from pyspark.sql.types import ArrayType, BooleanType, DateType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ValueSet_Compose:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.valueset_include import ValueSet_Include
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
                StructField("lockedDate", DateType(), True),
                StructField("inactive", BooleanType(), True),
                StructField(
                    "include",
                    ArrayType(
                        ValueSet_Include.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "exclude",
                    ArrayType(
                        ValueSet_Include.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
