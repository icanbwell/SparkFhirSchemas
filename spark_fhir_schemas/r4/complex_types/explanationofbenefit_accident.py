from pyspark.sql.types import ArrayType, DateType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.address import Address
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class ExplanationOfBenefit_Accident:
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
                StructField("date", DateType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("locationAddress", Address.get_schema(), True),
                StructField("locationReference", Reference.get_schema(), True),
            ]
        )

        return schema
