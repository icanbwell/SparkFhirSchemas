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
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchFamilyMemberHistory(AutoMapperDataTypeComplexBase):
    """
    Significant health conditions for a person related to the patient relevant in
    the context of care for the patient.
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
        status: Optional[Any] = None,
        dataAbsentReason: Optional[Any] = None,
        patient: Optional[Any] = None,
        date: Optional[Any] = None,
        name: Optional[Any] = None,
        relationship: Optional[Any] = None,
        sex: Optional[Any] = None,
        bornPeriod: Optional[Any] = None,
        bornDate: Optional[Any] = None,
        bornString: Optional[Any] = None,
        ageAge: Optional[Any] = None,
        ageRange: Optional[Any] = None,
        ageString: Optional[Any] = None,
        estimatedAge: Optional[Any] = None,
        deceasedBoolean: Optional[Any] = None,
        deceasedAge: Optional[Any] = None,
        deceasedRange: Optional[Any] = None,
        deceasedDate: Optional[Any] = None,
        deceasedString: Optional[Any] = None,
        reasonCode: Optional[Any] = None,
        reasonReference: Optional[Any] = None,
        note: Optional[Any] = None,
        condition: Optional[Any] = None,
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
            status=status,
            dataAbsentReason=dataAbsentReason,
            patient=patient,
            date=date,
            name=name,
            relationship=relationship,
            sex=sex,
            bornPeriod=bornPeriod,
            bornDate=bornDate,
            bornString=bornString,
            ageAge=ageAge,
            ageRange=ageRange,
            ageString=ageString,
            estimatedAge=estimatedAge,
            deceasedBoolean=deceasedBoolean,
            deceasedAge=deceasedAge,
            deceasedRange=deceasedRange,
            deceasedDate=deceasedDate,
            deceasedString=deceasedString,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            note=note,
            condition=condition,
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
        Significant health conditions for a person related to the patient relevant in
        the context of care for the patient.


        resourceType: This is a FamilyMemberHistory resource

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

        identifier: Business identifiers assigned to this family member history by the performer
            or other systems which remain constant as the resource is updated and
            propagates from server to server.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this FamilyMemberHistory.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            FamilyMemberHistory.

        status: A code specifying the status of the record of the family history of a specific
            family member.

        dataAbsentReason: Describes why the family member's history is not available.

        patient: The person who this history concerns.

        date: The date (and possibly time) when the family member history was recorded or
            last updated.

        name: This will either be a name or a description; e.g. "Aunt Susan", "my cousin
            with the red hair".

        relationship: The type of relationship this person has to the patient (father, mother,
            brother etc.).

        sex: The birth sex of the family member.

        bornPeriod: The actual or approximate date of birth of the relative.

        bornDate: The actual or approximate date of birth of the relative.

        bornString: The actual or approximate date of birth of the relative.

        ageAge: The age of the relative at the time the family member history is recorded.

        ageRange: The age of the relative at the time the family member history is recorded.

        ageString: The age of the relative at the time the family member history is recorded.

        estimatedAge: If true, indicates that the age value specified is an estimated value.

        deceasedBoolean: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedAge: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedRange: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedDate: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        deceasedString: Deceased flag or the actual or approximate age of the relative at the time of
            death for the family member history record.

        reasonCode: Describes why the family member history occurred in coded or textual form.

        reasonReference: Indicates a Condition, Observation, AllergyIntolerance, or
            QuestionnaireResponse that justifies this family member history event.

        note: This property allows a non condition-specific note to the made about the
            related person. Ideally, the note would be in the condition property, but this
            is not always possible.

        condition: The significant Conditions (or condition) that the family member had. This is
            a repeating section to allow a system to represent more than one condition per
            resource, though there is nothing stopping multiple resources - one per
            condition.

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
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.age import (
            AutoMapperElasticSearchAge as AgeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.range import (
            AutoMapperElasticSearchRange as RangeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.annotation import (
            AutoMapperElasticSearchAnnotation as AnnotationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.familymemberhistory_condition import (
            AutoMapperElasticSearchFamilyMemberHistory_Condition as FamilyMemberHistory_ConditionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("FamilyMemberHistory") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["FamilyMemberHistory"]
        schema = StructType(
            [
                # This is a FamilyMemberHistory resource
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
                # Business identifiers assigned to this family member history by the performer
                # or other systems which remain constant as the resource is updated and
                # propagates from server to server.
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
                # definition that is adhered to in whole or in part by this FamilyMemberHistory.
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
                # FamilyMemberHistory.
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
                # A code specifying the status of the record of the family history of a specific
                # family member.
                StructField("status", StringType(), True),
                # Describes why the family member's history is not available.
                StructField(
                    "dataAbsentReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The person who this history concerns.
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
                # The date (and possibly time) when the family member history was recorded or
                # last updated.
                StructField(
                    "date",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # This will either be a name or a description; e.g. "Aunt Susan", "my cousin
                # with the red hair".
                StructField("name", StringType(), True),
                # The type of relationship this person has to the patient (father, mother,
                # brother etc.).
                StructField(
                    "relationship",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The birth sex of the family member.
                StructField(
                    "sex",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The actual or approximate date of birth of the relative.
                StructField(
                    "bornPeriod",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The actual or approximate date of birth of the relative.
                StructField("bornDate", DateType(), True),
                # The actual or approximate date of birth of the relative.
                StructField("bornString", StringType(), True),
                # The age of the relative at the time the family member history is recorded.
                StructField(
                    "ageAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The age of the relative at the time the family member history is recorded.
                StructField(
                    "ageRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The age of the relative at the time the family member history is recorded.
                StructField("ageString", StringType(), True),
                # If true, indicates that the age value specified is an estimated value.
                StructField("estimatedAge", BooleanType(), True),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField("deceasedBoolean", BooleanType(), True),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField(
                    "deceasedAge",
                    AgeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField(
                    "deceasedRange",
                    RangeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField("deceasedDate", DateType(), True),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField("deceasedString", StringType(), True),
                # Describes why the family member history occurred in coded or textual form.
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
                # Indicates a Condition, Observation, AllergyIntolerance, or
                # QuestionnaireResponse that justifies this family member history event.
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
                # This property allows a non condition-specific note to the made about the
                # related person. Ideally, the note would be in the condition property, but this
                # is not always possible.
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
                # The significant Conditions (or condition) that the family member had. This is
                # a repeating section to allow a system to represent more than one condition per
                # resource, though there is nothing stopping multiple resources - one per
                # condition.
                StructField(
                    "condition",
                    ArrayType(
                        FamilyMemberHistory_ConditionSchema.schema(
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
