from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class Questionnaire_ItemSchema:
    """
    A structured set of questions intended to guide the collection of answers from
    end-users. Questionnaires provide detailed control over order, presentation,
    phraseology and grouping to allow coherent, consistent data collection.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = None,
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
        include_modifierExtension: Optional[bool] = False,
        use_date_for: Optional[List[str]] = None,
        parent_path: Optional[str] = "",
    ) -> Union[StructType, DataType]:
        """
        A structured set of questions intended to guide the collection of answers from
        end-users. Questionnaires provide detailed control over order, presentation,
        phraseology and grouping to allow coherent, consistent data collection.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        linkId: An identifier that is unique within the Questionnaire allowing linkage to the
            equivalent item in a QuestionnaireResponse resource.

        definition: This element is a URI that refers to an
            [ElementDefinition](elementdefinition.html) that provides information about
            this item, including information that might otherwise be included in the
            instance of the Questionnaire resource. A detailed description of the
            construction of the URI is shown in Comments, below. If this element is
            present then the following element values MAY be derived from the Element
            Definition if the corresponding elements of this Questionnaire resource
            instance have no value:

            * code (ElementDefinition.code)
            * type (ElementDefinition.type)
            * required (ElementDefinition.min)
            * repeats (ElementDefinition.max)
            * maxLength (ElementDefinition.maxLength)
            * answerValueSet (ElementDefinition.binding)
            * options (ElementDefinition.binding).

        code: A terminology code that corresponds to this group or question (e.g. a code
            from LOINC, which defines many questions and answers).

        prefix: A short label for a particular group, question or set of display text within
            the questionnaire used for reference by the individual completing the
            questionnaire.

        text: The name of a section, the text of a question or text content for a display
            item.

        type: The type of questionnaire item this is - whether text for display, a grouping
            of other items or a particular type of data to be captured (string, integer,
            coded choice, etc.).

        enableWhen: A constraint indicating that this item should only be enabled (displayed/allow
            answers to be captured) when the specified condition is true.

        enableBehavior: Controls how multiple enableWhen values are interpreted -  whether all or any
            must be true.

        required: An indication, if true, that the item must be present in a "completed"
            QuestionnaireResponse.  If false, the item may be skipped when answering the
            questionnaire.

        repeats: An indication, if true, that the item may occur multiple times in the
            response, collecting multiple answers for questions or multiple sets of
            answers for groups.

        readOnly: An indication, when true, that the value cannot be changed by a human
            respondent to the Questionnaire.

        maxLength: The maximum number of characters that are permitted in the answer to be
            considered a "valid" QuestionnaireResponse.

        answerValueSet: A reference to a value set containing a list of codes representing permitted
            answers for a "choice" or "open-choice" question.

        answerOption: One of the permitted answers for a "choice" or "open-choice" question.

        initial: One or more values that should be pre-populated in the answer when initially
            rendering the questionnaire for user input.

        item: Text, questions and other groups to be nested beneath a question or group.

        """
        if extension_fields is None:
            extension_fields = [
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
                "valueUrl",
                "valueReference",
                "valueCodeableConcept",
                "valueAddress",
            ]
        from spark_fhir_schemas.r4b.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4b.simple_types.uri import uriSchema
        from spark_fhir_schemas.r4b.complex_types.coding import CodingSchema
        from spark_fhir_schemas.r4b.simple_types.code import codeSchema
        from spark_fhir_schemas.r4b.complex_types.questionnaire_enablewhen import (
            Questionnaire_EnableWhenSchema,
        )
        from spark_fhir_schemas.r4b.simple_types.integer import integerSchema
        from spark_fhir_schemas.r4b.simple_types.canonical import canonicalSchema
        from spark_fhir_schemas.r4b.complex_types.questionnaire_answeroption import (
            Questionnaire_AnswerOptionSchema,
        )
        from spark_fhir_schemas.r4b.complex_types.questionnaire_initial import (
            Questionnaire_InitialSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Questionnaire_Item") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Questionnaire_Item"]
        my_parent_path = (
            parent_path + ".questionnaire_item" if parent_path else "questionnaire_item"
        )
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
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
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
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
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # An identifier that is unique within the Questionnaire allowing linkage to the
                # equivalent item in a QuestionnaireResponse resource.
                StructField("linkId", StringType(), True),
                # This element is a URI that refers to an
                # [ElementDefinition](elementdefinition.html) that provides information about
                # this item, including information that might otherwise be included in the
                # instance of the Questionnaire resource. A detailed description of the
                # construction of the URI is shown in Comments, below. If this element is
                # present then the following element values MAY be derived from the Element
                # Definition if the corresponding elements of this Questionnaire resource
                # instance have no value:
                #
                # * code (ElementDefinition.code)
                # * type (ElementDefinition.type)
                # * required (ElementDefinition.min)
                # * repeats (ElementDefinition.max)
                # * maxLength (ElementDefinition.maxLength)
                # * answerValueSet (ElementDefinition.binding)
                # * options (ElementDefinition.binding).
                StructField(
                    "definition",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".definition",
                    ),
                    True,
                ),
                # A terminology code that corresponds to this group or question (e.g. a code
                # from LOINC, which defines many questions and answers).
                StructField(
                    "code",
                    ArrayType(
                        CodingSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # A short label for a particular group, question or set of display text within
                # the questionnaire used for reference by the individual completing the
                # questionnaire.
                StructField("prefix", StringType(), True),
                # The name of a section, the text of a question or text content for a display
                # item.
                StructField("text", StringType(), True),
                # The type of questionnaire item this is - whether text for display, a grouping
                # of other items or a particular type of data to be captured (string, integer,
                # coded choice, etc.).
                StructField(
                    "type",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".type",
                    ),
                    True,
                ),
                # A constraint indicating that this item should only be enabled (displayed/allow
                # answers to be captured) when the specified condition is true.
                StructField(
                    "enableWhen",
                    ArrayType(
                        Questionnaire_EnableWhenSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # Controls how multiple enableWhen values are interpreted -  whether all or any
                # must be true.
                StructField(
                    "enableBehavior",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".enablebehavior",
                    ),
                    True,
                ),
                # An indication, if true, that the item must be present in a "completed"
                # QuestionnaireResponse.  If false, the item may be skipped when answering the
                # questionnaire.
                StructField("required", BooleanType(), True),
                # An indication, if true, that the item may occur multiple times in the
                # response, collecting multiple answers for questions or multiple sets of
                # answers for groups.
                StructField("repeats", BooleanType(), True),
                # An indication, when true, that the value cannot be changed by a human
                # respondent to the Questionnaire.
                StructField("readOnly", BooleanType(), True),
                # The maximum number of characters that are permitted in the answer to be
                # considered a "valid" QuestionnaireResponse.
                StructField(
                    "maxLength",
                    integerSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".maxlength",
                    ),
                    True,
                ),
                # A reference to a value set containing a list of codes representing permitted
                # answers for a "choice" or "open-choice" question.
                StructField(
                    "answerValueSet",
                    canonicalSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".answervalueset",
                    ),
                    True,
                ),
                # One of the permitted answers for a "choice" or "open-choice" question.
                StructField(
                    "answerOption",
                    ArrayType(
                        Questionnaire_AnswerOptionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # One or more values that should be pre-populated in the answer when initially
                # rendering the questionnaire for user input.
                StructField(
                    "initial",
                    ArrayType(
                        Questionnaire_InitialSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # Text, questions and other groups to be nested beneath a question or group.
                StructField(
                    "item",
                    ArrayType(
                        Questionnaire_ItemSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
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

        if not include_modifierExtension:
            schema.fields = [
                c
                if c.name != "modifierExtension"
                else StructField("modifierExtension", StringType(), True)
                for c in schema.fields
            ]

        return schema