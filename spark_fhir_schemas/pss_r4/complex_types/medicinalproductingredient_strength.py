from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMedicinalProductIngredient_Strength(
    AutoMapperDataTypeComplexBase
):
    """
    An ingredient of a manufactured item or pharmaceutical product.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        presentation: Optional[Any] = None,
        presentationLowLimit: Optional[Any] = None,
        concentration: Optional[Any] = None,
        concentrationLowLimit: Optional[Any] = None,
        measurementPoint: Optional[Any] = None,
        country: Optional[Any] = None,
        referenceStrength: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            presentation=presentation,
            presentationLowLimit=presentationLowLimit,
            concentration=concentration,
            concentrationLowLimit=concentrationLowLimit,
            measurementPoint=measurementPoint,
            country=country,
            referenceStrength=referenceStrength,
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
        An ingredient of a manufactured item or pharmaceutical product.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        presentation: The quantity of substance in the unit of presentation, or in the volume (or
            mass) of the single pharmaceutical product or manufactured item.

        presentationLowLimit: A lower limit for the quantity of substance in the unit of presentation. For
            use when there is a range of strengths, this is the lower limit, with the
            presentation attribute becoming the upper limit.

        concentration: The strength per unitary volume (or mass).

        concentrationLowLimit: A lower limit for the strength per unitary volume (or mass), for when there is
            a range. The concentration attribute then becomes the upper limit.

        measurementPoint: For when strength is measured at a particular point or distance.

        country: The country or countries for which the strength range applies.

        referenceStrength: Strength expressed in terms of a reference substance.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicinalproductingredient_referencestrength import (
            AutoMapperElasticSearchMedicinalProductIngredient_ReferenceStrength as MedicinalProductIngredient_ReferenceStrengthSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MedicinalProductIngredient_Strength")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "MedicinalProductIngredient_Strength"
        ]
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
                # The quantity of substance in the unit of presentation, or in the volume (or
                # mass) of the single pharmaceutical product or manufactured item.
                StructField(
                    "presentation",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A lower limit for the quantity of substance in the unit of presentation. For
                # use when there is a range of strengths, this is the lower limit, with the
                # presentation attribute becoming the upper limit.
                StructField(
                    "presentationLowLimit",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The strength per unitary volume (or mass).
                StructField(
                    "concentration",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A lower limit for the strength per unitary volume (or mass), for when there is
                # a range. The concentration attribute then becomes the upper limit.
                StructField(
                    "concentrationLowLimit",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # For when strength is measured at a particular point or distance.
                StructField("measurementPoint", StringType(), True),
                # The country or countries for which the strength range applies.
                StructField(
                    "country",
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
                # Strength expressed in terms of a reference substance.
                StructField(
                    "referenceStrength",
                    ArrayType(
                        MedicinalProductIngredient_ReferenceStrengthSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
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
