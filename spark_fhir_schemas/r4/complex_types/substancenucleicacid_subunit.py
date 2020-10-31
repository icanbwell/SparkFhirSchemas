from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceNucleicAcid_Subunit:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.substancenucleicacid_linkage import SubstanceNucleicAcid_Linkage
        from spark_fhir_schemas.r4.complex_types.substancenucleicacid_sugar import SubstanceNucleicAcid_Sugar
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
                    "subunit", integer.get_schema(recursion_depth + 1), True
                ),
                StructField("sequence", StringType(), True),
                StructField(
                    "length", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sequenceAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fivePrime",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "threePrime",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "linkage",
                    ArrayType(
                        SubstanceNucleicAcid_Linkage.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "sugar",
                    ArrayType(
                        SubstanceNucleicAcid_Sugar.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
