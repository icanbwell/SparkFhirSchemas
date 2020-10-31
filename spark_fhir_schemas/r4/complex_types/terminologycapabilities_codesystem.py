from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.terminologycapabilities_version import TerminologyCapabilities_Version


# noinspection PyPep8Naming
class TerminologyCapabilities_CodeSystem:
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
                StructField("uri", canonical.get_schema(), True),
                StructField(
                    "version",
                    ArrayType(TerminologyCapabilities_Version.get_schema()),
                    True
                ),
                StructField("subsumption", BooleanType(), True),
            ]
        )

        return schema
