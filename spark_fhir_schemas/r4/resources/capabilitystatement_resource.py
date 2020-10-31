from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.canonical import canonical
from spark_fhir_schemas.r4.resources.markdown import markdown
from spark_fhir_schemas.r4.resources.capabilitystatement_interaction import CapabilityStatement_Interaction
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.capabilitystatement_searchparam import CapabilityStatement_SearchParam
from spark_fhir_schemas.r4.resources.capabilitystatement_operation import CapabilityStatement_Operation


class CapabilityStatement_Resource:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", code.get_schema(), True),
                StructField("profile", canonical.get_schema(), True),
                StructField("supportedProfile",ArrayType(canonical.get_schema()), True),
                StructField("documentation", markdown.get_schema(), True),
                StructField("interaction",ArrayType(CapabilityStatement_Interaction.get_schema()), True),
                StructField("versioning", StringType(), True),
                StructField("readHistory", BooleanType(), True),
                StructField("updateCreate", BooleanType(), True),
                StructField("conditionalCreate", BooleanType(), True),
                StructField("conditionalRead", StringType(), True),
                StructField("conditionalUpdate", BooleanType(), True),
                StructField("conditionalDelete", StringType(), True),
                StructField("referencePolicy",ArrayType(None.get_schema()), True),
                StructField("searchInclude",ArrayType(string.get_schema()), True),
                StructField("searchRevInclude",ArrayType(string.get_schema()), True),
                StructField("searchParam",ArrayType(CapabilityStatement_SearchParam.get_schema()), True),
                StructField("operation",ArrayType(CapabilityStatement_Operation.get_schema()), True),]
        )

        return schema
