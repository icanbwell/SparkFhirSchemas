from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchNutritionOrder_OralDiet(AutoMapperDataTypeComplexBase):
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        schedule: Optional[Any] = None,
        nutrient: Optional[Any] = None,
        texture: Optional[Any] = None,
        fluidConsistencyType: Optional[Any] = None,
        instruction: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            schedule=schedule,
            nutrient=nutrient,
            texture=texture,
            fluidConsistencyType=fluidConsistencyType,
            instruction=instruction,
        )
        super().include_null_properties(include_null_properties=True)

    @staticmethod
    def schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.nutritionorder_nutrient import (
            AutoMapperElasticSearchNutritionOrder_Nutrient as NutritionOrder_NutrientSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.nutritionorder_texture import (
            AutoMapperElasticSearchNutritionOrder_Texture as NutritionOrder_TextureSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("NutritionOrder_OralDiet") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["NutritionOrder_OralDiet"]
        schema = StructType(
            [
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
                    ArrayType(
                        ExtensionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The kind of diet or dietary restriction such as fiber restricted diet or
                # diabetic diet.
                StructField(
                    "type",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The time period and frequency at which the diet should be given.  The diet
                # should be given for the combination of all schedules if more than one schedule
                # is present.
                StructField(
                    "schedule",
                    ArrayType(
                        TimingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Class that defines the quantity and type of nutrient modifications (for
                # example carbohydrate, fiber or sodium) required for the oral diet.
                StructField(
                    "nutrient",
                    ArrayType(
                        NutritionOrder_NutrientSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Class that describes any texture modifications required for the patient to
                # safely consume various types of solid foods.
                StructField(
                    "texture",
                    ArrayType(
                        NutritionOrder_TextureSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The required consistency (e.g. honey-thick, nectar-thick, thin, thickened.) of
                # liquids or fluids served to the patient.
                StructField(
                    "fluidConsistencyType",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Free text or additional instructions or information pertaining to the oral
                # diet.
                StructField("instruction", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
