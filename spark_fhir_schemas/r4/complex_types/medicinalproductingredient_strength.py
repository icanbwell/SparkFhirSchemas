from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.ratio import Ratio
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.medicinalproductingredient_referencestrength import MedicinalProductIngredient_ReferenceStrength


class MedicinalProductIngredient_Strength:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("presentation", Ratio.get_schema(), True),
                StructField("presentationLowLimit", Ratio.get_schema(), True),
                StructField("concentration", Ratio.get_schema(), True),
                StructField("concentrationLowLimit", Ratio.get_schema(), True),
                StructField("measurementPoint", StringType(), True),
                StructField("country",ArrayType(CodeableConcept.get_schema()), True),
                StructField("referenceStrength",ArrayType(MedicinalProductIngredient_ReferenceStrength.get_schema()), True),
            ]
        )

        return schema
