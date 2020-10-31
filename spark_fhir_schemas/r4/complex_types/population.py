from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class Population:
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
                StructField("ageRange", Range.get_schema(), True),
                StructField(
                    "ageCodeableConcept", CodeableConcept.get_schema(), True
                ),
                StructField("gender", CodeableConcept.get_schema(), True),
                StructField("race", CodeableConcept.get_schema(), True),
                StructField(
                    "physiologicalCondition", CodeableConcept.get_schema(),
                    True
                ),
            ]
        )

        return schema
