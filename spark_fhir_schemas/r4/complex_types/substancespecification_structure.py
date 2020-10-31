from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceSpecification_Structure:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substancespecification_isotope import SubstanceSpecification_Isotope
        from spark_fhir_schemas.r4.complex_types.substancespecification_molecularweight import SubstanceSpecification_MolecularWeight
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.substancespecification_representation import SubstanceSpecification_Representation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "stereochemistry",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "opticalActivity",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("molecularFormula", StringType(), True),
                StructField("molecularFormulaByMoiety", StringType(), True),
                StructField(
                    "isotope",
                    ArrayType(
                        SubstanceSpecification_Isotope.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "molecularWeight",
                    SubstanceSpecification_MolecularWeight.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "source",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "representation",
                    ArrayType(
                        SubstanceSpecification_Representation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
