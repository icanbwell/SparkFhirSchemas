from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TerminologyCapabilities_CodeSystem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_version import TerminologyCapabilities_Version
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
                    "uri", canonical.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "version",
                    ArrayType(
                        TerminologyCapabilities_Version.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("subsumption", BooleanType(), True),
            ]
        )

        return schema
