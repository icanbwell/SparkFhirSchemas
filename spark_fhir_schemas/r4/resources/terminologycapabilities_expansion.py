from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.terminologycapabilities_parameter import TerminologyCapabilities_Parameter
from spark_fhir_schemas.r4.resources.markdown import markdown


class TerminologyCapabilities_Expansion:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("hierarchical", BooleanType(), True),
                StructField("paging", BooleanType(), True),
                StructField("incomplete", BooleanType(), True),
                StructField("parameter",ArrayType(TerminologyCapabilities_Parameter.get_schema()), True),
                StructField("textFilter", markdown.get_schema(), True),]
        )

        return schema
