from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.base64binary import base64Binary
from spark_fhir_schemas.r4.resources.auditevent_detail import AuditEvent_Detail


class AuditEvent_Entity:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("what", Reference.get_schema(), True),
                StructField("type", Coding.get_schema(), True),
                StructField("role", Coding.get_schema(), True),
                StructField("lifecycle", Coding.get_schema(), True),
                StructField("securityLabel",ArrayType(Coding.get_schema()), True),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField("query", base64Binary.get_schema(), True),
                StructField("detail",ArrayType(AuditEvent_Detail.get_schema()), True),]
        )

        return schema
