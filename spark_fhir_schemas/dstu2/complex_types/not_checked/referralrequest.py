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
class ReferralRequestSchema:
    """
    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organization.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
        """
        Used to record and send details about a request for referral service or
        transfer of a patient to the care of another provider or provider
        organization.


        resourceType: This is a ReferralRequest resource

        identifier: Business identifier that uniquely identifies the referral/care transfer
            request instance.

        definition: A protocol, guideline, orderset or other definition that is adhered to in
            whole or in part by this request.

        basedOn: Indicates any plans, proposals or orders that this request is intended to
            satisfy - in whole or in part.

        replaces: Completed or terminated request(s) whose function is taken by this new
            request.

        groupIdentifier: The business identifier of the logical "grouping" request/order that this
            referral is a part of.

        status: The status of the authorization/intention reflected by the referral request
            record.

        intent: Distinguishes the "level" of authorization/demand implicit in this request.

        type: An indication of the type of referral (or where applicable the type of
            transfer of care) request.

        priority: An indication of the urgency of referral (or where applicable the type of
            transfer of care) request.

        serviceRequested: The service(s) that is/are requested to be provided to the patient.  For
            example: cardiac pacemaker insertion.

        subject: The patient who is the subject of a referral or transfer of care request.

        context: The encounter at which the request for referral or transfer of care is
            initiated.

        occurrenceDateTime: The period of time within which the services identified in the
            referral/transfer of care is specified or required to occur.

        occurrencePeriod: The period of time within which the services identified in the
            referral/transfer of care is specified or required to occur.

        authoredOn: Date/DateTime of creation for draft requests and date of activation for active
            requests.

        requester: The individual who initiated the request and has responsibility for its
            activation.

        specialty: Indication of the clinical domain or discipline to which the referral or
            transfer of care request is sent.  For example: Cardiology Gastroenterology
            Diabetology.

        recipient: The healthcare provider(s) or provider organization(s) who/which is to receive
            the referral/transfer of care request.

        reasonCode: Description of clinical condition indicating why referral/transfer of care is
            requested.  For example:  Pathological Anomalies, Disabled (physical or
            mental),  Behavioral Management.

        reasonReference: Indicates another resource whose existence justifies this request.

        description: The reason element gives a short description of why the referral is being
            made, the description expands on this to support a more complete clinical
            summary.

        supportingInfo: Any additional (administrative, financial or clinical) information required to
            support request for referral or transfer of care.  For example: Presenting
            problems/chief complaints Medical History Family History Alerts
            Allergy/Intolerance and Adverse Reactions Medications Observations/Assessments
            (may include cognitive and fundtional assessments) Diagnostic Reports Care
            Plan.

        note: Comments made about the referral request by any of the participants.

        relevantHistory: Links to Provenance records for past versions of this resource or fulfilling
            request or event resources that identify key state transitions or updates that
            are likely to be relevant to a user looking at the current version of the
            resource.

        """
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema
        from spark_fhir_schemas.dstu2.complex_types.not_checked.referralrequest_requester import (
            ReferralRequest_RequesterSchema,
        )
        from spark_fhir_schemas.dstu2.complex_types.not_checked.annotation import AnnotationSchema

        if (
            max_recursion_limit
            and nesting_list.count("ReferralRequest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ReferralRequest"]
        schema = StructType(
            [
                # This is a ReferralRequest resource
                StructField("resourceType", StringType(), True),
                # Business identifier that uniquely identifies the referral/care transfer
                # request instance.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A protocol, guideline, orderset or other definition that is adhered to in
                # whole or in part by this request.
                StructField(
                    "definition",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates any plans, proposals or orders that this request is intended to
                # satisfy - in whole or in part.
                StructField(
                    "basedOn",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Completed or terminated request(s) whose function is taken by this new
                # request.
                StructField(
                    "replaces",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The business identifier of the logical "grouping" request/order that this
                # referral is a part of.
                StructField(
                    "groupIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The status of the authorization/intention reflected by the referral request
                # record.
                StructField("status", StringType(), True),
                # Distinguishes the "level" of authorization/demand implicit in this request.
                StructField("intent", StringType(), True),
                # An indication of the type of referral (or where applicable the type of
                # transfer of care) request.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An indication of the urgency of referral (or where applicable the type of
                # transfer of care) request.
                StructField("priority", StringType(), True),
                # The service(s) that is/are requested to be provided to the patient.  For
                # example: cardiac pacemaker insertion.
                StructField(
                    "serviceRequested",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The patient who is the subject of a referral or transfer of care request.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The encounter at which the request for referral or transfer of care is
                # initiated.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The period of time within which the services identified in the
                # referral/transfer of care is specified or required to occur.
                StructField("occurrenceDateTime", StringType(), True),
                # The period of time within which the services identified in the
                # referral/transfer of care is specified or required to occur.
                StructField(
                    "occurrencePeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Date/DateTime of creation for draft requests and date of activation for active
                # requests.
                StructField("authoredOn", StringType(), True),
                # The individual who initiated the request and has responsibility for its
                # activation.
                StructField(
                    "requester",
                    ReferralRequest_RequesterSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indication of the clinical domain or discipline to which the referral or
                # transfer of care request is sent.  For example: Cardiology Gastroenterology
                # Diabetology.
                StructField(
                    "specialty",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The healthcare provider(s) or provider organization(s) who/which is to receive
                # the referral/transfer of care request.
                StructField(
                    "recipient",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Description of clinical condition indicating why referral/transfer of care is
                # requested.  For example:  Pathological Anomalies, Disabled (physical or
                # mental),  Behavioral Management.
                StructField(
                    "reasonCode",
                    ArrayType(
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates another resource whose existence justifies this request.
                StructField(
                    "reasonReference",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The reason element gives a short description of why the referral is being
                # made, the description expands on this to support a more complete clinical
                # summary.
                StructField("description", StringType(), True),
                # Any additional (administrative, financial or clinical) information required to
                # support request for referral or transfer of care.  For example: Presenting
                # problems/chief complaints Medical History Family History Alerts
                # Allergy/Intolerance and Adverse Reactions Medications Observations/Assessments
                # (may include cognitive and fundtional assessments) Diagnostic Reports Care
                # Plan.
                StructField(
                    "supportingInfo",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Comments made about the referral request by any of the participants.
                StructField(
                    "note",
                    ArrayType(
                        AnnotationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Links to Provenance records for past versions of this resource or fulfilling
                # request or event resources that identify key state transitions or updates that
                # are likely to be relevant to a user looking at the current version of the
                # resource.
                StructField(
                    "relevantHistory",
                    ArrayType(
                        ReferenceSchema.get_schema(
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