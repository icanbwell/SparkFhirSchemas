from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    BooleanType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class FamilyMemberHistorySchema:
    """
    Significant health events and conditions for a person related to the patient
    relevant in the context of care for the patient.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
            "valueBoolean",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInteger",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueQuantity",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        Significant health events and conditions for a person related to the patient
        relevant in the context of care for the patient.


        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content may not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource, and may be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        resourceType: This is a FamilyMemberHistory resource

        identifier: This records identifiers associated with this family member history record
            that are defined by business processes and/ or used to refer to it when a
            direct URL reference to the resource itself is not appropriate (e.g. in CDA
            documents, or in written / printed documentation).

        definition: A protocol or questionnaire that was adhered to in whole or in part by this
            event.

        status: A code specifying the status of the record of the family history of a specific
            family member.

        notDone: If true, indicates the taking of an individual family member's history did not
            occur. The notDone element should not be used to document negated conditions,
            such as a family member that did not have a condition.

        notDoneReason: Describes why the family member's history is absent.

        patient: The person who this history concerns.

        date: The date (and possibly time) when the family member history was taken.

        name: This will either be a name or a description; e.g. "Aunt Susan", "my cousin
            with the red hair".

        relationship: The type of relationship this person has to the patient (father, mother,
            brother etc.).

        gender: Administrative Gender - the gender that the relative is considered to have for
            administration and record keeping purposes.

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
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.meta import MetaSchema
        from spark_fhir_schemas.stu3.complex_types.narrative import NarrativeSchema
        from spark_fhir_schemas.stu3.simple_types.resourcelist import ResourceListSchema
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.period import PeriodSchema
        from spark_fhir_schemas.stu3.complex_types.age import AgeSchema
        from spark_fhir_schemas.stu3.complex_types.range import RangeSchema
        from spark_fhir_schemas.stu3.complex_types.annotation import AnnotationSchema
        from spark_fhir_schemas.stu3.complex_types.familymemberhistory_condition import (
            FamilyMemberHistory_ConditionSchema,
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
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField("implicitRules", StringType(), True),
                # The base language in which the resource is written.
                StructField("language", StringType(), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # This is a FamilyMemberHistory resource
                StructField("resourceType", StringType(), True),
                # This records identifiers associated with this family member history record
                # that are defined by business processes and/ or used to refer to it when a
                # direct URL reference to the resource itself is not appropriate (e.g. in CDA
                # documents, or in written / printed documentation).
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # A protocol or questionnaire that was adhered to in whole or in part by this
                # event.
                StructField(
                    "definition",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # A code specifying the status of the record of the family history of a specific
                # family member.
                StructField("status", StringType(), True),
                # If true, indicates the taking of an individual family member's history did not
                # occur. The notDone element should not be used to document negated conditions,
                # such as a family member that did not have a condition.
                StructField("notDone", BooleanType(), True),
                # Describes why the family member's history is absent.
                StructField(
                    "notDoneReason",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The person who this history concerns.
                StructField(
                    "patient",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The date (and possibly time) when the family member history was taken.
                StructField("date", StringType(), True),
                # This will either be a name or a description; e.g. "Aunt Susan", "my cousin
                # with the red hair".
                StructField("name", StringType(), True),
                # The type of relationship this person has to the patient (father, mother,
                # brother etc.).
                StructField(
                    "relationship",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Administrative Gender - the gender that the relative is considered to have for
                # administration and record keeping purposes.
                StructField("gender", StringType(), True),
                # The actual or approximate date of birth of the relative.
                StructField(
                    "bornPeriod",
                    PeriodSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
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
                    AgeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The age of the relative at the time the family member history is recorded.
                StructField(
                    "ageRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
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
                    AgeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Deceased flag or the actual or approximate age of the relative at the time of
                # death for the family member history record.
                StructField(
                    "deceasedRange",
                    RangeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
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
                        CodeableConceptSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Indicates a Condition, Observation, AllergyIntolerance, or
                # QuestionnaireResponse that justifies this family member history event.
                StructField(
                    "reasonReference",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
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
                        AnnotationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
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
                        FamilyMemberHistory_ConditionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                (
                    c
                    if c.name != "extension"
                    else StructField("extension", StringType(), True)
                )
                for c in schema.fields
            ]

        return schema
