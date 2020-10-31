from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.markdown import markdown
from spark_fhir_schemas.r4.complex_types.capabilitystatement_security import CapabilityStatement_Security
from spark_fhir_schemas.r4.complex_types.capabilitystatement_resource import CapabilityStatement_Resource
from spark_fhir_schemas.r4.complex_types.capabilitystatement_interaction1 import CapabilityStatement_Interaction1
from spark_fhir_schemas.r4.complex_types.capabilitystatement_searchparam import CapabilityStatement_SearchParam
from spark_fhir_schemas.r4.complex_types.capabilitystatement_operation import CapabilityStatement_Operation
from spark_fhir_schemas.r4.complex_types.canonical import canonical


# noinspection PyPep8Naming
class CapabilityStatement_Rest:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("mode", StringType(), True),
                StructField("documentation", markdown.get_schema(), True),
                StructField(
                    "security", CapabilityStatement_Security.get_schema(), True
                ),
                StructField(
                    "resource",
                    ArrayType(CapabilityStatement_Resource.get_schema()), True
                ),
                StructField(
                    "interaction",
                    ArrayType(CapabilityStatement_Interaction1.get_schema()),
                    True
                ),
                StructField(
                    "searchParam",
                    ArrayType(CapabilityStatement_SearchParam.get_schema()),
                    True
                ),
                StructField(
                    "operation",
                    ArrayType(CapabilityStatement_Operation.get_schema()), True
                ),
                StructField(
                    "compartment", ArrayType(canonical.get_schema()), True
                ),
            ]
        )

        return schema
