from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.structuremap_input import StructureMap_Input
from spark_fhir_schemas.r4.resources.structuremap_rule import StructureMap_Rule


class StructureMap_Group:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("name", id.get_schema(), True),
                StructField("extends", id.get_schema(), True),
                StructField("typeMode", StringType(), True),
                StructField("documentation", StringType(), True),
                StructField("input",ArrayType(StructureMap_Input.get_schema()), True),
                StructField("rule",ArrayType(StructureMap_Rule.get_schema()), True),]
        )

        return schema
