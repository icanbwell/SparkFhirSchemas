from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.url import url
from spark_fhir_schemas.r4.complex_types.implementationguide_resource1 import ImplementationGuide_Resource1
from spark_fhir_schemas.r4.complex_types.implementationguide_page1 import ImplementationGuide_Page1


# noinspection PyPep8Naming
class ImplementationGuide_Manifest:
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
                StructField("rendering", url.get_schema(), True),
                StructField(
                    "resource",
                    ArrayType(ImplementationGuide_Resource1.get_schema()), True
                ),
                StructField(
                    "page", ArrayType(ImplementationGuide_Page1.get_schema()),
                    True
                ),
                StructField("image", ArrayType(StringType()), True),
                StructField("other", ArrayType(StringType()), True),
            ]
        )

        return schema
