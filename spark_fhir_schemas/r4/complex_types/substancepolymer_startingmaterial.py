from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.substanceamount import SubstanceAmount


# noinspection PyPep8Naming
class SubstancePolymer_StartingMaterial:
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
                StructField("material", CodeableConcept.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("isDefining", BooleanType(), True),
                StructField("amount", SubstanceAmount.get_schema(), True),
            ]
        )

        return schema
