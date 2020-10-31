from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.ratio import Ratio


# noinspection PyPep8Naming
class SubstanceSpecification_Relationship:
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
                    "substanceReference", Reference.get_schema(), True
                ),
                StructField(
                    "substanceCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField(
                    "relationship", CodeableConcept.get_schema(), True
                ),
                StructField("isDefining", BooleanType(), True),
                StructField("amountQuantity", Quantity.get_schema(), True),
                StructField("amountRange", Range.get_schema(), True),
                StructField("amountRatio", Ratio.get_schema(), True),
                StructField("amountString", StringType(), True),
                StructField("amountRatioLowLimit", Ratio.get_schema(), True),
                StructField("amountType", CodeableConcept.get_schema(), True),
                StructField("source", ArrayType(Reference.get_schema()), True),
            ]
        )

        return schema
