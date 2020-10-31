from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Signature:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.base64binary import base64Binary
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
                    "type", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "when", instant.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "onBehalfOf", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "targetFormat", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sigFormat", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "data", base64Binary.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
