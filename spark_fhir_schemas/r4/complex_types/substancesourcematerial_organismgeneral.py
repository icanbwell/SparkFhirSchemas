from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


# noinspection PyPep8Naming
class SubstanceSourceMaterial_OrganismGeneral:
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
                StructField("kingdom", CodeableConcept.get_schema(), True),
                StructField("phylum", CodeableConcept.get_schema(), True),
                StructField("class", CodeableConcept.get_schema(), True),
                StructField("order", CodeableConcept.get_schema(), True),
            ]
        )

        return schema
