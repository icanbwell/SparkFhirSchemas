from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchNutritionOrder_EnteralFormula(
    AutoMapperDataTypeComplexBase
):
    """
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        baseFormulaType: Optional[Any] = None,
        baseFormulaProductName: Optional[Any] = None,
        additiveType: Optional[Any] = None,
        additiveProductName: Optional[Any] = None,
        caloricDensity: Optional[Any] = None,
        routeofAdministration: Optional[Any] = None,
        administration: Optional[Any] = None,
        maxVolumeToDeliver: Optional[Any] = None,
        administrationInstruction: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            baseFormulaType=baseFormulaType,
            baseFormulaProductName=baseFormulaProductName,
            additiveType=additiveType,
            additiveProductName=additiveProductName,
            caloricDensity=caloricDensity,
            routeofAdministration=routeofAdministration,
            administration=administration,
            maxVolumeToDeliver=maxVolumeToDeliver,
            administrationInstruction=administrationInstruction,
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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.nutritionorder_administration import (
            AutoMapperElasticSearchNutritionOrder_Administration as NutritionOrder_AdministrationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("NutritionOrder_EnteralFormula")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["NutritionOrder_EnteralFormula"]
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
                # The type of enteral or infant formula such as an adult standard formula with
                # fiber or a soy-based infant formula.
                StructField(
                    "baseFormulaType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The product or brand name of the enteral or infant formula product such as
                # "ACME Adult Standard Formula".
                StructField("baseFormulaProductName", StringType(), True),
                # Indicates the type of modular component such as protein, carbohydrate, fat or
                # fiber to be provided in addition to or mixed with the base formula.
                StructField(
                    "additiveType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
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
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The route or physiological path of administration into the patient's
                # gastrointestinal  tract for purposes of providing the formula feeding, e.g.
                # nasogastric tube.
                StructField(
                    "routeofAdministration",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Formula administration instructions as structured data.  This repeating
                # structure allows for changing the administration rate or volume over time for
                # both bolus and continuous feeding.  An example of this would be an instruction
                # to increase the rate of continuous feeding every 2 hours.
                StructField(
                    "administration",
                    ArrayType(
                        NutritionOrder_AdministrationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The maximum total quantity of formula that may be administered to a subject
                # over the period of time, e.g. 1440 mL over 24 hours.
                StructField(
                    "maxVolumeToDeliver",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Free text formula administration, feeding instructions or additional
                # instructions or information.
                StructField("administrationInstruction", StringType(), True),
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
