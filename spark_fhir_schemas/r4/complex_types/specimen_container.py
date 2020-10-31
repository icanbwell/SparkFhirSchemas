from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class Specimen_Container:
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
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("description", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("capacity", Quantity.get_schema(), True),
                StructField("specimenQuantity", Quantity.get_schema(), True),
                StructField(
                    "additiveCodeableConcept", CodeableConcept.get_schema(),
                    True
                ),
                StructField("additiveReference", Reference.get_schema(), True),
            ]
        )

        return schema
