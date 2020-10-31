from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.coding import Coding


class CodeSystem_Property1:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", code.get_schema(), True),
                StructField("valueCode", StringType(), True),
                StructField("valueCoding", Coding.get_schema(), True),
                StructField("valueString", StringType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField("valueDecimal", IntegerType(), True),]
        )

        return schema
