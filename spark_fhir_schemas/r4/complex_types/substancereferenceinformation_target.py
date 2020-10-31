from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.range import Range
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class SubstanceReferenceInformation_Target:
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
                StructField("target", Identifier.get_schema(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("interaction", CodeableConcept.get_schema(), True),
                StructField("organism", CodeableConcept.get_schema(), True),
                StructField(
                    "organismType", CodeableConcept.get_schema(), True
                ),
                StructField("amountQuantity", Quantity.get_schema(), True),
                StructField("amountRange", Range.get_schema(), True),
                StructField("amountString", StringType(), True),
                StructField("amountType", CodeableConcept.get_schema(), True),
                StructField("source", ArrayType(Reference.get_schema()), True),
            ]
        )

        return schema
