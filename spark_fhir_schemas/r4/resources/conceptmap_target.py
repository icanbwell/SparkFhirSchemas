from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.conceptmap_dependson import ConceptMap_DependsOn
from spark_fhir_schemas.r4.resources.conceptmap_dependson import ConceptMap_DependsOn


class ConceptMap_Target:
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
                StructField("equivalence", StringType(), True),
                StructField("comment", StringType(), True),
                StructField("dependsOn",ArrayType(ConceptMap_DependsOn.get_schema()), True),
                StructField("product",ArrayType(ConceptMap_DependsOn.get_schema()), True),]
        )

        return schema
