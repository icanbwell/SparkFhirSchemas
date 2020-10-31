from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.terminologycapabilities_filter import TerminologyCapabilities_Filter
from spark_fhir_schemas.r4.complex_types.code import code


class TerminologyCapabilities_Version:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", StringType(), True),
                StructField("isDefault", BooleanType(), True),
                StructField("compositional", BooleanType(), True),
                StructField("language",ArrayType(code.get_schema()), True),
                StructField("filter",ArrayType(TerminologyCapabilities_Filter.get_schema()), True),
                StructField("property",ArrayType(code.get_schema()), True),
            ]
        )

        return schema
