from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.unsignedint import unsignedInt
from spark_fhir_schemas.r4.resources.bundle_link import Bundle_Link
from spark_fhir_schemas.r4.resources.bundle_entry import Bundle_Entry
from spark_fhir_schemas.r4.resources.signature import Signature


class Bundle:
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
                StructField("identifier", Identifier.get_schema(), True),
                StructField("type", StringType(), True),
                StructField("timestamp", instant.get_schema(), True),
                StructField("total", unsignedInt.get_schema(), True),
                StructField("link",ArrayType(Bundle_Link.get_schema()), True),
                StructField("entry",ArrayType(Bundle_Entry.get_schema()), True),
                StructField("signature", Signature.get_schema(), True),]
        )

        return schema
