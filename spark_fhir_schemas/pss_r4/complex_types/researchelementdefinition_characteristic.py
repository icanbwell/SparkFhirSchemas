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
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchResearchElementDefinition_Characteristic(
    AutoMapperDataTypeComplexBase
):
    """
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        definitionCodeableConcept: Optional[Any] = None,
        definitionCanonical: Optional[Any] = None,
        definitionExpression: Optional[Any] = None,
        definitionDataRequirement: Optional[Any] = None,
        usageContext: Optional[Any] = None,
        exclude: Optional[Any] = None,
        unitOfMeasure: Optional[Any] = None,
        studyEffectiveDescription: Optional[Any] = None,
        studyEffectiveDateTime: Optional[Any] = None,
        studyEffectivePeriod: Optional[Any] = None,
        studyEffectiveDuration: Optional[Any] = None,
        studyEffectiveTiming: Optional[Any] = None,
        studyEffectiveTimeFromStart: Optional[Any] = None,
        studyEffectiveGroupMeasure: Optional[Any] = None,
        participantEffectiveDescription: Optional[Any] = None,
        participantEffectiveDateTime: Optional[Any] = None,
        participantEffectivePeriod: Optional[Any] = None,
        participantEffectiveDuration: Optional[Any] = None,
        participantEffectiveTiming: Optional[Any] = None,
        participantEffectiveTimeFromStart: Optional[Any] = None,
        participantEffectiveGroupMeasure: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            definitionCodeableConcept=definitionCodeableConcept,
            definitionCanonical=definitionCanonical,
            definitionExpression=definitionExpression,
            definitionDataRequirement=definitionDataRequirement,
            usageContext=usageContext,
            exclude=exclude,
            unitOfMeasure=unitOfMeasure,
            studyEffectiveDescription=studyEffectiveDescription,
            studyEffectiveDateTime=studyEffectiveDateTime,
            studyEffectivePeriod=studyEffectivePeriod,
            studyEffectiveDuration=studyEffectiveDuration,
            studyEffectiveTiming=studyEffectiveTiming,
            studyEffectiveTimeFromStart=studyEffectiveTimeFromStart,
            studyEffectiveGroupMeasure=studyEffectiveGroupMeasure,
            participantEffectiveDescription=participantEffectiveDescription,
            participantEffectiveDateTime=participantEffectiveDateTime,
            participantEffectivePeriod=participantEffectivePeriod,
            participantEffectiveDuration=participantEffectiveDuration,
            participantEffectiveTiming=participantEffectiveTiming,
            participantEffectiveTimeFromStart=participantEffectiveTimeFromStart,
            participantEffectiveGroupMeasure=participantEffectiveGroupMeasure,
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
        The ResearchElementDefinition resource describes a "PICO" element that
        knowledge (evidence, assertion, recommendation) is about.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        definitionCodeableConcept: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionCanonical: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionExpression: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionDataRequirement: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        usageContext: Use UsageContext to define the members of the population, such as Age Ranges,
            Genders, Settings.

        exclude: When true, members with this characteristic are excluded from the element.

        unitOfMeasure: Specifies the UCUM unit for the outcome.

        studyEffectiveDescription: A narrative description of the time period the study covers.

        studyEffectiveDateTime: Indicates what effective period the study covers.

        studyEffectivePeriod: Indicates what effective period the study covers.

        studyEffectiveDuration: Indicates what effective period the study covers.

        studyEffectiveTiming: Indicates what effective period the study covers.

        studyEffectiveTimeFromStart: Indicates duration from the study initiation.

        studyEffectiveGroupMeasure: Indicates how elements are aggregated within the study effective period.

        participantEffectiveDescription: A narrative description of the time period the study covers.

        participantEffectiveDateTime: Indicates what effective period the study covers.

        participantEffectivePeriod: Indicates what effective period the study covers.

        participantEffectiveDuration: Indicates what effective period the study covers.

        participantEffectiveTiming: Indicates what effective period the study covers.

        participantEffectiveTimeFromStart: Indicates duration from the participant's study entry.

        participantEffectiveGroupMeasure: Indicates how elements are aggregated within the study effective period.

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
        from spark_fhir_schemas.pss_r4.complex_types.datarequirement import (
            AutoMapperElasticSearchDataRequirement as DataRequirementSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.usagecontext import (
            AutoMapperElasticSearchUsageContext as UsageContextSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ResearchElementDefinition_Characteristic")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ResearchElementDefinition_Characteristic"
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
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField("definitionCanonical", StringType(), True),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionExpression",
                    ExpressionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionDataRequirement",
                    DataRequirementSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Use UsageContext to define the members of the population, such as Age Ranges,
                # Genders, Settings.
                StructField(
                    "usageContext",
                    ArrayType(
                        UsageContextSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # When true, members with this characteristic are excluded from the element.
                StructField("exclude", BooleanType(), True),
                # Specifies the UCUM unit for the outcome.
                StructField(
                    "unitOfMeasure",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A narrative description of the time period the study covers.
                StructField("studyEffectiveDescription", StringType(), True),
                # Indicates what effective period the study covers.
                StructField("studyEffectiveDateTime", TimestampType(), True),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectivePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectiveDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectiveTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates duration from the study initiation.
                StructField(
                    "studyEffectiveTimeFromStart",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates how elements are aggregated within the study effective period.
                StructField("studyEffectiveGroupMeasure", StringType(), True),
                # A narrative description of the time period the study covers.
                StructField("participantEffectiveDescription", StringType(), True),
                # Indicates what effective period the study covers.
                StructField("participantEffectiveDateTime", TimestampType(), True),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectivePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates duration from the participant's study entry.
                StructField(
                    "participantEffectiveTimeFromStart",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates how elements are aggregated within the study effective period.
                StructField("participantEffectiveGroupMeasure", StringType(), True),
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