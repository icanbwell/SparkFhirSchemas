from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceAmount(AutoMapperDataTypeComplexBase):
    """
    Chemical substances are a single substance type whose primary defining element
    is the molecular structure. Chemical substances shall be defined on the basis
    of their complete covalent molecular structure; the presence of a salt
    (counter-ion) and/or solvates (water, alcohols) is also captured. Purity,
    grade, physical form or particle size are not taken into account in the
    definition of a chemical substance or in the assignment of a Substance ID.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        amountQuantity: Optional[Any] = None,
        amountRange: Optional[Any] = None,
        amountString: Optional[Any] = None,
        amountType: Optional[Any] = None,
        amountText: Optional[Any] = None,
        referenceRange: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            amountQuantity=amountQuantity,
            amountRange=amountRange,
            amountString=amountString,
            amountType=amountType,
            amountText=amountText,
            referenceRange=referenceRange,
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
        Chemical substances are a single substance type whose primary defining element
        is the molecular structure. Chemical substances shall be defined on the basis
        of their complete covalent molecular structure; the presence of a salt
        (counter-ion) and/or solvates (water, alcohols) is also captured. Purity,
        grade, physical form or particle size are not taken into account in the
        definition of a chemical substance or in the assignment of a Substance ID.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        amountQuantity: Used to capture quantitative values for a variety of elements. If only limits
            are given, the arithmetic mean would be the average. If only a single definite
            value for a given element is given, it would be captured in this field.

        amountRange: Used to capture quantitative values for a variety of elements. If only limits
            are given, the arithmetic mean would be the average. If only a single definite
            value for a given element is given, it would be captured in this field.

        amountString: Used to capture quantitative values for a variety of elements. If only limits
            are given, the arithmetic mean would be the average. If only a single definite
            value for a given element is given, it would be captured in this field.

        amountType: Most elements that require a quantitative value will also have a field called
            amount type. Amount type should always be specified because the actual value
            of the amount is often dependent on it. EXAMPLE: In capturing the actual
            relative amounts of substances or molecular fragments it is essential to
            indicate whether the amount refers to a mole ratio or weight ratio. For any
            given element an effort should be made to use same the amount type for all
            related definitional elements.

        amountText: A textual comment on a numeric value.

        referenceRange: Reference range of possible or expected values.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substanceamount_referencerange import (
            AutoMapperElasticSearchSubstanceAmount_ReferenceRange as SubstanceAmount_ReferenceRangeSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceAmount") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SubstanceAmount"]
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
                # Used to capture quantitative values for a variety of elements. If only limits
                # are given, the arithmetic mean would be the average. If only a single definite
                # value for a given element is given, it would be captured in this field.
                StructField(
                    "amountQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Used to capture quantitative values for a variety of elements. If only limits
                # are given, the arithmetic mean would be the average. If only a single definite
                # value for a given element is given, it would be captured in this field.
                StructField(
                    "amountRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Used to capture quantitative values for a variety of elements. If only limits
                # are given, the arithmetic mean would be the average. If only a single definite
                # value for a given element is given, it would be captured in this field.
                StructField("amountString", StringType(), True),
                # Most elements that require a quantitative value will also have a field called
                # amount type. Amount type should always be specified because the actual value
                # of the amount is often dependent on it. EXAMPLE: In capturing the actual
                # relative amounts of substances or molecular fragments it is essential to
                # indicate whether the amount refers to a mole ratio or weight ratio. For any
                # given element an effort should be made to use same the amount type for all
                # related definitional elements.
                StructField(
                    "amountType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A textual comment on a numeric value.
                StructField("amountText", StringType(), True),
                # Reference range of possible or expected values.
                StructField(
                    "referenceRange",
                    SubstanceAmount_ReferenceRangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
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