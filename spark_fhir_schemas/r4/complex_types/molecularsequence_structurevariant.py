from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.molecularsequence_outer import MolecularSequence_Outer
from spark_fhir_schemas.r4.complex_types.molecularsequence_inner import MolecularSequence_Inner


class MolecularSequence_StructureVariant:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("variantType", CodeableConcept.get_schema(), True),
                StructField("exact", BooleanType(), True),
                StructField("length", integer.get_schema(), True),
                StructField("outer", MolecularSequence_Outer.get_schema(), True),
                StructField("inner", MolecularSequence_Inner.get_schema(), True),
            ]
        )

        return schema
