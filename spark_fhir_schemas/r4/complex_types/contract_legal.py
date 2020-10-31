from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.attachment import Attachment
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Contract_Legal:
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
                    "contentAttachment", Attachment.get_schema(), True
                ),
                StructField("contentReference", Reference.get_schema(), True),
            ]
        )

        return schema
