from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.duration import Duration


# noinspection PyPep8Naming
class SpecimenDefinition_Handling:
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
                    "temperatureQualifier", CodeableConcept.get_schema(), True
                ),
                StructField("temperatureRange", Range.get_schema(), True),
                StructField("maxDuration", Duration.get_schema(), True),
                StructField("instruction", StringType(), True),
            ]
        )

        return schema
