from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class ObservationDefinition_QualifiedInterval:
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
                StructField("category", StringType(), True),
                StructField("range", Range.get_schema(), True),
                StructField("context", CodeableConcept.get_schema(), True),
                StructField(
                    "appliesTo", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField("gender", StringType(), True),
                StructField("age", Range.get_schema(), True),
                StructField("gestationalAge", Range.get_schema(), True),
                StructField("condition", StringType(), True),
            ]
        )

        return schema
