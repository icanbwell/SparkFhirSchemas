from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ImagingStudy_Instance:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
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
                StructField("uid", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "sopClass", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "number", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField("title", StringType(), True),
            ]
        )

        return schema
