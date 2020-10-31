from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.bundle_link import Bundle_Link
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.bundle_search import Bundle_Search
from spark_fhir_schemas.r4.complex_types.bundle_request import Bundle_Request
from spark_fhir_schemas.r4.complex_types.bundle_response import Bundle_Response


class Bundle_Entry:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("link",ArrayType(Bundle_Link.get_schema()), True),
                StructField("fullUrl", uri.get_schema(), True),
                StructField("resource", ResourceList.get_schema(), True),
                StructField("search", Bundle_Search.get_schema(), True),
                StructField("request", Bundle_Request.get_schema(), True),
                StructField("response", Bundle_Response.get_schema(), True),
            ]
        )

        return schema
