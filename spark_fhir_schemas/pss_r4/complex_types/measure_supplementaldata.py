from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMeasure_SupplementalData(AutoMapperDataTypeComplexBase):
    """
    The Measure resource provides the definition of a quality measure.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        code: Optional[Any] = None,
        usage: Optional[Any] = None,
        description: Optional[Any] = None,
        criteria: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            usage=usage,
            description=description,
            criteria=criteria,
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
        The Measure resource provides the definition of a quality measure.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        code: Indicates a meaning for the supplemental data. This can be as simple as a
            unique identifier, or it can establish meaning in a broader context by drawing
            from a terminology, allowing supplemental data to be correlated across
            measures.

        usage: An indicator of the intended usage for the supplemental data element.
            Supplemental data indicates the data is additional information requested to
            augment the measure information. Risk adjustment factor indicates the data is
            additional information used to calculate risk adjustment factors when applying
            a risk model to the measure calculation.

        description: The human readable description of this supplemental data.

        criteria: The criteria for the supplemental data. This is typically the name of a valid
            expression defined within a referenced library, but it may also be a path to a
            specific data element. The criteria defines the data to be returned for this
            element.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.expression import (
            AutoMapperElasticSearchExpression as ExpressionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Measure_SupplementalData") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Measure_SupplementalData"]
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
                # Indicates a meaning for the supplemental data. This can be as simple as a
                # unique identifier, or it can establish meaning in a broader context by drawing
                # from a terminology, allowing supplemental data to be correlated across
                # measures.
                StructField(
                    "code",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An indicator of the intended usage for the supplemental data element.
                # Supplemental data indicates the data is additional information requested to
                # augment the measure information. Risk adjustment factor indicates the data is
                # additional information used to calculate risk adjustment factors when applying
                # a risk model to the measure calculation.
                StructField(
                    "usage",
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
                # The human readable description of this supplemental data.
                StructField("description", StringType(), True),
                # The criteria for the supplemental data. This is typically the name of a valid
                # expression defined within a referenced library, but it may also be a path to a
                # specific data element. The criteria defines the data to be returned for this
                # element.
                StructField(
                    "criteria",
                    ExpressionSchema.schema(
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
