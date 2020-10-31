from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.implementationguide_grouping import ImplementationGuide_Grouping
from spark_fhir_schemas.r4.resources.implementationguide_resource import ImplementationGuide_Resource
from spark_fhir_schemas.r4.resources.implementationguide_page import ImplementationGuide_Page
from spark_fhir_schemas.r4.resources.implementationguide_parameter import ImplementationGuide_Parameter
from spark_fhir_schemas.r4.resources.implementationguide_template import ImplementationGuide_Template


class ImplementationGuide_Definition:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("grouping",ArrayType(ImplementationGuide_Grouping.get_schema()), True),
                StructField("resource",ArrayType(ImplementationGuide_Resource.get_schema()), True),
                StructField("page", ImplementationGuide_Page.get_schema(), True),
                StructField("parameter",ArrayType(ImplementationGuide_Parameter.get_schema()), True),
                StructField("template",ArrayType(ImplementationGuide_Template.get_schema()), True),]
        )

        return schema
