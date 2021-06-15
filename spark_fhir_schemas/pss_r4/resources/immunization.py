from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    BooleanType,
    DataType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchImmunization(AutoMapperDataTypeComplexBase):
    """
    Describes the event of a patient being administered a vaccine or a record of
    an immunization as reported by a patient, a clinician or another party.
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
        status: Optional[Any] = None,
        statusReason: Optional[Any] = None,
        vaccineCode: Optional[Any] = None,
        patient: Optional[Any] = None,
        encounter: Optional[Any] = None,
        occurrenceDateTime: Optional[Any] = None,
        occurrenceString: Optional[Any] = None,
        recorded: Optional[Any] = None,
        primarySource: Optional[Any] = None,
        reportOrigin: Optional[Any] = None,
        location: Optional[Any] = None,
        manufacturer: Optional[Any] = None,
        lotNumber: Optional[Any] = None,
        expirationDate: Optional[Any] = None,
        site: Optional[Any] = None,
        route: Optional[Any] = None,
        doseQuantity: Optional[Any] = None,
        performer: Optional[Any] = None,
        note: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        isSubpotent: Optional[Any] = None,
        subpotentReason: Optional[Any] = None,
        education: Optional[Any] = None,
        programEligibility: Optional[Any] = None,
        fundingSource: Optional[Any] = None,
        reaction: Optional[Any] = None,
        protocolApplied: Optional[Any] = None,
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
            status=status,
            statusReason=statusReason,
            vaccineCode=vaccineCode,
            patient=patient,
            encounter=encounter,
            occurrenceDateTime=occurrenceDateTime,
            occurrenceString=occurrenceString,
            recorded=recorded,
            primarySource=primarySource,
            reportOrigin=reportOrigin,
            location=location,
            manufacturer=manufacturer,
            lotNumber=lotNumber,
            expirationDate=expirationDate,
            site=site,
            route=route,
            doseQuantity=doseQuantity,
            performer=performer,
            note=note,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            isSubpotent=isSubpotent,
            subpotentReason=subpotentReason,
            education=education,
            programEligibility=programEligibility,
            fundingSource=fundingSource,
            reaction=reaction,
            protocolApplied=protocolApplied,
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
        Describes the event of a patient being administered a vaccine or a record of
        an immunization as reported by a patient, a clinician or another party.


        resourceType: This is a Immunization resource

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

        identifier: A unique identifier assigned to this immunization record.

        status: Indicates the current status of the immunization event.

        statusReason: Indicates the reason the immunization event was not performed.

        vaccineCode: Vaccine that was administered or was to be administered.

        patient: The patient who either received or did not receive the immunization.

        encounter: The visit or admission or other contact between patient and health care
            provider the immunization was performed as part of.

        occurrenceDateTime: Date vaccine administered or was to be administered.

        occurrenceString: Date vaccine administered or was to be administered.

        recorded: The date the occurrence of the immunization was first captured in the record -
            potentially significantly after the occurrence of the event.

        primarySource: An indication that the content of the record is based on information from the
            person who administered the vaccine. This reflects the context under which the
            data was originally recorded.

        reportOrigin: The source of the data when the report of the immunization event is not based
            on information from the person who administered the vaccine.

        location: The service delivery location where the vaccine administration occurred.

        manufacturer: Name of vaccine manufacturer.

        lotNumber: Lot number of the  vaccine product.

        expirationDate: Date vaccine batch expires.

        site: Body site where vaccine was administered.

        route: The path by which the vaccine product is taken into the body.

        doseQuantity: The quantity of vaccine product that was administered.

        performer: Indicates who performed the immunization event.

        note: Extra information about the immunization that is not conveyed by the other
            attributes.

        reasonCode: Reasons why the vaccine was administered.

        reasonReference: Condition, Observation or DiagnosticReport that supports why the immunization
            was administered.

        isSubpotent: Indication if a dose is considered to be subpotent. By default, a dose should
            be considered to be potent.

        subpotentReason: Reason why a dose is considered to be subpotent.

        education: Educational material presented to the patient (or guardian) at the time of
            vaccine administration.

        programEligibility: Indicates a patient's eligibility for a funding program.

        fundingSource: Indicates the source of the vaccine actually administered. This may be
            different than the patient eligibility (e.g. the patient may be eligible for a
            publically purchased vaccine but due to inventory issues, vaccine purchased
            with private funds was actually administered).

        reaction: Categorical data indicating that an adverse event is associated in time to an
            immunization.

        protocolApplied: The protocol (set of recommendations) being followed by the provider who
            administered the dose.

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
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.immunization_performer import (
            AutoMapperElasticSearchImmunization_Performer as Immunization_PerformerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.immunization_education import (
            AutoMapperElasticSearchImmunization_Education as Immunization_EducationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.immunization_reaction import (
            AutoMapperElasticSearchImmunization_Reaction as Immunization_ReactionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.immunization_protocolapplied import (
            AutoMapperElasticSearchImmunization_ProtocolApplied as Immunization_ProtocolAppliedSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Immunization") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Immunization"]
        schema = StructType(
            [
                # This is a Immunization resource
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
                # A unique identifier assigned to this immunization record.
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
                # Indicates the current status of the immunization event.
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
                # Indicates the reason the immunization event was not performed.
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
                # Vaccine that was administered or was to be administered.
                StructField(
                    "vaccineCode",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The patient who either received or did not receive the immunization.
                StructField(
                    "patient",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The visit or admission or other contact between patient and health care
                # provider the immunization was performed as part of.
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
                # Date vaccine administered or was to be administered.
                StructField("occurrenceDateTime", TimestampType(), True),
                # Date vaccine administered or was to be administered.
                StructField("occurrenceString", StringType(), True),
                # The date the occurrence of the immunization was first captured in the record -
                # potentially significantly after the occurrence of the event.
                StructField(
                    "recorded",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An indication that the content of the record is based on information from the
                # person who administered the vaccine. This reflects the context under which the
                # data was originally recorded.
                StructField("primarySource", BooleanType(), True),
                # The source of the data when the report of the immunization event is not based
                # on information from the person who administered the vaccine.
                StructField(
                    "reportOrigin",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The service delivery location where the vaccine administration occurred.
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
                # Name of vaccine manufacturer.
                StructField(
                    "manufacturer",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Lot number of the  vaccine product.
                StructField("lotNumber", StringType(), True),
                # Date vaccine batch expires.
                StructField("expirationDate", DateType(), True),
                # Body site where vaccine was administered.
                StructField(
                    "site",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The path by which the vaccine product is taken into the body.
                StructField(
                    "route",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The quantity of vaccine product that was administered.
                StructField(
                    "doseQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates who performed the immunization event.
                StructField(
                    "performer",
                    ArrayType(
                        Immunization_PerformerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Extra information about the immunization that is not conveyed by the other
                # attributes.
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
                # Reasons why the vaccine was administered.
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
                # Condition, Observation or DiagnosticReport that supports why the immunization
                # was administered.
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
                # Indication if a dose is considered to be subpotent. By default, a dose should
                # be considered to be potent.
                StructField("isSubpotent", BooleanType(), True),
                # Reason why a dose is considered to be subpotent.
                StructField(
                    "subpotentReason",
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
                # Educational material presented to the patient (or guardian) at the time of
                # vaccine administration.
                StructField(
                    "education",
                    ArrayType(
                        Immunization_EducationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates a patient's eligibility for a funding program.
                StructField(
                    "programEligibility",
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
                # Indicates the source of the vaccine actually administered. This may be
                # different than the patient eligibility (e.g. the patient may be eligible for a
                # publically purchased vaccine but due to inventory issues, vaccine purchased
                # with private funds was actually administered).
                StructField(
                    "fundingSource",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Categorical data indicating that an adverse event is associated in time to an
                # immunization.
                StructField(
                    "reaction",
                    ArrayType(
                        Immunization_ReactionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The protocol (set of recommendations) being followed by the provider who
                # administered the dose.
                StructField(
                    "protocolApplied",
                    ArrayType(
                        Immunization_ProtocolAppliedSchema.schema(
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
