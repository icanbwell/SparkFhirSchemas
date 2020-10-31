from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.url import url
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.canonical import canonical


# noinspection PyPep8Naming
class RelatedArtifact:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("type", StringType(), True),
                StructField("label", StringType(), True),
                StructField("display", StringType(), True),
                StructField("citation", markdown.get_schema(), True),
                StructField("url", url.get_schema(), True),
                StructField("document", Attachment.get_schema(), True),
                StructField("resource", canonical.get_schema(), True),
            ]
        )

        return schema
