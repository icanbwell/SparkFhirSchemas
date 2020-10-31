from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.quantity import Quantity


# noinspection PyPep8Naming
class SubstanceSpecification_Moiety:
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
                StructField("role", CodeableConcept.get_schema(), True),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("name", StringType(), True),
                StructField(
                    "stereochemistry", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "opticalActivity", CodeableConcept.get_schema(), True
                ),
                StructField("molecularFormula", StringType(), True),
                StructField("amountQuantity", Quantity.get_schema(), True),
                StructField("amountString", StringType(), True),
            ]
        )

        return schema
