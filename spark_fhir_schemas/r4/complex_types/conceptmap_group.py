from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.conceptmap_element import ConceptMap_Element
from spark_fhir_schemas.r4.complex_types.conceptmap_unmapped import ConceptMap_Unmapped


class ConceptMap_Group:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("source", uri.get_schema(), True),
                StructField("sourceVersion", StringType(), True),
                StructField("target", uri.get_schema(), True),
                StructField("targetVersion", StringType(), True),
                StructField("element",ArrayType(ConceptMap_Element.get_schema()), True),
                StructField("unmapped", ConceptMap_Unmapped.get_schema(), True),
            ]
        )

        return schema
