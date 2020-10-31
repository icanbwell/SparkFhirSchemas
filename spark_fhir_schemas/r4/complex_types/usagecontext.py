from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class UsageContext:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("code", Coding.get_schema(), True),
                StructField(
                    "valueCodeableConcept", CodeableConcept.get_schema(), True
                ),
                StructField("valueQuantity", Quantity.get_schema(), True),
                StructField("valueRange", Range.get_schema(), True),
                StructField("valueReference", Reference.get_schema(), True),
            ]
        )

        return schema
