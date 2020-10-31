from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.timing import Timing
from spark_fhir_schemas.r4.resources.nutritionorder_nutrient import NutritionOrder_Nutrient
from spark_fhir_schemas.r4.resources.nutritionorder_texture import NutritionOrder_Texture
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.string import string


class NutritionOrder_OralDiet:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type",ArrayType(CodeableConcept.get_schema()), True),
                StructField("schedule",ArrayType(Timing.get_schema()), True),
                StructField("nutrient",ArrayType(NutritionOrder_Nutrient.get_schema()), True),
                StructField("texture",ArrayType(NutritionOrder_Texture.get_schema()), True),
                StructField("fluidConsistencyType",ArrayType(CodeableConcept.get_schema()), True),
                StructField("instruction", StringType(), True),]
        )

        return schema
