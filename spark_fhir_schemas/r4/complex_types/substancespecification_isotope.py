from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.quantity import Quantity
from spark_fhir_schemas.r4.complex_types.substancespecification_molecularweight import SubstanceSpecification_MolecularWeight


# noinspection PyPep8Naming
class SubstanceSpecification_Isotope:
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
                StructField("identifier", Identifier.get_schema(), True),
                StructField("name", CodeableConcept.get_schema(), True),
                StructField(
                    "substitution", CodeableConcept.get_schema(), True
                ),
                StructField("halfLife", Quantity.get_schema(), True),
                StructField(
                    "molecularWeight",
                    SubstanceSpecification_MolecularWeight.get_schema(), True
                ),
            ]
        )

        return schema
