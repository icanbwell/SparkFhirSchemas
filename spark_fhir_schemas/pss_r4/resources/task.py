from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchTask(AutoMapperDataTypeComplexBase):
    """
    A task to be performed.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        resourceType: Optional[Any] = None,
        id_: Optional[Any] = None,
        meta: Optional[Any] = None,
        implicitRules: Optional[Any] = None,
        language: Optional[Any] = None,
        text: Optional[Any] = None,
        contained: Optional[Any] = None,
        extension: Optional[Any] = None,
        identifier: Optional[Any] = None,
        instantiatesCanonical: Optional[Any] = None,
        instantiatesUri: Optional[Any] = None,
        basedOn: Optional[Any] = None,
        groupIdentifier: Optional[Any] = None,
        partOf: Optional[Any] = None,
        status: Optional[Any] = None,
        statusReason: Optional[Any] = None,
        businessStatus: Optional[Any] = None,
        intent: Optional[Any] = None,
        priority: Optional[Any] = None,
        code: Optional[Any] = None,
        description: Optional[Any] = None,
        focus: Optional[Any] = None,
        for_: Optional[Any] = None,
        encounter: Optional[Any] = None,
        executionPeriod: Optional[Any] = None,
        authoredOn: Optional[Any] = None,
        lastModified: Optional[Any] = None,
        requester: Optional[Any] = None,
        performerType: Optional[Any] = None,
        owner: Optional[Any] = None,
        location: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        insurance: Optional[Any] = None,
        note: Optional[Any] = None,
        relevantHistory: Optional[Any] = None,
        restriction: Optional[Any] = None,
        input_: Optional[Any] = None,
        output: Optional[Any] = None,
    ) -> None:
        super().__init__(
            resourceType=resourceType,
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            identifier=identifier,
            instantiatesCanonical=instantiatesCanonical,
            instantiatesUri=instantiatesUri,
            basedOn=basedOn,
            groupIdentifier=groupIdentifier,
            partOf=partOf,
            status=status,
            statusReason=statusReason,
            businessStatus=businessStatus,
            intent=intent,
            priority=priority,
            code=code,
            description=description,
            focus=focus,
            for_=for_,
            encounter=encounter,
            executionPeriod=executionPeriod,
            authoredOn=authoredOn,
            lastModified=lastModified,
            requester=requester,
            performerType=performerType,
            owner=owner,
            location=location,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            insurance=insurance,
            note=note,
            relevantHistory=relevantHistory,
            restriction=restriction,
            input_=input_,
            output=output,
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
        A task to be performed.


        resourceType: This is a Task resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        identifier: The business identifier for this task.

        instantiatesCanonical: The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this Task.

        instantiatesUri: The URL pointing to an *externally* maintained  protocol, guideline, orderset
            or other definition that is adhered to in whole or in part by this Task.

        basedOn: BasedOn refers to a higher-level authorization that triggered the creation of
            the task.  It references a "request" resource such as a ServiceRequest,
            MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the
            "request" resource the task is seeking to fulfill.  This latter resource is
            referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a
            task is created to fulfill a procedureRequest ( = FocusOn ) to collect a
            specimen from a patient.

        groupIdentifier: An identifier that links together multiple tasks and other requests that were
            created in the same context.

        partOf: Task that this particular task is part of.

        status: The current status of the task.

        statusReason: An explanation as to why this task is held, failed, was refused, etc.

        businessStatus: Contains business-specific nuances of the business state.

        intent: Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs
            this a proposed task, a planned task, an actionable task, etc.

        priority: Indicates how quickly the Task should be addressed with respect to other
            requests.

        code: A name or code (or both) briefly describing what the task involves.

        description: A free-text description of what is to be performed.

        focus: The request being actioned or the resource being manipulated by this task.

        for: The entity who benefits from the performance of the service specified in the
            task (e.g., the patient).

        encounter: The healthcare event  (e.g. a patient and healthcare provider interaction)
            during which this task was created.

        executionPeriod: Identifies the time action was first taken against the task (start) and/or the
            time final action was taken against the task prior to marking it as completed
            (end).

        authoredOn: The date and time this task was created.

        lastModified: The date and time of last modification to this task.

        requester: The creator of the task.

        performerType: The kind of participant that should perform the task.

        owner: Individual organization or Device currently responsible for task execution.

        location: Principal physical location where the this task is performed.

        reasonCode: A description or code indicating why this task needs to be performed.

        reasonReference: A resource reference indicating why this task needs to be performed.

        insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
            determinations that may be relevant to the Task.

        note: Free-text information captured about the task as it progresses.

        relevantHistory: Links to Provenance records for past versions of this Task that identify key
            state transitions or updates that are likely to be relevant to a user looking
            at the current version of the task.

        restriction: If the Task.focus is a request resource and the task is seeking fulfillment
            (i.e. is asking for the request to be actioned), this element identifies any
            limitations on what parts of the referenced request should be actioned.

        input: Additional information that may be needed in the execution of the task.

        output: Outputs produced by the Task.

        """
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.meta import (
            AutoMapperElasticSearchMeta as MetaSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.narrative import (
            AutoMapperElasticSearchNarrative as NarrativeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.task_restriction import (
            AutoMapperElasticSearchTask_Restriction as Task_RestrictionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.task_input import (
            AutoMapperElasticSearchTask_Input as Task_InputSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.task_output import (
            AutoMapperElasticSearchTask_Output as Task_OutputSchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Task") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Task"]
        schema = StructType(
            [
                # This is a Task resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
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
                # The business identifier for this task.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The URL pointing to a *FHIR*-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this Task.
                StructField(
                    "instantiatesCanonical",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The URL pointing to an *externally* maintained  protocol, guideline, orderset
                # or other definition that is adhered to in whole or in part by this Task.
                StructField(
                    "instantiatesUri",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # BasedOn refers to a higher-level authorization that triggered the creation of
                # the task.  It references a "request" resource such as a ServiceRequest,
                # MedicationRequest, ServiceRequest, CarePlan, etc. which is distinct from the
                # "request" resource the task is seeking to fulfill.  This latter resource is
                # referenced by FocusOn.  For example, based on a ServiceRequest (= BasedOn), a
                # task is created to fulfill a procedureRequest ( = FocusOn ) to collect a
                # specimen from a patient.
                StructField(
                    "basedOn",
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
                # An identifier that links together multiple tasks and other requests that were
                # created in the same context.
                StructField(
                    "groupIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Task that this particular task is part of.
                StructField(
                    "partOf",
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
                # The current status of the task.
                StructField("status", StringType(), True),
                # An explanation as to why this task is held, failed, was refused, etc.
                StructField(
                    "statusReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Contains business-specific nuances of the business state.
                StructField(
                    "businessStatus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the "level" of actionability associated with the Task, i.e. i+R[9]Cs
                # this a proposed task, a planned task, an actionable task, etc.
                StructField("intent", StringType(), True),
                # Indicates how quickly the Task should be addressed with respect to other
                # requests.
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
                # A name or code (or both) briefly describing what the task involves.
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
                # A free-text description of what is to be performed.
                StructField("description", StringType(), True),
                # The request being actioned or the resource being manipulated by this task.
                StructField(
                    "focus",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The entity who benefits from the performance of the service specified in the
                # task (e.g., the patient).
                StructField(
                    "for",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The healthcare event  (e.g. a patient and healthcare provider interaction)
                # during which this task was created.
                StructField(
                    "encounter",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the time action was first taken against the task (start) and/or the
                # time final action was taken against the task prior to marking it as completed
                # (end).
                StructField(
                    "executionPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date and time this task was created.
                StructField(
                    "authoredOn",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date and time of last modification to this task.
                StructField(
                    "lastModified",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The creator of the task.
                StructField(
                    "requester",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The kind of participant that should perform the task.
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
                # Individual organization or Device currently responsible for task execution.
                StructField(
                    "owner",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Principal physical location where the this task is performed.
                StructField(
                    "location",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A description or code indicating why this task needs to be performed.
                StructField(
                    "reasonCode",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A resource reference indicating why this task needs to be performed.
                StructField(
                    "reasonReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Insurance plans, coverage extensions, pre-authorizations and/or pre-
                # determinations that may be relevant to the Task.
                StructField(
                    "insurance",
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
                # Free-text information captured about the task as it progresses.
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
                # Links to Provenance records for past versions of this Task that identify key
                # state transitions or updates that are likely to be relevant to a user looking
                # at the current version of the task.
                StructField(
                    "relevantHistory",
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
                # If the Task.focus is a request resource and the task is seeking fulfillment
                # (i.e. is asking for the request to be actioned), this element identifies any
                # limitations on what parts of the referenced request should be actioned.
                StructField(
                    "restriction",
                    Task_RestrictionSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional information that may be needed in the execution of the task.
                StructField(
                    "input",
                    ArrayType(
                        Task_InputSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Outputs produced by the Task.
                StructField(
                    "output",
                    ArrayType(
                        Task_OutputSchema.schema(
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