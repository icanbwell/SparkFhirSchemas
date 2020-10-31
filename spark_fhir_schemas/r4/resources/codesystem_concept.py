from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codesystem_designation import CodeSystem_Designation
from spark_fhir_schemas.r4.resources.codesystem_property1 import CodeSystem_Property1
from spark_fhir_schemas.r4.resources.codesystem_concept import CodeSystem_Concept


class CodeSystem_Concept:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("code", code.get_schema(), True),
                StructField("display", StringType(), True),
                StructField("definition", StringType(), True),
                StructField("designation",ArrayType(CodeSystem_Designation.get_schema()), True),
                StructField("property",ArrayType(CodeSystem_Property1.get_schema()), True),
                StructField("concept",ArrayType(CodeSystem_Concept.get_schema()), True),]
        )

        return schema
