from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.integer import integer
from spark_fhir_schemas.r4.resources.valueset_parameter import ValueSet_Parameter
from spark_fhir_schemas.r4.resources.valueset_contains import ValueSet_Contains


class ValueSet_Expansion:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier", uri.get_schema(), True),
                StructField("timestamp", dateTime.get_schema(), True),
                StructField("total", integer.get_schema(), True),
                StructField("offset", integer.get_schema(), True),
                StructField("parameter",ArrayType(ValueSet_Parameter.get_schema()), True),
                StructField("contains",ArrayType(ValueSet_Contains.get_schema()), True),]
        )

        return schema
