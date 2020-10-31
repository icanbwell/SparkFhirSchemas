from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class OperationDefinition_Parameter:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.operationdefinition_binding import OperationDefinition_Binding
        from spark_fhir_schemas.r4.complex_types.operationdefinition_referencedfrom import OperationDefinition_ReferencedFrom
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
                    "name", code.get_schema(recursion_depth + 1), True
                ),
                StructField("use", StringType(), True),
                StructField(
                    "min", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("max", StringType(), True),
                StructField("documentation", StringType(), True),
                StructField(
                    "type", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "targetProfile",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField("searchType", StringType(), True),
                StructField(
                    "binding",
                    OperationDefinition_Binding.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "referencedFrom",
                    ArrayType(
                        OperationDefinition_ReferencedFrom.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "part",
                    ArrayType(
                        OperationDefinition_Parameter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
