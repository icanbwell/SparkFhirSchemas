from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceSpecification_Name:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substancespecification_official import SubstanceSpecification_Official
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                StructField("name", StringType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("preferred", BooleanType(), True),
                StructField(
                    "language",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "domain",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "synonym",
                    ArrayType(
                        SubstanceSpecification_Name.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "translation",
                    ArrayType(
                        SubstanceSpecification_Name.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "official",
                    ArrayType(
                        SubstanceSpecification_Official.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "source",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
