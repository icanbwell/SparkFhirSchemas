from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.structuremap_source import StructureMap_Source
from spark_fhir_schemas.r4.resources.structuremap_target import StructureMap_Target
from spark_fhir_schemas.r4.resources.structuremap_rule import StructureMap_Rule
from spark_fhir_schemas.r4.resources.structuremap_dependent import StructureMap_Dependent
from spark_fhir_schemas.r4.resources.string import string


class StructureMap_Rule:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("name", id.get_schema(), True),
                StructField("source",ArrayType(StructureMap_Source.get_schema()), True),
                StructField("target",ArrayType(StructureMap_Target.get_schema()), True),
                StructField("rule",ArrayType(StructureMap_Rule.get_schema()), True),
                StructField("dependent",ArrayType(StructureMap_Dependent.get_schema()), True),
                StructField("documentation", StringType(), True),]
        )

        return schema
