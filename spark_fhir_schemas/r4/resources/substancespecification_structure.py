from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.substancespecification_isotope import SubstanceSpecification_Isotope
from spark_fhir_schemas.r4.resources.substancespecification_molecularweight import SubstanceSpecification_MolecularWeight
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.substancespecification_representation import SubstanceSpecification_Representation


class SubstanceSpecification_Structure:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("stereochemistry", CodeableConcept.get_schema(), True),
                StructField("opticalActivity", CodeableConcept.get_schema(), True),
                StructField("molecularFormula", StringType(), True),
                StructField("molecularFormulaByMoiety", StringType(), True),
                StructField("isotope",ArrayType(SubstanceSpecification_Isotope.get_schema()), True),
                StructField("molecularWeight", SubstanceSpecification_MolecularWeight.get_schema(), True),
                StructField("source",ArrayType(Reference.get_schema()), True),
                StructField("representation",ArrayType(SubstanceSpecification_Representation.get_schema()), True),]
        )

        return schema
