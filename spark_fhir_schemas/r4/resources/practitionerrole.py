from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class PractitionerRole:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A specific set of Roles/Locations/specialties/services that a practitioner may
        perform at an organization for a period of time.


        resourceType: This is a PractitionerRole resource

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

        identifier: Business Identifiers that are specific to a role/location.

        active: Whether this practitioner role record is in active use.

        period: The period during which the person is authorized to act as a practitioner in
            these role(s) for the organization.

        practitioner: Practitioner that is able to provide the defined services for the
            organization.

        organization: The organization where the Practitioner performs the roles associated.

        code: Roles which this practitioner is authorized to perform for the organization.

        specialty: Specific specialty of the practitioner.

        location: The location(s) at which this practitioner provides care.

        healthcareService: The list of healthcare services that this worker provides for this role's
            Organization/Location(s).

        telecom: Contact details that are specific to the role/location/service.

        availableTime: A collection of times the practitioner is available or performing this role at
            the location and/or healthcareservice.

        notAvailable: The practitioner is not available or performing this role during this period
            of time due to the provided reason.

        availabilityExceptions: A description of site availability exceptions, e.g. public holiday
            availability. Succinctly describing all possible exceptions to normal site
            availability as details in the available Times and not available Times.

        endpoint: Technical endpoints providing access to services operated for the practitioner
            with this role.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.practitionerrole_availabletime import PractitionerRole_AvailableTime
        from spark_fhir_schemas.r4.complex_types.practitionerrole_notavailable import PractitionerRole_NotAvailable
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a PractitionerRole resource
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
                # Business Identifiers that are specific to a role/location.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Whether this practitioner role record is in active use.
                StructField("active", BooleanType(), True),
                # The period during which the person is authorized to act as a practitioner in
                # these role(s) for the organization.
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                # Practitioner that is able to provide the defined services for the
                # organization.
                StructField(
                    "practitioner", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The organization where the Practitioner performs the roles associated.
                StructField(
                    "organization", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Roles which this practitioner is authorized to perform for the organization.
                StructField(
                    "code",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Specific specialty of the practitioner.
                StructField(
                    "specialty",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The location(s) at which this practitioner provides care.
                StructField(
                    "location",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # The list of healthcare services that this worker provides for this role's
                # Organization/Location(s).
                StructField(
                    "healthcareService",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Contact details that are specific to the role/location/service.
                StructField(
                    "telecom",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                # A collection of times the practitioner is available or performing this role at
                # the location and/or healthcareservice.
                StructField(
                    "availableTime",
                    ArrayType(
                        PractitionerRole_AvailableTime.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The practitioner is not available or performing this role during this period
                # of time due to the provided reason.
                StructField(
                    "notAvailable",
                    ArrayType(
                        PractitionerRole_NotAvailable.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # A description of site availability exceptions, e.g. public holiday
                # availability. Succinctly describing all possible exceptions to normal site
                # availability as details in the available Times and not available Times.
                StructField("availabilityExceptions", StringType(), True),
                # Technical endpoints providing access to services operated for the practitioner
                # with this role.
                StructField(
                    "endpoint",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
