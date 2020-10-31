from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
from spark_fhir_schemas.r4.complex_types.instant import instant
from spark_fhir_schemas.r4.complex_types.subscription_channel import Subscription_Channel


# noinspection PyPep8Naming
class Subscription:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "contact", ArrayType(ContactPoint.get_schema()), True
                ),
                StructField("end", instant.get_schema(), True),
                StructField("reason", StringType(), True),
                StructField("criteria", StringType(), True),
                StructField("error", StringType(), True),
                StructField(
                    "channel", Subscription_Channel.get_schema(), True
                ),
            ]
        )

        return schema
