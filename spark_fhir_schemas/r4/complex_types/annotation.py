from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.markdown import markdown


# noinspection PyPep8Naming
class Annotation:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField("authorReference", Reference.get_schema(), True),
                StructField("authorString", StringType(), True),
                StructField("time", dateTime.get_schema(), True),
                StructField("text", markdown.get_schema(), True),
            ]
        )

        return schema
