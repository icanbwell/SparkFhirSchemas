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
class AutoMapperElasticSearchServiceRequest(AutoMapperDataTypeComplexBase):
    """
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
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
        replaces: Optional[Any] = None,
        requisition: Optional[Any] = None,
        status: Optional[Any] = None,
        intent: Optional[Any] = None,
        category: Optional[Any] = None,
        priority: Optional[Any] = None,
        doNotPerform: Optional[Any] = None,
        code: Optional[Any] = None,
        orderDetail: Optional[Any] = None,
        quantityQuantity: Optional[Any] = None,
        quantityRatio: Optional[Any] = None,
        quantityRange: Optional[Any] = None,
        subject: Optional[Any] = None,
        encounter: Optional[Any] = None,
        occurrenceDateTime: Optional[Any] = None,
        occurrencePeriod: Optional[Any] = None,
        occurrenceTiming: Optional[Any] = None,
        asNeededBoolean: Optional[Any] = None,
        asNeededCodeableConcept: Optional[Any] = None,
        authoredOn: Optional[Any] = None,
        requester: Optional[Any] = None,
        performerType: Optional[Any] = None,
        performer: Optional[Any] = None,
        locationCode: Optional[Any] = None,
        locationReference: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        insurance: Optional[Any] = None,
        supportingInfo: Optional[Any] = None,
        specimen: Optional[Any] = None,
        bodySite: Optional[Any] = None,
        note: Optional[Any] = None,
        patientInstruction: Optional[Any] = None,
        relevantHistory: Optional[Any] = None,
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
            replaces=replaces,
            requisition=requisition,
            status=status,
            intent=intent,
            category=category,
            priority=priority,
            doNotPerform=doNotPerform,
            code=code,
            orderDetail=orderDetail,
            quantityQuantity=quantityQuantity,
            quantityRatio=quantityRatio,
            quantityRange=quantityRange,
            subject=subject,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            occurrencePeriod=occurrencePeriod,
            occurrenceTiming=occurrenceTiming,
            asNeededBoolean=asNeededBoolean,
            asNeededCodeableConcept=asNeededCodeableConcept,
            authoredOn=authoredOn,
            requester=requester,
            performerType=performerType,
            performer=performer,
            locationCode=locationCode,
            locationReference=locationReference,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            insurance=insurance,
            supportingInfo=supportingInfo,
            specimen=specimen,
            bodySite=bodySite,
            note=note,
            patientInstruction=patientInstruction,
            relevantHistory=relevantHistory,
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
        A record of a request for service such as diagnostic investigations,
        treatments, or operations to be performed.


        resourceType: This is a ServiceRequest resource

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

        identifier: Identifiers assigned to this order instance by the orderer and/or the receiver
            and/or order fulfiller.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this ServiceRequest.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            ServiceRequest.

        basedOn: Plan/proposal/order fulfilled by this request.

        replaces: The request takes the place of the referenced completed or terminated
            request(s).

        requisition: A shared identifier common to all service requests that were authorized more
            or less simultaneously by a single author, representing the composite or group
            identifier.

        status: The status of the order.

        intent: Whether the request is a proposal, plan, an original order or a reflex order.

        category: A code that classifies the service for searching, sorting and display purposes
            (e.g. "Surgical Procedure").

        priority: Indicates how quickly the ServiceRequest should be addressed with respect to
            other requests.

        doNotPerform: Set this to true if the record is saying that the service/procedure should NOT
            be performed.

        code: A code that identifies a particular service (i.e., procedure, diagnostic
            investigation, or panel of investigations) that have been requested.

        orderDetail: Additional details and instructions about the how the services are to be
            delivered.   For example, and order for a urinary catheter may have an order
            detail for an external or indwelling catheter, or an order for a bandage may
            require additional instructions specifying how the bandage should be applied.

        quantityQuantity: An amount of service being requested which can be a quantity ( for example
            $1,500 home modification), a ratio ( for example, 20 half day visits per
            month), or a range (2.0 to 1.8 Gy per fraction).

        quantityRatio: An amount of service being requested which can be a quantity ( for example
            $1,500 home modification), a ratio ( for example, 20 half day visits per
            month), or a range (2.0 to 1.8 Gy per fraction).

        quantityRange: An amount of service being requested which can be a quantity ( for example
            $1,500 home modification), a ratio ( for example, 20 half day visits per
            month), or a range (2.0 to 1.8 Gy per fraction).

        subject: On whom or what the service is to be performed. This is usually a human
            patient, but can also be requested on animals, groups of humans or animals,
            devices such as dialysis machines, or even locations (typically for
            environmental scans).

        encounter: An encounter that provides additional information about the healthcare context
            in which this request is made.

        occurrenceDateTime: The date/time at which the requested service should occur.

        occurrencePeriod: The date/time at which the requested service should occur.

        occurrenceTiming: The date/time at which the requested service should occur.

        asNeededBoolean: If a CodeableConcept is present, it indicates the pre-condition for performing
            the service.  For example "pain", "on flare-up", etc.

        asNeededCodeableConcept: If a CodeableConcept is present, it indicates the pre-condition for performing
            the service.  For example "pain", "on flare-up", etc.

        authoredOn: When the request transitioned to being actionable.

        requester: The individual who initiated the request and has responsibility for its
            activation.

        performerType: Desired type of performer for doing the requested service.

        performer: The desired performer for doing the requested service.  For example, the
            surgeon, dermatopathologist, endoscopist, etc.

        locationCode: The preferred location(s) where the procedure should actually happen in coded
            or free text form. E.g. at home or nursing day care center.

        locationReference: A reference to the the preferred location(s) where the procedure should
            actually happen. E.g. at home or nursing day care center.

        reasonCode: An explanation or justification for why this service is being requested in
            coded or textual form.   This is often for billing purposes.  May relate to
            the resources referred to in `supportingInfo`.

        reasonReference: Indicates another resource that provides a justification for why this service
            is being requested.   May relate to the resources referred to in
            `supportingInfo`.

        insurance: Insurance plans, coverage extensions, pre-authorizations and/or pre-
            determinations that may be needed for delivering the requested service.

        supportingInfo: Additional clinical information about the patient or specimen that may
            influence the services or their interpretations.     This information includes
            diagnosis, clinical findings and other observations.  In laboratory ordering
            these are typically referred to as "ask at order entry questions (AOEs)".
            This includes observations explicitly requested by the producer (filler) to
            provide context or supporting information needed to complete the order. For
            example,  reporting the amount of inspired oxygen for blood gas measurements.

        specimen: One or more specimens that the laboratory procedure will use.

        bodySite: Anatomic location where the procedure should be performed. This is the target
            site.

        note: Any other notes and comments made about the service request. For example,
            internal billing notes.

        patientInstruction: Instructions in terms that are understood by the patient or consumer.

        relevantHistory: Key events in the history of the request.

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
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ServiceRequest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ServiceRequest"]
        schema = StructType(
            [
                # This is a ServiceRequest resource
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
                # Identifiers assigned to this order instance by the orderer and/or the receiver
                # and/or order fulfiller.
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
                # The URL pointing to a FHIR-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this ServiceRequest.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(
                        canonicalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this
                # ServiceRequest.
                StructField(
                    "instantiatesUri",
                    ArrayType(
                        uriSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Plan/proposal/order fulfilled by this request.
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
                # The request takes the place of the referenced completed or terminated
                # request(s).
                StructField(
                    "replaces",
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
                # A shared identifier common to all service requests that were authorized more
                # or less simultaneously by a single author, representing the composite or group
                # identifier.
                StructField(
                    "requisition",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The status of the order.
                StructField(
                    "status",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Whether the request is a proposal, plan, an original order or a reflex order.
                StructField(
                    "intent",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A code that classifies the service for searching, sorting and display purposes
                # (e.g. "Surgical Procedure").
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
                # Indicates how quickly the ServiceRequest should be addressed with respect to
                # other requests.
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
                # Set this to true if the record is saying that the service/procedure should NOT
                # be performed.
                StructField("doNotPerform", BooleanType(), True),
                # A code that identifies a particular service (i.e., procedure, diagnostic
                # investigation, or panel of investigations) that have been requested.
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
                # Additional details and instructions about the how the services are to be
                # delivered.   For example, and order for a urinary catheter may have an order
                # detail for an external or indwelling catheter, or an order for a bandage may
                # require additional instructions specifying how the bandage should be applied.
                StructField(
                    "orderDetail",
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
                # An amount of service being requested which can be a quantity ( for example
                # $1,500 home modification), a ratio ( for example, 20 half day visits per
                # month), or a range (2.0 to 1.8 Gy per fraction).
                StructField(
                    "quantityQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An amount of service being requested which can be a quantity ( for example
                # $1,500 home modification), a ratio ( for example, 20 half day visits per
                # month), or a range (2.0 to 1.8 Gy per fraction).
                StructField(
                    "quantityRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An amount of service being requested which can be a quantity ( for example
                # $1,500 home modification), a ratio ( for example, 20 half day visits per
                # month), or a range (2.0 to 1.8 Gy per fraction).
                StructField(
                    "quantityRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # On whom or what the service is to be performed. This is usually a human
                # patient, but can also be requested on animals, groups of humans or animals,
                # devices such as dialysis machines, or even locations (typically for
                # environmental scans).
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
                # An encounter that provides additional information about the healthcare context
                # in which this request is made.
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
                # The date/time at which the requested service should occur.
                StructField("occurrenceDateTime", TimestampType(), True),
                # The date/time at which the requested service should occur.
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
                # The date/time at which the requested service should occur.
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
                # If a CodeableConcept is present, it indicates the pre-condition for performing
                # the service.  For example "pain", "on flare-up", etc.
                StructField("asNeededBoolean", BooleanType(), True),
                # If a CodeableConcept is present, it indicates the pre-condition for performing
                # the service.  For example "pain", "on flare-up", etc.
                StructField(
                    "asNeededCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # When the request transitioned to being actionable.
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
                # The individual who initiated the request and has responsibility for its
                # activation.
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
                # Desired type of performer for doing the requested service.
                StructField(
                    "performerType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The desired performer for doing the requested service.  For example, the
                # surgeon, dermatopathologist, endoscopist, etc.
                StructField(
                    "performer",
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
                # The preferred location(s) where the procedure should actually happen in coded
                # or free text form. E.g. at home or nursing day care center.
                StructField(
                    "locationCode",
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
                # A reference to the the preferred location(s) where the procedure should
                # actually happen. E.g. at home or nursing day care center.
                StructField(
                    "locationReference",
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
                # An explanation or justification for why this service is being requested in
                # coded or textual form.   This is often for billing purposes.  May relate to
                # the resources referred to in `supportingInfo`.
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
                # Indicates another resource that provides a justification for why this service
                # is being requested.   May relate to the resources referred to in
                # `supportingInfo`.
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
                # Insurance plans, coverage extensions, pre-authorizations and/or pre-
                # determinations that may be needed for delivering the requested service.
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
                # Additional clinical information about the patient or specimen that may
                # influence the services or their interpretations.     This information includes
                # diagnosis, clinical findings and other observations.  In laboratory ordering
                # these are typically referred to as "ask at order entry questions (AOEs)".
                # This includes observations explicitly requested by the producer (filler) to
                # provide context or supporting information needed to complete the order. For
                # example,  reporting the amount of inspired oxygen for blood gas measurements.
                StructField(
                    "supportingInfo",
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
                # One or more specimens that the laboratory procedure will use.
                StructField(
                    "specimen",
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
                # Anatomic location where the procedure should be performed. This is the target
                # site.
                StructField(
                    "bodySite",
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
                # Any other notes and comments made about the service request. For example,
                # internal billing notes.
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
                # Instructions in terms that are understood by the patient or consumer.
                StructField("patientInstruction", StringType(), True),
                # Key events in the history of the request.
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