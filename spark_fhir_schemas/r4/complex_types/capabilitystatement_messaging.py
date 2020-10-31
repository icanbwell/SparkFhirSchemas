from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.capabilitystatement_endpoint import CapabilityStatement_Endpoint
from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.capabilitystatement_supportedmessage import CapabilityStatement_SupportedMessage


# noinspection PyPep8Naming
class CapabilityStatement_Messaging:
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
                StructField(
                    "endpoint",
                    ArrayType(CapabilityStatement_Endpoint.get_schema()), True
                ),
                StructField("reliableCache", unsignedInt.get_schema(), True),
                StructField("documentation", markdown.get_schema(), True),
                StructField(
                    "supportedMessage",
                    ArrayType(
                        CapabilityStatement_SupportedMessage.get_schema()
                    ), True
                ),
            ]
        )

        return schema
