from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.medicinalproductingredient_referencestrength import MedicinalProductIngredient_ReferenceStrength


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
                StructField("referenceStrength",ArrayType(MedicinalProductIngredient_ReferenceStrength.get_schema()), True),]
        )

        return schema
