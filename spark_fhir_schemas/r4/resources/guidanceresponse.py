from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class GuidanceResponse:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a GuidanceResponse resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # The identifier of the request associated with this response. If an identifier
                # was given as part of the request, it will be reproduced here to enable the
                # requester to more easily identify the response in a multi-request scenario.
                StructField(
                    "requestIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                # Allows a service to provide  unique, business identifiers for the response.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
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
                    CodeableConcept.get_schema(recursion_depth + 1), True
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
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The encounter during which this response was created or to which the creation
                # of this record is tightly associated.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates when the guidance response was processed.
                StructField(
                    "occurrenceDateTime",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                # Provides a reference to the device that performed the guidance.
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Describes the reason for the guidance response in coded or textual form.
                StructField(
                    "reasonCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates the reason the request was initiated. This is typically provided as
                # a parameter to the evaluation and echoed by the service, although for some use
                # cases, such as subscription- or event-based scenarios, it may provide an
                # indication of the cause for the response.
                StructField(
                    "reasonReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Provides a mechanism to communicate additional information about the response.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                # Messages resulting from the evaluation of the artifact or artifacts. As part
                # of evaluating the request, the engine may produce informational or warning
                # messages. These messages will be provided by this element.
                StructField(
                    "evaluationMessage",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The output parameters of the evaluation, if any. Many modules will result in
                # the return of specific resources such as procedure or communication requests
                # that are returned as part of the operation result. However, modules may define
                # specific outputs that would be returned as the result of the evaluation, and
                # these would be returned in this element.
                StructField(
                    "outputParameters",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The actions, if any, produced by the evaluation of the artifact.
                StructField(
                    "result", Reference.get_schema(recursion_depth + 1), True
                ),
                # If the evaluation could not be completed due to lack of information, or
                # additional information would potentially result in a more accurate response,
                # this element will a description of the data required in order to proceed with
                # the evaluation. A subsequent request to the service should include this data.
                StructField(
                    "dataRequirement",
                    ArrayType(DataRequirement.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
