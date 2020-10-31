from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class RequestGroup_Action:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A group of related requests that can be used to capture intended activities
        that have inter-dependencies such as "give this medication after that one".


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

        description: A short description of the action used to provide a summary to display to the
            user.

        textEquivalent: A text equivalent of the action to be performed. This provides a human-
            interpretable description of the action when the definition is consumed by a
            system that might not be capable of interpreting it dynamically.

        priority: Indicates how quickly the action should be addressed with respect to other
            actions.

        code: A code that provides meaning for the action or action group. For example, a
            section may have a LOINC code for a section of a documentation template.

        documentation: Didactic or other informational resources associated with the action that can
            be provided to the CDS recipient. Information resources can include inline
            text commentary and links to web resources.

        condition: An expression that describes applicability criteria, or start/stop conditions
            for the action.

        relatedAction: A relationship to another action such as "before" or "30-60 minutes after
            start of".

        timingDateTime: An optional value describing when the action should be performed.

        timingAge: An optional value describing when the action should be performed.

        timingPeriod: An optional value describing when the action should be performed.

        timingDuration: An optional value describing when the action should be performed.

        timingRange: An optional value describing when the action should be performed.

        timingTiming: An optional value describing when the action should be performed.

        participant: The participant that should perform or be responsible for this action.

        type: The type of action to perform (create, update, remove).

        groupingBehavior: Defines the grouping behavior for the action and its children.

        selectionBehavior: Defines the selection behavior for the action and its children.

        requiredBehavior: Defines expectations around whether an action is required.

        precheckBehavior: Defines whether the action should usually be preselected.

        cardinalityBehavior: Defines whether the action can be selected multiple times.

        resource: The resource that is the target of the action (e.g. CommunicationRequest).

        action: Sub actions.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.complex_types.requestgroup_condition import RequestGroup_Condition
        from spark_fhir_schemas.r4.complex_types.requestgroup_relatedaction import RequestGroup_RelatedAction
        from spark_fhir_schemas.r4.complex_types.age import Age
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # A short description of the action used to provide a summary to display to the
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
                # section may have a LOINC code for a section of a documentation template.
                StructField(
                    "code",
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
                # An expression that describes applicability criteria, or start/stop conditions
                # for the action.
                StructField(
                    "condition",
                    ArrayType(
                        RequestGroup_Condition.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A relationship to another action such as "before" or "30-60 minutes after
                # start of".
                StructField(
                    "relatedAction",
                    ArrayType(
                        RequestGroup_RelatedAction.
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
                # The participant that should perform or be responsible for this action.
                StructField(
                    "participant",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The type of action to perform (create, update, remove).
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Defines the grouping behavior for the action and its children.
                StructField(
                    "groupingBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                # Defines the selection behavior for the action and its children.
                StructField(
                    "selectionBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                # Defines expectations around whether an action is required.
                StructField(
                    "requiredBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                # Defines whether the action should usually be preselected.
                StructField(
                    "precheckBehavior", code.get_schema(recursion_depth + 1),
                    True
                ),
                # Defines whether the action can be selected multiple times.
                StructField(
                    "cardinalityBehavior",
                    code.get_schema(recursion_depth + 1), True
                ),
                # The resource that is the target of the action (e.g. CommunicationRequest).
                StructField(
                    "resource", Reference.get_schema(recursion_depth + 1), True
                ),
                # Sub actions.
                StructField(
                    "action",
                    ArrayType(
                        RequestGroup_Action.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
