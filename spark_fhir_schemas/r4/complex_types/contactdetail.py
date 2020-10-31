from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint


# noinspection PyPep8Naming
class ContactDetail:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("name", StringType(), True),
                StructField(
                    "telecom", ArrayType(ContactPoint.get_schema()), True
                ),
            ]
        )

        return schema
