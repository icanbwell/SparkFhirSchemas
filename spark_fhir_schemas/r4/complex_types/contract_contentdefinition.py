from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.markdown import markdown


# noinspection PyPep8Naming
class Contract_ContentDefinition:
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
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("subType", CodeableConcept.get_schema(), True),
                StructField("publisher", Reference.get_schema(), True),
                StructField("publicationDate", dateTime.get_schema(), True),
                StructField("publicationStatus", code.get_schema(), True),
                StructField("copyright", markdown.get_schema(), True),
            ]
        )

        return schema
