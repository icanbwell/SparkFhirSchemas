from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.duration import Duration


# noinspection PyPep8Naming
class PlanDefinition_Target:
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
                StructField("measure", CodeableConcept.get_schema(), True),
                StructField("detailQuantity", Quantity.get_schema(), True),
                StructField("detailRange", Range.get_schema(), True),
                StructField(
                    "detailCodeableConcept", CodeableConcept.get_schema(), True
                ),
                StructField("due", Duration.get_schema(), True),
            ]
        )

        return schema
