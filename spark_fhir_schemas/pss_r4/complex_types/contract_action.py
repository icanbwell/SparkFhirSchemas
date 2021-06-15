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
class AutoMapperElasticSearchContract_Action(AutoMapperDataTypeComplexBase):
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        doNotPerform: Optional[Any] = None,
        type_: Optional[Any] = None,
        subject: Optional[Any] = None,
        intent: Optional[Any] = None,
        linkId: Optional[Any] = None,
        status: Optional[Any] = None,
        context: Optional[Any] = None,
        contextLinkId: Optional[Any] = None,
        occurrenceDateTime: Optional[Any] = None,
        occurrencePeriod: Optional[Any] = None,
        occurrenceTiming: Optional[Any] = None,
        requester: Optional[Any] = None,
        requesterLinkId: Optional[Any] = None,
        performerType: Optional[Any] = None,
        performerRole: Optional[Any] = None,
        performer: Optional[Any] = None,
        performerLinkId: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        reason: Optional[Any] = None,
        reasonLinkId: Optional[Any] = None,
        note: Optional[Any] = None,
        securityLabelNumber: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            doNotPerform=doNotPerform,
            type_=type_,
            subject=subject,
            intent=intent,
            linkId=linkId,
            status=status,
            context=context,
            contextLinkId=contextLinkId,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
            requester=requester,
            requesterLinkId=requesterLinkId,
            performerType=performerType,
            performerRole=performerRole,
            performer=performer,
            performerLinkId=performerLinkId,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            reason=reason,
            reasonLinkId=reasonLinkId,
            note=note,
            securityLabelNumber=securityLabelNumber,
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
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        doNotPerform: True if the term prohibits the  action.

        type: Activity or service obligation to be done or not done, performed or not
            performed, effectuated or not by this Contract term.

        subject: Entity of the action.

        intent: Reason or purpose for the action stipulated by this Contract Provision.

        linkId: Id [identifier??] of the clause or question text related to this action in the
            referenced form or QuestionnaireResponse.

        status: Current state of the term action.

        context: Encounter or Episode with primary association to specified term activity.

        contextLinkId: Id [identifier??] of the clause or question text related to the requester of
            this action in the referenced form or QuestionnaireResponse.

        occurrenceDateTime: When action happens.

        occurrencePeriod: When action happens.

        occurrenceTiming: When action happens.

        requester: Who or what initiated the action and has responsibility for its activation.

        requesterLinkId: Id [identifier??] of the clause or question text related to the requester of
            this action in the referenced form or QuestionnaireResponse.

        performerType: The type of individual that is desired or required to perform or not perform
            the action.

        performerRole: The type of role or competency of an individual desired or required to perform
            or not perform the action.

        performer: Indicates who or what is being asked to perform (or not perform) the ction.

        performerLinkId: Id [identifier??] of the clause or question text related to the reason type or
            reference of this  action in the referenced form or QuestionnaireResponse.

        reasonCode: Rationale for the action to be performed or not performed. Describes why the
            action is permitted or prohibited.

        reasonReference: Indicates another resource whose existence justifies permitting or not
            permitting this action.

        reason: Describes why the action is to be performed or not performed in textual form.

        reasonLinkId: Id [identifier??] of the clause or question text related to the reason type or
            reference of this  action in the referenced form or QuestionnaireResponse.

        note: Comments made about the term action made by the requester, performer, subject
            or other participants.

        securityLabelNumber: Security labels that protects the action.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_subject import (
            AutoMapperElasticSearchContract_Subject as Contract_SubjectSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Contract_Action") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Contract_Action"]
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
                # True if the term prohibits the  action.
                StructField("doNotPerform", BooleanType(), True),
                # Activity or service obligation to be done or not done, performed or not
                # performed, effectuated or not by this Contract term.
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
                # Entity of the action.
                StructField(
                    "subject",
                    ArrayType(
                        Contract_SubjectSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Reason or purpose for the action stipulated by this Contract Provision.
                StructField(
                    "intent",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Id [identifier??] of the clause or question text related to this action in the
                # referenced form or QuestionnaireResponse.
                StructField("linkId", ArrayType(StringType()), True),
                # Current state of the term action.
                StructField(
                    "status",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Encounter or Episode with primary association to specified term activity.
                StructField(
                    "context",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Id [identifier??] of the clause or question text related to the requester of
                # this action in the referenced form or QuestionnaireResponse.
                StructField("contextLinkId", ArrayType(StringType()), True),
                # When action happens.
                StructField("occurrenceDateTime", TimestampType(), True),
                # When action happens.
                StructField(
                    "occurrencePeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # When action happens.
                StructField(
                    "occurrenceTiming",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Who or what initiated the action and has responsibility for its activation.
                StructField(
                    "requester",
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
                # Id [identifier??] of the clause or question text related to the requester of
                # this action in the referenced form or QuestionnaireResponse.
                StructField("requesterLinkId", ArrayType(StringType()), True),
                # The type of individual that is desired or required to perform or not perform
                # the action.
                StructField(
                    "performerType",
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
                # The type of role or competency of an individual desired or required to perform
                # or not perform the action.
                StructField(
                    "performerRole",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates who or what is being asked to perform (or not perform) the ction.
                StructField(
                    "performer",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Id [identifier??] of the clause or question text related to the reason type or
                # reference of this  action in the referenced form or QuestionnaireResponse.
                StructField("performerLinkId", ArrayType(StringType()), True),
                # Rationale for the action to be performed or not performed. Describes why the
                # action is permitted or prohibited.
                StructField(
                    "reasonCode",
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
                # Indicates another resource whose existence justifies permitting or not
                # permitting this action.
                StructField(
                    "reasonReference",
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
                # Describes why the action is to be performed or not performed in textual form.
                StructField("reason", ArrayType(StringType()), True),
                # Id [identifier??] of the clause or question text related to the reason type or
                # reference of this  action in the referenced form or QuestionnaireResponse.
                StructField("reasonLinkId", ArrayType(StringType()), True),
                # Comments made about the term action made by the requester, performer, subject
                # or other participants.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Security labels that protects the action.
                StructField(
                    "securityLabelNumber",
                    ArrayType(
                        unsignedIntSchema.schema(
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
