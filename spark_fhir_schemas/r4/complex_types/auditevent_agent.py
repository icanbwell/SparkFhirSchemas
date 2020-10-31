from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.auditevent_network import AuditEvent_Network
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


class AuditEvent_Agent:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("role",ArrayType(CodeableConcept.get_schema()), True),
                StructField("who", Reference.get_schema(), True),
                StructField("altId", StringType(), True),
                StructField("name", StringType(), True),
                StructField("requestor", BooleanType(), True),
                StructField("location", Reference.get_schema(), True),
                StructField("policy",ArrayType(uri.get_schema()), True),
                StructField("media", Coding.get_schema(), True),
                StructField("network", AuditEvent_Network.get_schema(), True),
                StructField("purposeOfUse",ArrayType(CodeableConcept.get_schema()), True),
            ]
        )

        return schema
