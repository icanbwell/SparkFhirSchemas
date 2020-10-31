from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.reference import Reference


# noinspection PyPep8Naming
class MolecularSequence_Variant:
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
                StructField("start", integer.get_schema(), True),
                StructField("end", integer.get_schema(), True),
                StructField("observedAllele", StringType(), True),
                StructField("referenceAllele", StringType(), True),
                StructField("cigar", StringType(), True),
                StructField("variantPointer", Reference.get_schema(), True),
            ]
        )

        return schema
