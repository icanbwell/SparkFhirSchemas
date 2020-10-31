from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CoverageEligibilityRequest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The CoverageEligibilityRequest provides patient and insurance coverage
        information to an insurer for them to respond, in the form of an
        CoverageEligibilityResponse, with information regarding whether the stated
        coverage is valid and in-force and optionally to provide the insurance details
        of the policy.


        resourceType: This is a CoverageEligibilityRequest resource

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

        identifier: A unique identifier assigned to this coverage eligiblity request.

        status: The status of the resource instance.

        priority: When the requestor expects the processor to complete processing.

        purpose: Code to specify whether requesting: prior authorization requirements for some
            service categories or billing codes; benefits for coverages specified or
            discovered; discovery and return of coverages for the patient; and/or
            validation that the specified coverage is in-force at the date/period
            specified or 'now' if not specified.

        patient: The party who is the beneficiary of the supplied coverage and for whom
            eligibility is sought.

        servicedDate: The date or dates when the enclosed suite of services were performed or
            completed.

        servicedPeriod: The date or dates when the enclosed suite of services were performed or
            completed.

        created: The date when this resource was created.

        enterer: Person who created the request.

        provider: The provider which is responsible for the request.

        insurer: The Insurer who issued the coverage in question and is the recipient of the
            request.

        facility: Facility where the services are intended to be provided.

        supportingInfo: Additional information codes regarding exceptions, special considerations, the
            condition, situation, prior or concurrent issues.

        insurance: Financial instruments for reimbursement for the health care products and
            services.

        item: Service categories or billable services for which benefit details and/or an
            authorization prior to service delivery may be required by the payor.

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
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_supportinginfo import CoverageEligibilityRequest_SupportingInfo
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_insurance import CoverageEligibilityRequest_Insurance
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityrequest_item import CoverageEligibilityRequest_Item
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a CoverageEligibilityRequest resource
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
                # A unique identifier assigned to this coverage eligiblity request.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The status of the resource instance.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # When the requestor expects the processor to complete processing.
                StructField(
                    "priority",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Code to specify whether requesting: prior authorization requirements for some
                # service categories or billing codes; benefits for coverages specified or
                # discovered; discovery and return of coverages for the patient; and/or
                # validation that the specified coverage is in-force at the date/period
                # specified or 'now' if not specified.
                # The party who is the beneficiary of the supplied coverage and for whom
                # eligibility is sought.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # The date or dates when the enclosed suite of services were performed or
                # completed.
                StructField("servicedDate", StringType(), True),
                # The date or dates when the enclosed suite of services were performed or
                # completed.
                StructField(
                    "servicedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # The date when this resource was created.
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Person who created the request.
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                # The provider which is responsible for the request.
                StructField(
                    "provider", Reference.get_schema(recursion_depth + 1), True
                ),
                # The Insurer who issued the coverage in question and is the recipient of the
                # request.
                StructField(
                    "insurer", Reference.get_schema(recursion_depth + 1), True
                ),
                # Facility where the services are intended to be provided.
                StructField(
                    "facility", Reference.get_schema(recursion_depth + 1), True
                ),
                # Additional information codes regarding exceptions, special considerations, the
                # condition, situation, prior or concurrent issues.
                StructField(
                    "supportingInfo",
                    ArrayType(
                        CoverageEligibilityRequest_SupportingInfo.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Financial instruments for reimbursement for the health care products and
                # services.
                StructField(
                    "insurance",
                    ArrayType(
                        CoverageEligibilityRequest_Insurance.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Service categories or billable services for which benefit details and/or an
                # authorization prior to service delivery may be required by the payor.
                StructField(
                    "item",
                    ArrayType(
                        CoverageEligibilityRequest_Item.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
