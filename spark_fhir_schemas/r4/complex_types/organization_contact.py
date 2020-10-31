from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.humanname import HumanName
from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
from spark_fhir_schemas.r4.complex_types.address import Address


# noinspection PyPep8Naming
class Organization_Contact:
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
                StructField("purpose", CodeableConcept.get_schema(), True),
                StructField("name", HumanName.get_schema(), True),
                StructField(
                    "telecom", ArrayType(ContactPoint.get_schema()), True
                ),
                StructField("address", Address.get_schema(), True),
            ]
        )

        return schema
