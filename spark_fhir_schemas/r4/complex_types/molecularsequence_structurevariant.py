from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence_StructureVariant:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.molecularsequence_outer import MolecularSequence_Outer
        from spark_fhir_schemas.r4.complex_types.molecularsequence_inner import MolecularSequence_Inner
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
                    "variantType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("exact", BooleanType(), True),
                StructField(
                    "length", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "outer",
                    MolecularSequence_Outer.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "inner",
                    MolecularSequence_Inner.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
