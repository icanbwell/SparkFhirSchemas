from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.medicinalproduct_namepart import MedicinalProduct_NamePart
from spark_fhir_schemas.r4.complex_types.medicinalproduct_countrylanguage import MedicinalProduct_CountryLanguage


# noinspection PyPep8Naming
class MedicinalProduct_Name:
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
                StructField("productName", StringType(), True),
                StructField(
                    "namePart",
                    ArrayType(MedicinalProduct_NamePart.get_schema()), True
                ),
                StructField(
                    "countryLanguage",
                    ArrayType(MedicinalProduct_CountryLanguage.get_schema()),
                    True
                ),
            ]
        )

        return schema
