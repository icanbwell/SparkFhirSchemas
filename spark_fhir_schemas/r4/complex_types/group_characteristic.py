from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period


# noinspection PyPep8Naming
class Group_Characteristic:
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
                StructField("code", CodeableConcept.get_schema(), True),
                StructField(
                    "valueCodeableConcept", CodeableConcept.get_schema(), True
                ),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueQuantity", Quantity.get_schema(), True),
                StructField("valueRange", Range.get_schema(), True),
                StructField("valueReference", Reference.get_schema(), True),
                StructField("exclude", BooleanType(), True),
                StructField("period", Period.get_schema(), True),
            ]
        )

        return schema
