from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.substancesourcematerial_author import SubstanceSourceMaterial_Author
from spark_fhir_schemas.r4.complex_types.substancesourcematerial_hybrid import SubstanceSourceMaterial_Hybrid
from spark_fhir_schemas.r4.complex_types.substancesourcematerial_organismgeneral import SubstanceSourceMaterial_OrganismGeneral


# noinspection PyPep8Naming
class SubstanceSourceMaterial_Organism:
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
                StructField("family", CodeableConcept.get_schema(), True),
                StructField("genus", CodeableConcept.get_schema(), True),
                StructField("species", CodeableConcept.get_schema(), True),
                StructField(
                    "intraspecificType", CodeableConcept.get_schema(), True
                ),
                StructField("intraspecificDescription", StringType(), True),
                StructField(
                    "author",
                    ArrayType(SubstanceSourceMaterial_Author.get_schema()),
                    True
                ),
                StructField(
                    "hybrid", SubstanceSourceMaterial_Hybrid.get_schema(), True
                ),
                StructField(
                    "organismGeneral",
                    SubstanceSourceMaterial_OrganismGeneral.get_schema(), True
                ),
            ]
        )

        return schema
