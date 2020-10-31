from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class NutritionOrder_OralDiet:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.nutritionorder_nutrient import NutritionOrder_Nutrient
        from spark_fhir_schemas.r4.complex_types.nutritionorder_texture import NutritionOrder_Texture
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
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "schedule",
                    ArrayType(Timing.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "nutrient",
                    ArrayType(
                        NutritionOrder_Nutrient.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "texture",
                    ArrayType(
                        NutritionOrder_Texture.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "fluidConsistencyType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("instruction", StringType(), True),
            ]
        )
        return schema
