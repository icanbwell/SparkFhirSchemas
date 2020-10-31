from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.datetime import dateTime


# noinspection PyPep8Naming
class VerificationResult_PrimarySource:
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
                StructField("who", Reference.get_schema(), True),
                StructField(
                    "type", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "communicationMethod",
                    ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "validationStatus", CodeableConcept.get_schema(), True
                ),
                StructField("validationDate", dateTime.get_schema(), True),
                StructField(
                    "canPushUpdates", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "pushTypeAvailable",
                    ArrayType(CodeableConcept.get_schema()), True
                ),
            ]
        )

        return schema
