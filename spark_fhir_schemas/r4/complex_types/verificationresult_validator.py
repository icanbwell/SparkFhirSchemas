from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.signature import Signature


# noinspection PyPep8Naming
class VerificationResult_Validator:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("organization", Reference.get_schema(), True),
                StructField("identityCertificate", StringType(), True),
                StructField(
                    "attestationSignature", Signature.get_schema(), True
                ),
            ]
        )

        return schema
