from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DataType,
    FloatType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchRiskAssessment_Prediction(AutoMapperDataTypeComplexBase):
    """
    An assessment of the likely outcome(s) for a patient or other subject as well
    as the likelihood of each outcome.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        outcome: Optional[Any] = None,
        probabilityDecimal: Optional[Any] = None,
        probabilityRange: Optional[Any] = None,
        qualitativeRisk: Optional[Any] = None,
        relativeRisk: Optional[Any] = None,
        whenPeriod: Optional[Any] = None,
        whenRange: Optional[Any] = None,
        rationale: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            outcome=outcome,
            probabilityDecimal=probabilityDecimal,
            probabilityRange=probabilityRange,
            qualitativeRisk=qualitativeRisk,
            relativeRisk=relativeRisk,
            whenPeriod=whenPeriod,
            whenRange=whenRange,
            rationale=rationale,
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
        An assessment of the likely outcome(s) for a patient or other subject as well
        as the likelihood of each outcome.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        outcome: One of the potential outcomes for the patient (e.g. remission, death,  a
            particular condition).

        probabilityDecimal: Indicates how likely the outcome is (in the specified timeframe).

        probabilityRange: Indicates how likely the outcome is (in the specified timeframe).

        qualitativeRisk: Indicates how likely the outcome is (in the specified timeframe), expressed as
            a qualitative value (e.g. low, medium, or high).

        relativeRisk: Indicates the risk for this particular subject (with their specific
            characteristics) divided by the risk of the population in general.  (Numbers
            greater than 1 = higher risk than the population, numbers less than 1 = lower
            risk.).

        whenPeriod: Indicates the period of time or age range of the subject to which the
            specified probability applies.

        whenRange: Indicates the period of time or age range of the subject to which the
            specified probability applies.

        rationale: Additional information explaining the basis for the prediction.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.decimal import (
            AutoMapperElasticSearchdecimal as decimalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("RiskAssessment_Prediction") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["RiskAssessment_Prediction"]
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
                # One of the potential outcomes for the patient (e.g. remission, death,  a
                # particular condition).
                StructField(
                    "outcome",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates how likely the outcome is (in the specified timeframe).
                StructField("probabilityDecimal", FloatType(), True),
                # Indicates how likely the outcome is (in the specified timeframe).
                StructField(
                    "probabilityRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates how likely the outcome is (in the specified timeframe), expressed as
                # a qualitative value (e.g. low, medium, or high).
                StructField(
                    "qualitativeRisk",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the risk for this particular subject (with their specific
                # characteristics) divided by the risk of the population in general.  (Numbers
                # greater than 1 = higher risk than the population, numbers less than 1 = lower
                # risk.).
                StructField(
                    "relativeRisk",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the period of time or age range of the subject to which the
                # specified probability applies.
                StructField(
                    "whenPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the period of time or age range of the subject to which the
                # specified probability applies.
                StructField(
                    "whenRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional information explaining the basis for the prediction.
                StructField("rationale", StringType(), True),
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