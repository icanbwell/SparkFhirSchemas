from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class NutritionOrder_EnteralFormulaSchema:
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.


        baseFormulaType: The type of enteral or infant formula such as an adult standard formula with
            fiber or a soy-based infant formula.

        baseFormulaProductName: The product or brand name of the enteral or infant formula product such as
            "ACME Adult Standard Formula".

        additiveType: Indicates the type of modular component such as protein, carbohydrate, fat or
            fiber to be provided in addition to or mixed with the base formula.

        additiveProductName: The product or brand name of the type of modular component to be added to the
            formula.

        caloricDensity: The amount of energy (calories) that the formula should provide per specified
            volume, typically per mL or fluid oz.  For example, an infant may require a
            formula that provides 24 calories per fluid ounce or an adult may require an
            enteral formula that provides 1.5 calorie/mL.

        routeofAdministration: The route or physiological path of administration into the patient's
            gastrointestinal  tract for purposes of providing the formula feeding, e.g.
            nasogastric tube.

        administration: Formula administration instructions as structured data.  This repeating
            structure allows for changing the administration rate or volume over time for
            both bolus and continuous feeding.  An example of this would be an instruction
            to increase the rate of continuous feeding every 2 hours.

        maxVolumeToDeliver: The maximum total quantity of formula that may be administered to a subject
            over the period of time, e.g. 1440 mL over 24 hours.

        administrationInstruction: Free text formula administration, feeding instructions or additional
            instructions or information.

        """
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.nutritionorder_administration import NutritionOrder_AdministrationSchema
        if (
            max_recursion_limit
            and nesting_list.count("NutritionOrder_EnteralFormula") >=
            max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "NutritionOrder_EnteralFormula"
        ]
        schema = StructType(
            [
                # The type of enteral or infant formula such as an adult standard formula with
                # fiber or a soy-based infant formula.
                StructField(
                    "baseFormulaType",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The product or brand name of the enteral or infant formula product such as
                # "ACME Adult Standard Formula".
                StructField("baseFormulaProductName", StringType(), True),
                # Indicates the type of modular component such as protein, carbohydrate, fat or
                # fiber to be provided in addition to or mixed with the base formula.
                StructField(
                    "additiveType",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The product or brand name of the type of modular component to be added to the
                # formula.
                StructField("additiveProductName", StringType(), True),
                # The amount of energy (calories) that the formula should provide per specified
                # volume, typically per mL or fluid oz.  For example, an infant may require a
                # formula that provides 24 calories per fluid ounce or an adult may require an
                # enteral formula that provides 1.5 calorie/mL.
                StructField(
                    "caloricDensity",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The route or physiological path of administration into the patient's
                # gastrointestinal  tract for purposes of providing the formula feeding, e.g.
                # nasogastric tube.
                StructField(
                    "routeofAdministration",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Formula administration instructions as structured data.  This repeating
                # structure allows for changing the administration rate or volume over time for
                # both bolus and continuous feeding.  An example of this would be an instruction
                # to increase the rate of continuous feeding every 2 hours.
                StructField(
                    "administration",
                    ArrayType(
                        NutritionOrder_AdministrationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The maximum total quantity of formula that may be administered to a subject
                # over the period of time, e.g. 1440 mL over 24 hours.
                StructField(
                    "maxVolumeToDeliver",
                    QuantitySchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Free text formula administration, feeding instructions or additional
                # instructions or information.
                StructField("administrationInstruction", StringType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema