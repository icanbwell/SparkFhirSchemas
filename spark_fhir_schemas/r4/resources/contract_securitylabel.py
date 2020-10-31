from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.unsignedint import unsignedInt
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.coding import Coding
from spark_fhir_schemas.r4.resources.coding import Coding


class Contract_SecurityLabel:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("number",ArrayType(unsignedInt.get_schema()), True),
                StructField("classification", Coding.get_schema(), True),
                StructField("category",ArrayType(Coding.get_schema()), True),
                StructField("control",ArrayType(Coding.get_schema()), True),]
        )

        return schema
