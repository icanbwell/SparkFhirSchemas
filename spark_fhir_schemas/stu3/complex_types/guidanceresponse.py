from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class GuidanceResponseSchema:
    """
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the description
    of any proposed actions to be taken.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        A guidance response is the formal response to a guidance request, including
        any output parameters returned by the evaluation, as well as the description
        of any proposed actions to be taken.


        resourceType: This is a GuidanceResponse resource

        requestId: The id of the request associated with this response. If an id was given as
            part of the request, it will be reproduced here to enable the requester to
            more easily identify the response in a multi-request scenario.

        identifier: Allows a service to provide a unique, business identifier for the response.

        module: A reference to the knowledge module that was invoked.

        status: The status of the response. If the evaluation is completed successfully, the
            status will indicate success. However, in order to complete the evaluation,
            the engine may require more information. In this case, the status will be
            data-required, and the response will contain a description of the additional
            required information. If the evaluation completed successfully, but the engine
            determines that a potentially more accurate response could be provided if more
            data was available, the status will be data-requested, and the response will
            contain a description of the additional requested information.

        subject: The patient for which the request was processed.

        context: Allows the context of the guidance response to be provided if available. In a
            service context, this would likely be unavailable.

        occurrenceDateTime: Indicates when the guidance response was processed.

        performer: Provides a reference to the device that performed the guidance.

        reasonCodeableConcept: Indicates the reason the request was initiated. This is typically provided as
            a parameter to the evaluation and echoed by the service, although for some use
            cases, such as subscription- or event-based scenarios, it may provide an
            indication of the cause for the response.

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
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.stu3.complex_types.datarequirement import DataRequirementSchema
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
                # The id of the request associated with this response. If an id was given as
                # part of the request, it will be reproduced here to enable the requester to
                # more easily identify the response in a multi-request scenario.
                StructField("requestId", StringType(), True),
                # Allows a service to provide a unique, business identifier for the response.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # A reference to the knowledge module that was invoked.
                StructField(
                    "module",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
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
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Allows the context of the guidance response to be provided if available. In a
                # service context, this would likely be unavailable.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Indicates when the guidance response was processed.
                StructField("occurrenceDateTime", StringType(), True),
                # Provides a reference to the device that performed the guidance.
                StructField(
                    "performer",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Indicates the reason the request was initiated. This is typically provided as
                # a parameter to the evaluation and echoed by the service, although for some use
                # cases, such as subscription- or event-based scenarios, it may provide an
                # indication of the cause for the response.
                StructField(
                    "reasonCodeableConcept",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Indicates the reason the request was initiated. This is typically provided as
                # a parameter to the evaluation and echoed by the service, although for some use
                # cases, such as subscription- or event-based scenarios, it may provide an
                # indication of the cause for the response.
                StructField(
                    "reasonReference",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Provides a mechanism to communicate additional information about the response.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Messages resulting from the evaluation of the artifact or artifacts. As part
                # of evaluating the request, the engine may produce informational or warning
                # messages. These messages will be provided by this element.
                StructField(
                    "evaluationMessage",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The output parameters of the evaluation, if any. Many modules will result in
                # the return of specific resources such as procedure or communication requests
                # that are returned as part of the operation result. However, modules may define
                # specific outputs that would be returned as the result of the evaluation, and
                # these would be returned in this element.
                StructField(
                    "outputParameters",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # The actions, if any, produced by the evaluation of the artifact.
                StructField(
                    "result",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # If the evaluation could not be completed due to lack of information, or
                # additional information would potentially result in a more accurate response,
                # this element will a description of the data required in order to proceed with
                # the evaluation. A subsequent request to the service should include this data.
                StructField(
                    "dataRequirement",
                    ArrayType(
                        DataRequirementSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema