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
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchHealthcareService(AutoMapperDataTypeComplexBase):
    """
    The details of a healthcare service available at a location.
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
        active: Optional[Any] = None,
        providedBy: Optional[Any] = None,
        category: Optional[Any] = None,
        type_: Optional[Any] = None,
        specialty: Optional[Any] = None,
        location: Optional[Any] = None,
        name: Optional[Any] = None,
        comment: Optional[Any] = None,
        extraDetails: Optional[Any] = None,
        photo: Optional[Any] = None,
        telecom: Optional[Any] = None,
        coverageArea: Optional[Any] = None,
        serviceProvisionCode: Optional[Any] = None,
        eligibility: Optional[Any] = None,
        program: Optional[Any] = None,
        characteristic: Optional[Any] = None,
        communication: Optional[Any] = None,
        referralMethod: Optional[Any] = None,
        appointmentRequired: Optional[Any] = None,
        availableTime: Optional[Any] = None,
        notAvailable: Optional[Any] = None,
        availabilityExceptions: Optional[Any] = None,
        endpoint: Optional[Any] = None,
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
            active=active,
            providedBy=providedBy,
            category=category,
            type_=type_,
            specialty=specialty,
            location=location,
            name=name,
            comment=comment,
            extraDetails=extraDetails,
            photo=photo,
            telecom=telecom,
            coverageArea=coverageArea,
            serviceProvisionCode=serviceProvisionCode,
            eligibility=eligibility,
            program=program,
            characteristic=characteristic,
            communication=communication,
            referralMethod=referralMethod,
            appointmentRequired=appointmentRequired,
            availableTime=availableTime,
            notAvailable=notAvailable,
            availabilityExceptions=availabilityExceptions,
            endpoint=endpoint,
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
        The details of a healthcare service available at a location.


        resourceType: This is a HealthcareService resource

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

        identifier: External identifiers for this item.

        active: This flag is used to mark the record to not be used. This is not used when a
            center is closed for maintenance, or for holidays, the notAvailable period is
            to be used for this.

        providedBy: The organization that provides this healthcare service.

        category: Identifies the broad category of service being performed or delivered.

        type: The specific type of service that may be delivered or performed.

        specialty: Collection of specialties handled by the service site. This is more of a
            medical term.

        location: The location(s) where this healthcare service may be provided.

        name: Further description of the service as it would be presented to a consumer
            while searching.

        comment: Any additional description of the service and/or any specific issues not
            covered by the other attributes, which can be displayed as further detail
            under the serviceName.

        extraDetails: Extra details about the service that can't be placed in the other fields.

        photo: If there is a photo/symbol associated with this HealthcareService, it may be
            included here to facilitate quick identification of the service in a list.

        telecom: List of contacts related to this specific healthcare service.

        coverageArea: The location(s) that this service is available to (not where the service is
            provided).

        serviceProvisionCode: The code(s) that detail the conditions under which the healthcare service is
            available/offered.

        eligibility: Does this service have specific eligibility requirements that need to be met
            in order to use the service?

        program: Programs that this service is applicable to.

        characteristic: Collection of characteristics (attributes).

        communication: Some services are specifically made available in multiple languages, this
            property permits a directory to declare the languages this is offered in.
            Typically this is only provided where a service operates in communities with
            mixed languages used.

        referralMethod: Ways that the service accepts referrals, if this is not provided then it is
            implied that no referral is required.

        appointmentRequired: Indicates whether or not a prospective consumer will require an appointment
            for a particular service at a site to be provided by the Organization.
            Indicates if an appointment is required for access to this service.

        availableTime: A collection of times that the Service Site is available.

        notAvailable: The HealthcareService is not available during this period of time due to the
            provided reason.

        availabilityExceptions: A description of site availability exceptions, e.g. public holiday
            availability. Succinctly describing all possible exceptions to normal site
            availability as details in the available Times and not available Times.

        endpoint: Technical endpoints providing access to services operated for the specific
            healthcare services defined at this resource.

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
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contactpoint import (
            AutoMapperElasticSearchContactPoint as ContactPointSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.healthcareservice_eligibility import (
            AutoMapperElasticSearchHealthcareService_Eligibility as HealthcareService_EligibilitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.healthcareservice_availabletime import (
            AutoMapperElasticSearchHealthcareService_AvailableTime as HealthcareService_AvailableTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.healthcareservice_notavailable import (
            AutoMapperElasticSearchHealthcareService_NotAvailable as HealthcareService_NotAvailableSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("HealthcareService") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["HealthcareService"]
        schema = StructType(
            [
                # This is a HealthcareService resource
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
                # External identifiers for this item.
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
                # This flag is used to mark the record to not be used. This is not used when a
                # center is closed for maintenance, or for holidays, the notAvailable period is
                # to be used for this.
                StructField("active", BooleanType(), True),
                # The organization that provides this healthcare service.
                StructField(
                    "providedBy",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the broad category of service being performed or delivered.
                StructField(
                    "category",
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
                # The specific type of service that may be delivered or performed.
                StructField(
                    "type",
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
                # Collection of specialties handled by the service site. This is more of a
                # medical term.
                StructField(
                    "specialty",
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
                # The location(s) where this healthcare service may be provided.
                StructField(
                    "location",
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
                # Further description of the service as it would be presented to a consumer
                # while searching.
                StructField("name", StringType(), True),
                # Any additional description of the service and/or any specific issues not
                # covered by the other attributes, which can be displayed as further detail
                # under the serviceName.
                StructField("comment", StringType(), True),
                # Extra details about the service that can't be placed in the other fields.
                StructField(
                    "extraDetails",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If there is a photo/symbol associated with this HealthcareService, it may be
                # included here to facilitate quick identification of the service in a list.
                StructField(
                    "photo",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # List of contacts related to this specific healthcare service.
                StructField(
                    "telecom",
                    ArrayType(
                        ContactPointSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The location(s) that this service is available to (not where the service is
                # provided).
                StructField(
                    "coverageArea",
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
                # The code(s) that detail the conditions under which the healthcare service is
                # available/offered.
                StructField(
                    "serviceProvisionCode",
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
                # Does this service have specific eligibility requirements that need to be met
                # in order to use the service?
                StructField(
                    "eligibility",
                    ArrayType(
                        HealthcareService_EligibilitySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Programs that this service is applicable to.
                StructField(
                    "program",
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
                # Collection of characteristics (attributes).
                StructField(
                    "characteristic",
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
                # Some services are specifically made available in multiple languages, this
                # property permits a directory to declare the languages this is offered in.
                # Typically this is only provided where a service operates in communities with
                # mixed languages used.
                StructField(
                    "communication",
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
                # Ways that the service accepts referrals, if this is not provided then it is
                # implied that no referral is required.
                StructField(
                    "referralMethod",
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
                # Indicates whether or not a prospective consumer will require an appointment
                # for a particular service at a site to be provided by the Organization.
                # Indicates if an appointment is required for access to this service.
                StructField("appointmentRequired", BooleanType(), True),
                # A collection of times that the Service Site is available.
                StructField(
                    "availableTime",
                    ArrayType(
                        HealthcareService_AvailableTimeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The HealthcareService is not available during this period of time due to the
                # provided reason.
                StructField(
                    "notAvailable",
                    ArrayType(
                        HealthcareService_NotAvailableSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A description of site availability exceptions, e.g. public holiday
                # availability. Succinctly describing all possible exceptions to normal site
                # availability as details in the available Times and not available Times.
                StructField("availabilityExceptions", StringType(), True),
                # Technical endpoints providing access to services operated for the specific
                # healthcare services defined at this resource.
                StructField(
                    "endpoint",
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