from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.substanceamount import SubstanceAmount
from spark_fhir_schemas.r4.complex_types.substancepolymer_degreeofpolymerisation import SubstancePolymer_DegreeOfPolymerisation
from spark_fhir_schemas.r4.complex_types.substancepolymer_structuralrepresentation import SubstancePolymer_StructuralRepresentation


class SubstancePolymer_RepeatUnit:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("orientationOfPolymerisation", CodeableConcept.get_schema(), True),
                StructField("repeatUnit", StringType(), True),
                StructField("amount", SubstanceAmount.get_schema(), True),
                StructField("degreeOfPolymerisation",ArrayType(SubstancePolymer_DegreeOfPolymerisation.get_schema()), True),
                StructField("structuralRepresentation",ArrayType(SubstancePolymer_StructuralRepresentation.get_schema()), True),
            ]
        )

        return schema
