from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.timing import Timing
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.ratio import Ratio


# noinspection PyPep8Naming
class NutritionOrder_Administration:
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
                StructField("schedule", Timing.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("rateQuantity", Quantity.get_schema(), True),
                StructField("rateRatio", Ratio.get_schema(), True),
            ]
        )

        return schema
