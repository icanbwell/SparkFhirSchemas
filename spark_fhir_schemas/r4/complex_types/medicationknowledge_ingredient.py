from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.ratio import Ratio


# noinspection PyPep8Naming
class MedicationKnowledge_Ingredient:
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
                StructField(
                    "itemCodeableConcept", CodeableConcept.get_schema(), True
                ),
                StructField("itemReference", Reference.get_schema(), True),
                StructField("isActive", BooleanType(), True),
                StructField("strength", Ratio.get_schema(), True),
            ]
        )

        return schema
