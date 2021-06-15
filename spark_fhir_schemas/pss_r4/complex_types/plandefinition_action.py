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
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchPlanDefinition_Action(AutoMapperDataTypeComplexBase):
    """
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general enough
    to support the description of a broad range of clinical artifacts such as
    clinical decision support rules, order sets and protocols.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        prefix: Optional[Any] = None,
        title: Optional[Any] = None,
        description: Optional[Any] = None,
        textEquivalent: Optional[Any] = None,
        priority: Optional[Any] = None,
        code: Optional[Any] = None,
        reason: Optional[Any] = None,
        documentation: Optional[Any] = None,
        goalId: Optional[Any] = None,
        subjectCodeableConcept: Optional[Any] = None,
        subjectReference: Optional[Any] = None,
        trigger: Optional[Any] = None,
        condition: Optional[Any] = None,
        input_: Optional[Any] = None,
        output: Optional[Any] = None,
        relatedAction: Optional[Any] = None,
        timingDateTime: Optional[Any] = None,
        timingAge: Optional[Any] = None,
        timingPeriod: Optional[Any] = None,
        timingDuration: Optional[Any] = None,
        timingRange: Optional[Any] = None,
        timingTiming: Optional[Any] = None,
        participant: Optional[Any] = None,
        type_: Optional[Any] = None,
        groupingBehavior: Optional[Any] = None,
        selectionBehavior: Optional[Any] = None,
        requiredBehavior: Optional[Any] = None,
        precheckBehavior: Optional[Any] = None,
        cardinalityBehavior: Optional[Any] = None,
        definitionCanonical: Optional[Any] = None,
        definitionUri: Optional[Any] = None,
        transform: Optional[Any] = None,
        dynamicValue: Optional[Any] = None,
        action: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            prefix=prefix,
            title=title,
            description=description,
            textEquivalent=textEquivalent,
            priority=priority,
            code=code,
            reason=reason,
            documentation=documentation,
            goalId=goalId,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            trigger=trigger,
            condition=condition,
            input_=input_,
            output=output,
            relatedAction=relatedAction,
            timingDateTime=timingDateTime,
            timingAge=timingAge,
            timingPeriod=timingPeriod,
            timingDuration=timingDuration,
            timingRange=timingRange,
            timingTiming=timingTiming,
            participant=participant,
            type_=type_,
            groupingBehavior=groupingBehavior,
            selectionBehavior=selectionBehavior,
            requiredBehavior=requiredBehavior,
            precheckBehavior=precheckBehavior,
            cardinalityBehavior=cardinalityBehavior,
            definitionCanonical=definitionCanonical,
            definitionUri=definitionUri,
            transform=transform,
            dynamicValue=dynamicValue,
            action=action,
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
        This resource allows for the definition of various types of plans as a
        sharable, consumable, and executable artifact. The resource is general enough
        to support the description of a broad range of clinical artifacts such as
        clinical decision support rules, order sets and protocols.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        prefix: A user-visible prefix for the action.

        title: The title of the action displayed to a user.

        description: A brief description of the action used to provide a summary to display to the
            user.

        textEquivalent: A text equivalent of the action to be performed. This provides a human-
            interpretable description of the action when the definition is consumed by a
            system that might not be capable of interpreting it dynamically.

        priority: Indicates how quickly the action should be addressed with respect to other
            actions.

        code: A code that provides meaning for the action or action group. For example, a
            section may have a LOINC code for the section of a documentation template.

        reason: A description of why this action is necessary or appropriate.

        documentation: Didactic or other informational resources associated with the action that can
            be provided to the CDS recipient. Information resources can include inline
            text commentary and links to web resources.

        goalId: Identifies goals that this action supports. The reference must be to a goal
            element defined within this plan definition.

        subjectCodeableConcept: A code or group definition that describes the intended subject of the action
            and its children, if any.

        subjectReference: A code or group definition that describes the intended subject of the action
            and its children, if any.

        trigger: A description of when the action should be triggered.

        condition: An expression that describes applicability criteria or start/stop conditions
            for the action.

        input: Defines input data requirements for the action.

        output: Defines the outputs of the action, if any.

        relatedAction: A relationship to another action such as "before" or "30-60 minutes after
            start of".

        timingDateTime: An optional value describing when the action should be performed.

        timingAge: An optional value describing when the action should be performed.

        timingPeriod: An optional value describing when the action should be performed.

        timingDuration: An optional value describing when the action should be performed.

        timingRange: An optional value describing when the action should be performed.

        timingTiming: An optional value describing when the action should be performed.

        participant: Indicates who should participate in performing the action described.

        type: The type of action to perform (create, update, remove).

        groupingBehavior: Defines the grouping behavior for the action and its children.

        selectionBehavior: Defines the selection behavior for the action and its children.

        requiredBehavior: Defines the required behavior for the action.

        precheckBehavior: Defines whether the action should usually be preselected.

        cardinalityBehavior: Defines whether the action can be selected multiple times.

        definitionCanonical: A reference to an ActivityDefinition that describes the action to be taken in
            detail, or a PlanDefinition that describes a series of actions to be taken.

        definitionUri: A reference to an ActivityDefinition that describes the action to be taken in
            detail, or a PlanDefinition that describes a series of actions to be taken.

        transform: A reference to a StructureMap resource that defines a transform that can be
            executed to produce the intent resource using the ActivityDefinition instance
            as the input.

        dynamicValue: Customizations that should be applied to the statically defined resource. For
            example, if the dosage of a medication must be computed based on the patient's
            weight, a customization would be used to specify an expression that calculated
            the weight, and the path on the resource that would contain the result.

        action: Sub actions that are contained within the action. The behavior of this action
            determines the functionality of the sub-actions. For example, a selection
            behavior of at-most-one indicates that of the sub-actions, at most one may be
            chosen as part of realizing the action definition.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.relatedartifact import (
            AutoMapperElasticSearchRelatedArtifact as RelatedArtifactSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.triggerdefinition import (
            AutoMapperElasticSearchTriggerDefinition as TriggerDefinitionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.plandefinition_condition import (
            AutoMapperElasticSearchPlanDefinition_Condition as PlanDefinition_ConditionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.datarequirement import (
            AutoMapperElasticSearchDataRequirement as DataRequirementSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.plandefinition_relatedaction import (
            AutoMapperElasticSearchPlanDefinition_RelatedAction as PlanDefinition_RelatedActionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.plandefinition_participant import (
            AutoMapperElasticSearchPlanDefinition_Participant as PlanDefinition_ParticipantSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.plandefinition_dynamicvalue import (
            AutoMapperElasticSearchPlanDefinition_DynamicValue as PlanDefinition_DynamicValueSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("PlanDefinition_Action") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["PlanDefinition_Action"]
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
                # A user-visible prefix for the action.
                StructField("prefix", StringType(), True),
                # The title of the action displayed to a user.
                StructField("title", StringType(), True),
                # A brief description of the action used to provide a summary to display to the
                # user.
                StructField("description", StringType(), True),
                # A text equivalent of the action to be performed. This provides a human-
                # interpretable description of the action when the definition is consumed by a
                # system that might not be capable of interpreting it dynamically.
                StructField("textEquivalent", StringType(), True),
                # Indicates how quickly the action should be addressed with respect to other
                # actions.
                StructField(
                    "priority",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code that provides meaning for the action or action group. For example, a
                # section may have a LOINC code for the section of a documentation template.
                StructField(
                    "code",
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
                # A description of why this action is necessary or appropriate.
                StructField(
                    "reason",
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
                # Didactic or other informational resources associated with the action that can
                # be provided to the CDS recipient. Information resources can include inline
                # text commentary and links to web resources.
                StructField(
                    "documentation",
                    ArrayType(
                        RelatedArtifactSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Identifies goals that this action supports. The reference must be to a goal
                # element defined within this plan definition.
                StructField(
                    "goalId",
                    ArrayType(
                        idSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A code or group definition that describes the intended subject of the action
                # and its children, if any.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code or group definition that describes the intended subject of the action
                # and its children, if any.
                StructField(
                    "subjectReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A description of when the action should be triggered.
                StructField(
                    "trigger",
                    ArrayType(
                        TriggerDefinitionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An expression that describes applicability criteria or start/stop conditions
                # for the action.
                StructField(
                    "condition",
                    ArrayType(
                        PlanDefinition_ConditionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Defines input data requirements for the action.
                StructField(
                    "input",
                    ArrayType(
                        DataRequirementSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Defines the outputs of the action, if any.
                StructField(
                    "output",
                    ArrayType(
                        DataRequirementSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A relationship to another action such as "before" or "30-60 minutes after
                # start of".
                StructField(
                    "relatedAction",
                    ArrayType(
                        PlanDefinition_RelatedActionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An optional value describing when the action should be performed.
                StructField("timingDateTime", TimestampType(), True),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingDuration",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates who should participate in performing the action described.
                StructField(
                    "participant",
                    ArrayType(
                        PlanDefinition_ParticipantSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The type of action to perform (create, update, remove).
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Defines the grouping behavior for the action and its children.
                StructField("groupingBehavior", StringType(), True),
                # Defines the selection behavior for the action and its children.
                StructField("selectionBehavior", StringType(), True),
                # Defines the required behavior for the action.
                StructField("requiredBehavior", StringType(), True),
                # Defines whether the action should usually be preselected.
                StructField("precheckBehavior", StringType(), True),
                # Defines whether the action can be selected multiple times.
                StructField("cardinalityBehavior", StringType(), True),
                # A reference to an ActivityDefinition that describes the action to be taken in
                # detail, or a PlanDefinition that describes a series of actions to be taken.
                StructField("definitionCanonical", StringType(), True),
                # A reference to an ActivityDefinition that describes the action to be taken in
                # detail, or a PlanDefinition that describes a series of actions to be taken.
                StructField("definitionUri", StringType(), True),
                # A reference to a StructureMap resource that defines a transform that can be
                # executed to produce the intent resource using the ActivityDefinition instance
                # as the input.
                StructField(
                    "transform",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Customizations that should be applied to the statically defined resource. For
                # example, if the dosage of a medication must be computed based on the patient's
                # weight, a customization would be used to specify an expression that calculated
                # the weight, and the path on the resource that would contain the result.
                StructField(
                    "dynamicValue",
                    ArrayType(
                        PlanDefinition_DynamicValueSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Sub actions that are contained within the action. The behavior of this action
                # determines the functionality of the sub-actions. For example, a selection
                # behavior of at-most-one indicates that of the sub-actions, at most one may be
                # chosen as part of realizing the action definition.
                StructField(
                    "action",
                    ArrayType(
                        PlanDefinition_ActionSchema.schema(
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
