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
        """
        A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        type: The kind of diet or dietary restriction such as fiber restricted diet or
            diabetic diet.

        schedule: The time period and frequency at which the diet should be given.  The diet
            should be given for the combination of all schedules if more than one schedule
            is present.

        nutrient: Class that defines the quantity and type of nutrient modifications (for
            example carbohydrate, fiber or sodium) required for the oral diet.

        texture: Class that describes any texture modifications required for the patient to
            safely consume various types of solid foods.

        fluidConsistencyType: The required consistency (e.g. honey-thick, nectar-thick, thin, thickened.) of
            liquids or fluids served to the patient.

        instruction: Free text or additional instructions or information pertaining to the oral
            diet.

        """
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
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The kind of diet or dietary restriction such as fiber restricted diet or
                # diabetic diet.
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The time period and frequency at which the diet should be given.  The diet
                # should be given for the combination of all schedules if more than one schedule
                # is present.
                StructField(
                    "schedule",
                    ArrayType(Timing.get_schema(recursion_depth + 1)), True
                ),
                # Class that defines the quantity and type of nutrient modifications (for
                # example carbohydrate, fiber or sodium) required for the oral diet.
                StructField(
                    "nutrient",
                    ArrayType(
                        NutritionOrder_Nutrient.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Class that describes any texture modifications required for the patient to
                # safely consume various types of solid foods.
                StructField(
                    "texture",
                    ArrayType(
                        NutritionOrder_Texture.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The required consistency (e.g. honey-thick, nectar-thick, thin, thickened.) of
                # liquids or fluids served to the patient.
                StructField(
                    "fluidConsistencyType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Free text or additional instructions or information pertaining to the oral
                # diet.
                StructField("instruction", StringType(), True),
            ]
        )
        return schema
