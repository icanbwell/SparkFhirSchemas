from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.instant import instant
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.coding import Coding


class Meta:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("versionId", id.get_schema(), True),
                StructField("lastUpdated", instant.get_schema(), True),
                StructField("source", uri.get_schema(), True),
                StructField("profile",ArrayType(canonical.get_schema()), True),
                StructField("security",ArrayType(Coding.get_schema()), True),
                StructField("tag",ArrayType(Coding.get_schema()), True),]
        )

        return schema
