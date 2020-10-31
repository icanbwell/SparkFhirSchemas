from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class AuditEvent_Agent:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.auditevent_network import AuditEvent_Network
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
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "role",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("altId", StringType(), True),
                StructField("name", StringType(), True),
                StructField("requestor", BooleanType(), True),
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "policy", ArrayType(uri.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "media", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "network",
                    AuditEvent_Network.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "purposeOfUse",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )

        return schema
