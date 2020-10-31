from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.integer import integer
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.substancepolymer_repeatunit import SubstancePolymer_RepeatUnit


class SubstancePolymer_Repeat:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("numberOfUnits", integer.get_schema(), True),
                StructField("averageMolecularFormula", StringType(), True),
                StructField("repeatUnitAmountType", CodeableConcept.get_schema(), True),
                StructField("repeatUnit",ArrayType(SubstancePolymer_RepeatUnit.get_schema()), True),
            ]
        )

        return schema
