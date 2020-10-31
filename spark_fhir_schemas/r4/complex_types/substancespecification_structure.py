from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.substancespecification_isotope import SubstanceSpecification_Isotope
from spark_fhir_schemas.r4.complex_types.substancespecification_molecularweight import SubstanceSpecification_MolecularWeight
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.substancespecification_representation import SubstanceSpecification_Representation


# noinspection PyPep8Naming
class SubstanceSpecification_Structure:
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
                    "stereochemistry", CodeableConcept.get_schema(), True
                ),
                StructField(
                    "opticalActivity", CodeableConcept.get_schema(), True
                ),
                StructField("molecularFormula", StringType(), True),
                StructField("molecularFormulaByMoiety", StringType(), True),
                StructField(
                    "isotope",
                    ArrayType(SubstanceSpecification_Isotope.get_schema()),
                    True
                ),
                StructField(
                    "molecularWeight",
                    SubstanceSpecification_MolecularWeight.get_schema(), True
                ),
                StructField("source", ArrayType(Reference.get_schema()), True),
                StructField(
                    "representation",
                    ArrayType(
                        SubstanceSpecification_Representation.get_schema()
                    ), True
                ),
            ]
        )

        return schema
