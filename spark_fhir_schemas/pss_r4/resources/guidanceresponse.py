from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchGuidanceResponse(AutoMapperDataTypeComplexBase):
    """
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the description
    of any proposed actions to be taken.
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
        requestIdentifier: Optional[Any] = None,
        identifier: Optional[Any] = None,
        moduleUri: Optional[Any] = None,
        moduleCanonical: Optional[Any] = None,
        moduleCodeableConcept: Optional[Any] = None,
        status: Optional[Any] = None,
        subject: Optional[Any] = None,
        encounter: Optional[Any] = None,
        occurrenceDateTime: Optional[Any] = None,
        performer: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        note: Optional[Any] = None,
        evaluationMessage: Optional[Any] = None,
        outputParameters: Optional[Any] = None,
        result: Optional[Any] = None,
        dataRequirement: Optional[Any] = None,
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
            requestIdentifier=requestIdentifier,
            identifier=identifier,
            moduleUri=moduleUri,
            moduleCanonical=moduleCanonical,
            moduleCodeableConcept=moduleCodeableConcept,
            status=status,
            subject=subject,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            performer=performer,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            note=note,
            evaluationMessage=evaluationMessage,
            outputParameters=outputParameters,
            result=result,
            dataRequirement=dataRequirement,
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
        A guidance response is the formal response to a guidance request, including
        any output parameters returned by the evaluation, as well as the description
        of any proposed actions to be taken.


        resourceType: This is a GuidanceResponse resource

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

        requestIdentifier: The identifier of the request associated with this response. If an identifier
            was given as part of the request, it will be reproduced here to enable the
            requester to more easily identify the response in a multi-request scenario.

        identifier: Allows a service to provide  unique, business identifiers for the response.

        moduleUri: An identifier, CodeableConcept or canonical reference to the guidance that was
            requested.

        moduleCanonical: An identifier, CodeableConcept or canonical reference to the guidance that was
            requested.

        moduleCodeableConcept: An identifier, CodeableConcept or canonical reference to the guidance that was
            requested.

        status: The status of the response. If the evaluation is completed successfully, the
            status will indicate success. However, in order to complete the evaluation,
            the engine may require more information. In this case, the status will be
            data-required, and the response will contain a description of the additional
            required information. If the evaluation completed successfully, but the engine
            determines that a potentially more accurate response could be provided if more
            data was available, the status will be data-requested, and the response will
            contain a description of the additional requested information.

        subject: The patient for which the request was processed.

        encounter: The encounter during which this response was created or to which the creation
            of this record is tightly associated.

        occurrenceDateTime: Indicates when the guidance response was processed.

        performer: Provides a reference to the device that performed the guidance.

        reasonCode: Describes the reason for the guidance response in coded or textual form.

        reasonReference: Indicates the reason the request was initiated. This is typically provided as
            a parameter to the evaluation and echoed by the service, although for some use
            cases, such as subscription- or event-based scenarios, it may provide an
            indication of the cause for the response.

        note: Provides a mechanism to communicate additional information about the response.

        evaluationMessage: Messages resulting from the evaluation of the artifact or artifacts. As part
            of evaluating the request, the engine may produce informational or warning
            messages. These messages will be provided by this element.

        outputParameters: The output parameters of the evaluation, if any. Many modules will result in
            the return of specific resources such as procedure or communication requests
            that are returned as part of the operation result. However, modules may define
            specific outputs that would be returned as the result of the evaluation, and
            these would be returned in this element.

        result: The actions, if any, produced by the evaluation of the artifact.

        dataRequirement: If the evaluation could not be completed due to lack of information, or
            additional information would potentially result in a more accurate response,
            this element will a description of the data required in order to proceed with
            the evaluation. A subsequent request to the service should include this data.

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
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.datarequirement import (
            AutoMapperElasticSearchDataRequirement as DataRequirementSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("GuidanceResponse") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["GuidanceResponse"]
        schema = StructType(
            [
                # This is a GuidanceResponse resource
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
                # The identifier of the request associated with this response. If an identifier
                # was given as part of the request, it will be reproduced here to enable the
                # requester to more easily identify the response in a multi-request scenario.
                StructField(
                    "requestIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Allows a service to provide  unique, business identifiers for the response.
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
                # An identifier, CodeableConcept or canonical reference to the guidance that was
                # requested.
                StructField("moduleUri", StringType(), True),
                # An identifier, CodeableConcept or canonical reference to the guidance that was
                # requested.
                StructField("moduleCanonical", StringType(), True),
                # An identifier, CodeableConcept or canonical reference to the guidance that was
                # requested.
                StructField(
                    "moduleCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The status of the response. If the evaluation is completed successfully, the
                # status will indicate success. However, in order to complete the evaluation,
                # the engine may require more information. In this case, the status will be
                # data-required, and the response will contain a description of the additional
                # required information. If the evaluation completed successfully, but the engine
                # determines that a potentially more accurate response could be provided if more
                # data was available, the status will be data-requested, and the response will
                # contain a description of the additional requested information.
                StructField("status", StringType(), True),
                # The patient for which the request was processed.
                StructField(
                    "subject",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The encounter during which this response was created or to which the creation
                # of this record is tightly associated.
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
                # Indicates when the guidance response was processed.
                StructField(
                    "occurrenceDateTime",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Provides a reference to the device that performed the guidance.
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
                # Describes the reason for the guidance response in coded or textual form.
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
                # Indicates the reason the request was initiated. This is typically provided as
                # a parameter to the evaluation and echoed by the service, although for some use
                # cases, such as subscription- or event-based scenarios, it may provide an
                # indication of the cause for the response.
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
                # Provides a mechanism to communicate additional information about the response.
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
                # Messages resulting from the evaluation of the artifact or artifacts. As part
                # of evaluating the request, the engine may produce informational or warning
                # messages. These messages will be provided by this element.
                StructField(
                    "evaluationMessage",
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
                # The output parameters of the evaluation, if any. Many modules will result in
                # the return of specific resources such as procedure or communication requests
                # that are returned as part of the operation result. However, modules may define
                # specific outputs that would be returned as the result of the evaluation, and
                # these would be returned in this element.
                StructField(
                    "outputParameters",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The actions, if any, produced by the evaluation of the artifact.
                StructField(
                    "result",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If the evaluation could not be completed due to lack of information, or
                # additional information would potentially result in a more accurate response,
                # this element will a description of the data required in order to proceed with
                # the evaluation. A subsequent request to the service should include this data.
                StructField(
                    "dataRequirement",
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