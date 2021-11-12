from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchObservationDefinition_QualifiedInterval(
    AutoMapperDataTypeComplexBase
):
    """
    Set of definitional characteristics for a kind of observation or measurement
    produced or consumed by an orderable health care service.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        category: Optional[Any] = None,
        range_: Optional[Any] = None,
        context: Optional[Any] = None,
        appliesTo: Optional[Any] = None,
        gender: Optional[Any] = None,
        age: Optional[Any] = None,
        gestationalAge: Optional[Any] = None,
        condition: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            category=category,
            range_=range_,
            context=context,
            appliesTo=appliesTo,
            gender=gender,
            age=age,
            gestationalAge=gestationalAge,
            condition=condition,
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
        Set of definitional characteristics for a kind of observation or measurement
        produced or consumed by an orderable health care service.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        category: The category of interval of values for continuous or ordinal observations
            conforming to this ObservationDefinition.

        range: The low and high values determining the interval. There may be only one of the
            two.

        context: Codes to indicate the health context the range applies to. For example, the
            normal or therapeutic range.

        appliesTo: Codes to indicate the target population this reference range applies to.

        gender: Sex of the population the range applies to.

        age: The age at which this reference range is applicable. This is a neonatal age
            (e.g. number of weeks at term) if the meaning says so.

        gestationalAge: The gestational age to which this reference range is applicable, in the
            context of pregnancy.

        condition: Text based condition for which the reference range is valid.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ObservationDefinition_QualifiedInterval")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ObservationDefinition_QualifiedInterval"
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
                # The category of interval of values for continuous or ordinal observations
                # conforming to this ObservationDefinition.
                StructField("category", StringType(), True),
                # The low and high values determining the interval. There may be only one of the
                # two.
                StructField(
                    "range",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Codes to indicate the health context the range applies to. For example, the
                # normal or therapeutic range.
                StructField(
                    "context",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Codes to indicate the target population this reference range applies to.
                StructField(
                    "appliesTo",
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
                # Sex of the population the range applies to.
                StructField("gender", StringType(), True),
                # The age at which this reference range is applicable. This is a neonatal age
                # (e.g. number of weeks at term) if the meaning says so.
                StructField(
                    "age",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The gestational age to which this reference range is applicable, in the
                # context of pregnancy.
                StructField(
                    "gestationalAge",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Text based condition for which the reference range is valid.
                StructField("condition", StringType(), True),
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
