from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DataType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchAllergyIntolerance(AutoMapperDataTypeComplexBase):
    """
    Risk of harmful or undesirable, physiological response which is unique to an
    individual and associated with exposure to a substance.
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
        clinicalStatus: Optional[Any] = None,
        verificationStatus: Optional[Any] = None,
        type_: Optional[Any] = None,
        category: Optional[Any] = None,
        criticality: Optional[Any] = None,
        code: Optional[Any] = None,
        patient: Optional[Any] = None,
        encounter: Optional[Any] = None,
        onsetDateTime: Optional[Any] = None,
        onsetAge: Optional[Any] = None,
        onsetPeriod: Optional[Any] = None,
        onsetRange: Optional[Any] = None,
        onsetString: Optional[Any] = None,
        recordedDate: Optional[Any] = None,
        recorder: Optional[Any] = None,
        asserter: Optional[Any] = None,
        lastOccurrence: Optional[Any] = None,
        note: Optional[Any] = None,
        reaction: Optional[Any] = None,
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
            clinicalStatus=clinicalStatus,
            verificationStatus=verificationStatus,
            type_=type_,
            category=category,
            criticality=criticality,
            code=code,
            patient=patient,
            encounter=encounter,
            onsetDateTime=onsetDateTime,
            onsetAge=onsetAge,
            onsetPeriod=onsetPeriod,
            onsetRange=onsetRange,
            onsetString=onsetString,
            recordedDate=recordedDate,
            recorder=recorder,
            asserter=asserter,
            lastOccurrence=lastOccurrence,
            note=note,
            reaction=reaction,
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
        Risk of harmful or undesirable, physiological response which is unique to an
        individual and associated with exposure to a substance.


        resourceType: This is a AllergyIntolerance resource

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

        identifier: Business identifiers assigned to this AllergyIntolerance by the performer or
            other systems which remain constant as the resource is updated and propagates
            from server to server.

        clinicalStatus: The clinical status of the allergy or intolerance.

        verificationStatus: Assertion about certainty associated with the propensity, or potential risk,
            of a reaction to the identified substance (including pharmaceutical product).

        type: Identification of the underlying physiological mechanism for the reaction
            risk.

        category: Category of the identified substance.

        criticality: Estimate of the potential clinical harm, or seriousness, of the reaction to
            the identified substance.

        code: Code for an allergy or intolerance statement (either a positive or a
            negated/excluded statement).  This may be a code for a substance or
            pharmaceutical product that is considered to be responsible for the adverse
            reaction risk (e.g., "Latex"), an allergy or intolerance condition (e.g.,
            "Latex allergy"), or a negated/excluded code for a specific substance or class
            (e.g., "No latex allergy") or a general or categorical negated statement
            (e.g.,  "No known allergy", "No known drug allergies").  Note: the substance
            for a specific reaction may be different from the substance identified as the
            cause of the risk, but it must be consistent with it. For instance, it may be
            a more specific substance (e.g. a brand medication) or a composite product
            that includes the identified substance. It must be clinically safe to only
            process the 'code' and ignore the 'reaction.substance'.  If a receiving system
            is unable to confirm that AllergyIntolerance.reaction.substance falls within
            the semantic scope of AllergyIntolerance.code, then the receiving system
            should ignore AllergyIntolerance.reaction.substance.

        patient: The patient who has the allergy or intolerance.

        encounter: The encounter when the allergy or intolerance was asserted.

        onsetDateTime: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetAge: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetPeriod: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetRange: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        onsetString: Estimated or actual date,  date-time, or age when allergy or intolerance was
            identified.

        recordedDate: The recordedDate represents when this particular AllergyIntolerance record was
            created in the system, which is often a system-generated date.

        recorder: Individual who recorded the record and takes responsibility for its content.

        asserter: The source of the information about the allergy that is recorded.

        lastOccurrence: Represents the date and/or time of the last known occurrence of a reaction
            event.

        note: Additional narrative about the propensity for the Adverse Reaction, not
            captured in other fields.

        reaction: Details about each adverse reaction event linked to exposure to the identified
            substance.

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
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.allergyintolerance_reaction import (
            AutoMapperElasticSearchAllergyIntolerance_Reaction as AllergyIntolerance_ReactionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("AllergyIntolerance") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["AllergyIntolerance"]
        schema = StructType(
            [
                # This is a AllergyIntolerance resource
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
                # Business identifiers assigned to this AllergyIntolerance by the performer or
                # other systems which remain constant as the resource is updated and propagates
                # from server to server.
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
                # The clinical status of the allergy or intolerance.
                StructField(
                    "clinicalStatus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Assertion about certainty associated with the propensity, or potential risk,
                # of a reaction to the identified substance (including pharmaceutical product).
                StructField(
                    "verificationStatus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identification of the underlying physiological mechanism for the reaction
                # risk.
                StructField("type", StringType(), True),
                # Category of the identified substance.
                # Estimate of the potential clinical harm, or seriousness, of the reaction to
                # the identified substance.
                StructField("criticality", StringType(), True),
                # Code for an allergy or intolerance statement (either a positive or a
                # negated/excluded statement).  This may be a code for a substance or
                # pharmaceutical product that is considered to be responsible for the adverse
                # reaction risk (e.g., "Latex"), an allergy or intolerance condition (e.g.,
                # "Latex allergy"), or a negated/excluded code for a specific substance or class
                # (e.g., "No latex allergy") or a general or categorical negated statement
                # (e.g.,  "No known allergy", "No known drug allergies").  Note: the substance
                # for a specific reaction may be different from the substance identified as the
                # cause of the risk, but it must be consistent with it. For instance, it may be
                # a more specific substance (e.g. a brand medication) or a composite product
                # that includes the identified substance. It must be clinically safe to only
                # process the 'code' and ignore the 'reaction.substance'.  If a receiving system
                # is unable to confirm that AllergyIntolerance.reaction.substance falls within
                # the semantic scope of AllergyIntolerance.code, then the receiving system
                # should ignore AllergyIntolerance.reaction.substance.
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
                # The patient who has the allergy or intolerance.
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
                # The encounter when the allergy or intolerance was asserted.
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
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField("onsetDateTime", TimestampType(), True),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField(
                    "onsetAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField(
                    "onsetPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField(
                    "onsetRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Estimated or actual date,  date-time, or age when allergy or intolerance was
                # identified.
                StructField("onsetString", StringType(), True),
                # The recordedDate represents when this particular AllergyIntolerance record was
                # created in the system, which is often a system-generated date.
                StructField(
                    "recordedDate",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Individual who recorded the record and takes responsibility for its content.
                StructField(
                    "recorder",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The source of the information about the allergy that is recorded.
                StructField(
                    "asserter",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Represents the date and/or time of the last known occurrence of a reaction
                # event.
                StructField(
                    "lastOccurrence",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional narrative about the propensity for the Adverse Reaction, not
                # captured in other fields.
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
                # Details about each adverse reaction event linked to exposure to the identified
                # substance.
                StructField(
                    "reaction",
                    ArrayType(
                        AllergyIntolerance_ReactionSchema.schema(
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
