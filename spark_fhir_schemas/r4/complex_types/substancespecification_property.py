from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.quantity import Quantity


# noinspection PyPep8Naming
class SubstanceSpecification_Property:
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
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("parameters", StringType(), True),
                StructField(
                    "definingSubstanceReference", Reference.get_schema(), True
                ),
                StructField(
                    "definingSubstanceCodeableConcept",
                    CodeableConcept.get_schema(), True
                ),
                StructField("amountQuantity", Quantity.get_schema(), True),
                StructField("amountString", StringType(), True),
            ]
        )

        return schema
