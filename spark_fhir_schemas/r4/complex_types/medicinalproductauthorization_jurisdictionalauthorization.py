from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period


# noinspection PyPep8Naming
class MedicinalProductAuthorization_JurisdictionalAuthorization:
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
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("country", CodeableConcept.get_schema(), True),
                StructField(
                    "jurisdiction", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField(
                    "legalStatusOfSupply", CodeableConcept.get_schema(), True
                ),
                StructField("validityPeriod", Period.get_schema(), True),
            ]
        )

        return schema
