from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.id import id


class TestScript_Assert:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("label", StringType(), True),
                StructField("description", StringType(), True),
                StructField("direction", StringType(), True),
                StructField("compareToSourceId", StringType(), True),
                StructField("compareToSourceExpression", StringType(), True),
                StructField("compareToSourcePath", StringType(), True),
                StructField("contentType", code.get_schema(), True),
                StructField("expression", StringType(), True),
                StructField("headerField", StringType(), True),
                StructField("minimumId", StringType(), True),
                StructField("navigationLinks", BooleanType(), True),
                StructField("operator", StringType(), True),
                StructField("path", StringType(), True),
                StructField("requestMethod", StringType(), True),
                StructField("requestURL", StringType(), True),
                StructField("resource", code.get_schema(), True),
                StructField("response", StringType(), True),
                StructField("responseCode", StringType(), True),
                StructField("sourceId", id.get_schema(), True),
                StructField("validateProfileId", id.get_schema(), True),
                StructField("value", StringType(), True),
                StructField("warningOnly", BooleanType(), True),
            ]
        )

        return schema
