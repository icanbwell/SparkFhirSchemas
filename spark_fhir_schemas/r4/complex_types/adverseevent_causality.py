from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class AdverseEvent_Causality:
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
                StructField("assessment", CodeableConcept.get_schema(), True),
                StructField("productRelatedness", StringType(), True),
                StructField("author", Reference.get_schema(), True),
                StructField("method", CodeableConcept.get_schema(), True),
            ]
        )

        return schema
