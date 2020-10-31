from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class ExplanationOfBenefit_CareTeam:
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
                StructField("sequence", positiveInt.get_schema(), True),
                StructField("provider", Reference.get_schema(), True),
                StructField("responsible", BooleanType(), True),
                StructField("role", CodeableConcept.get_schema(), True),
                StructField(
                    "qualification", CodeableConcept.get_schema(), True
                ),
            ]
        )

        return schema
