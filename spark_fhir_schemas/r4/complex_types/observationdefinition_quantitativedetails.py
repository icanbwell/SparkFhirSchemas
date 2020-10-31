from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.integer import integer


# noinspection PyPep8Naming
class ObservationDefinition_QuantitativeDetails:
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
                    "customaryUnit", CodeableConcept.get_schema(), True
                ),
                StructField("unit", CodeableConcept.get_schema(), True),
                StructField("conversionFactor", decimal.get_schema(), True),
                StructField("decimalPrecision", integer.get_schema(), True),
            ]
        )

        return schema
