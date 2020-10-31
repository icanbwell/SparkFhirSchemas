from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.period import Period


# noinspection PyPep8Naming
class BiologicallyDerivedProduct_Storage:
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
                StructField("description", StringType(), True),
                StructField("temperature", decimal.get_schema(), True),
                StructField("scale", StringType(), True),
                StructField("duration", Period.get_schema(), True),
            ]
        )

        return schema
