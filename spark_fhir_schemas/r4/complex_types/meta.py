from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.instant import instant
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.coding import Coding


# noinspection PyPep8Naming
class Meta:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("versionId", id.get_schema(), True),
                StructField("lastUpdated", instant.get_schema(), True),
                StructField("source", uri.get_schema(), True),
                StructField(
                    "profile", ArrayType(canonical.get_schema()), True
                ),
                StructField("security", ArrayType(Coding.get_schema()), True),
                StructField("tag", ArrayType(Coding.get_schema()), True),
            ]
        )

        return schema
