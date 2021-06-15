from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceSpecification_Relationship(
    AutoMapperDataTypeComplexBase
):
    """
    The detailed description of a substance, typically at a level beyond what is
    used for prescribing.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        substanceReference: Optional[Any] = None,
        substanceCodeableConcept: Optional[Any] = None,
        relationship: Optional[Any] = None,
        isDefining: Optional[Any] = None,
        amountQuantity: Optional[Any] = None,
        amountRange: Optional[Any] = None,
        amountRatio: Optional[Any] = None,
        amountString: Optional[Any] = None,
        amountRatioLowLimit: Optional[Any] = None,
        amountType: Optional[Any] = None,
        source: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            substanceReference=substanceReference,
            substanceCodeableConcept=substanceCodeableConcept,
            relationship=relationship,
            isDefining=isDefining,
            amountQuantity=amountQuantity,
            amountRange=amountRange,
            amountRatio=amountRatio,
            amountString=amountString,
            amountRatioLowLimit=amountRatioLowLimit,
            amountType=amountType,
            source=source,
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
        The detailed description of a substance, typically at a level beyond what is
        used for prescribing.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        substanceReference: A pointer to another substance, as a resource or just a representational code.

        substanceCodeableConcept: A pointer to another substance, as a resource or just a representational code.

        relationship: For example "salt to parent", "active moiety", "starting material".

        isDefining: For example where an enzyme strongly bonds with a particular substance, this
            is a defining relationship for that enzyme, out of several possible substance
            relationships.

        amountQuantity: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountRange: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountRatio: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountString: A numeric factor for the relationship, for instance to express that the salt
            of a substance has some percentage of the active substance in relation to some
            other.

        amountRatioLowLimit: For use when the numeric.

        amountType: An operator for the amount, for example "average", "approximately", "less
            than".

        source: Supporting literature.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceSpecification_Relationship")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "SubstanceSpecification_Relationship"
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
                # A pointer to another substance, as a resource or just a representational code.
                StructField(
                    "substanceReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A pointer to another substance, as a resource or just a representational code.
                StructField(
                    "substanceCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # For example "salt to parent", "active moiety", "starting material".
                StructField(
                    "relationship",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # For example where an enzyme strongly bonds with a particular substance, this
                # is a defining relationship for that enzyme, out of several possible substance
                # relationships.
                StructField("isDefining", BooleanType(), True),
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
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
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
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
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
                StructField(
                    "amountRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A numeric factor for the relationship, for instance to express that the salt
                # of a substance has some percentage of the active substance in relation to some
                # other.
                StructField("amountString", StringType(), True),
                # For use when the numeric.
                StructField(
                    "amountRatioLowLimit",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An operator for the amount, for example "average", "approximately", "less
                # than".
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
                # Supporting literature.
                StructField(
                    "source",
                    ArrayType(
                        ReferenceSchema.schema(
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
