from pyspark.sql.types import ArrayType, DateType, StringType, StructField, StructType


# noinspection PyPep8Naming
class VerificationResult_Attestation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.signature import Signature
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
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "onBehalfOf", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "communicationMethod",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("date", DateType(), True),
                StructField("sourceIdentityCertificate", StringType(), True),
                StructField("proxyIdentityCertificate", StringType(), True),
                StructField(
                    "proxySignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sourceSignature",
                    Signature.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
