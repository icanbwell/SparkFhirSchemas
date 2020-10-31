from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.valueset_concept import ValueSet_Concept
from spark_fhir_schemas.r4.complex_types.valueset_filter import ValueSet_Filter
from spark_fhir_schemas.r4.complex_types.canonical import canonical


# noinspection PyPep8Naming
class ValueSet_Include:
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
                StructField("system", uri.get_schema(), True),
                StructField("version", StringType(), True),
                StructField(
                    "concept", ArrayType(ValueSet_Concept.get_schema()), True
                ),
                StructField(
                    "filter", ArrayType(ValueSet_Filter.get_schema()), True
                ),
                StructField(
                    "valueSet", ArrayType(canonical.get_schema()), True
                ),
            ]
        )

        return schema
