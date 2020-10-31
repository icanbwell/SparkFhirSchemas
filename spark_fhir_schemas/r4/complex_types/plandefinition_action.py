from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class PlanDefinition_Action:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.triggerdefinition import TriggerDefinition
        from spark_fhir_schemas.r4.complex_types.plandefinition_condition import PlanDefinition_Condition
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
        from spark_fhir_schemas.r4.complex_types.plandefinition_relatedaction import PlanDefinition_RelatedAction
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.plandefinition_participant import PlanDefinition_Participant
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.plandefinition_dynamicvalue import PlanDefinition_DynamicValue
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
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
                    "priority", code.get_schema(recursion_depth + 1), True
                ),
                # A code that provides meaning for the action or action group. For example, a
                # section may have a LOINC code for the section of a documentation template.
                StructField(
                    "code",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # A description of why this action is necessary or appropriate.
                StructField(
                    "reason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Didactic or other informational resources associated with the action that can
                # be provided to the CDS recipient. Information resources can include inline
                # text commentary and links to web resources.
                StructField(
                    "documentation",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                # Identifies goals that this action supports. The reference must be to a goal
                # element defined within this plan definition.
                StructField(
                    "goalId", ArrayType(id.get_schema(recursion_depth + 1)),
                    True
                ),
                # A code or group definition that describes the intended subject of the action
                # and its children, if any.
                StructField(
                    "subjectCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A code or group definition that describes the intended subject of the action
                # and its children, if any.
                StructField(
                    "subjectReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # A description of when the action should be triggered.
                StructField(
                    "trigger",
                    ArrayType(
                        TriggerDefinition.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An expression that describes applicability criteria or start/stop conditions
                # for the action.
                StructField(
                    "condition",
                    ArrayType(
                        PlanDefinition_Condition.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Defines input data requirements for the action.
                StructField(
                    "input",
                    ArrayType(DataRequirement.get_schema(recursion_depth + 1)),
                    True
                ),
                # Defines the outputs of the action, if any.
                StructField(
                    "output",
                    ArrayType(DataRequirement.get_schema(recursion_depth + 1)),
                    True
                ),
                # A relationship to another action such as "before" or "30-60 minutes after
                # start of".
                StructField(
                    "relatedAction",
                    ArrayType(
                        PlanDefinition_RelatedAction.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # An optional value describing when the action should be performed.
                StructField("timingDateTime", StringType(), True),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingAge", Age.get_schema(recursion_depth + 1), True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingRange", Range.get_schema(recursion_depth + 1), True
                ),
                # An optional value describing when the action should be performed.
                StructField(
                    "timingTiming", Timing.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates who should participate in performing the action described.
                StructField(
                    "participant",
                    ArrayType(
                        PlanDefinition_Participant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The type of action to perform (create, update, remove).
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
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
                    "transform", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                # Customizations that should be applied to the statically defined resource. For
                # example, if the dosage of a medication must be computed based on the patient's
                # weight, a customization would be used to specify an expression that calculated
                # the weight, and the path on the resource that would contain the result.
                StructField(
                    "dynamicValue",
                    ArrayType(
                        PlanDefinition_DynamicValue.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Sub actions that are contained within the action. The behavior of this action
                # determines the functionality of the sub-actions. For example, a selection
                # behavior of at-most-one indicates that of the sub-actions, at most one may be
                # chosen as part of realizing the action definition.
                StructField(
                    "action",
                    ArrayType(
                        PlanDefinition_Action.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
