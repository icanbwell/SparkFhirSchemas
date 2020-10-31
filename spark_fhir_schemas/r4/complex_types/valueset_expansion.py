from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.valueset_parameter import ValueSet_Parameter
from spark_fhir_schemas.r4.complex_types.valueset_contains import ValueSet_Contains


# noinspection PyPep8Naming
class ValueSet_Expansion:
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
                StructField("identifier", uri.get_schema(), True),
                StructField("timestamp", dateTime.get_schema(), True),
                StructField("total", integer.get_schema(), True),
                StructField("offset", integer.get_schema(), True),
                StructField(
                    "parameter", ArrayType(ValueSet_Parameter.get_schema()),
                    True
                ),
                StructField(
                    "contains", ArrayType(ValueSet_Contains.get_schema()), True
                ),
            ]
        )

        return schema
