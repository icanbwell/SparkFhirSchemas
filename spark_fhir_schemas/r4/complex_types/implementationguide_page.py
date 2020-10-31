from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.implementationguide_page import ImplementationGuide_Page


class ImplementationGuide_Page:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("nameUrl", StringType(), True),
                StructField("nameReference", Reference.get_schema(), True),
                StructField("title", StringType(), True),
                StructField("generation", StringType(), True),
                StructField("page",ArrayType(ImplementationGuide_Page.get_schema()), True),
            ]
        )

        return schema
