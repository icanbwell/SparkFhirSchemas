from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Bundle:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.bundle_link import Bundle_Link
        from spark_fhir_schemas.r4.complex_types.bundle_entry import Bundle_Entry
        from spark_fhir_schemas.r4.complex_types.signature import Signature
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("type", StringType(), True),
                StructField(
                    "timestamp", instant.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "total", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "link",
                    ArrayType(Bundle_Link.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "entry",
                    ArrayType(Bundle_Entry.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "signature", Signature.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
