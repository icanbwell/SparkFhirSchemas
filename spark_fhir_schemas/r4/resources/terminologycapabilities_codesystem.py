from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.terminologycapabilities_version import TerminologyCapabilities_Version
from spark_fhir_schemas.r4.resources.boolean import boolean


class TerminologyCapabilities_CodeSystem:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("uri", canonical.get_schema(), True),
                StructField("version",ArrayType(TerminologyCapabilities_Version.get_schema()), True),
                StructField("subsumption", BooleanType(), True),]
        )

        return schema
