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
class AutoMapperElasticSearchQuestionnaire_Item(AutoMapperDataTypeComplexBase):
    """
    A structured set of questions intended to guide the collection of answers from
    end-users. Questionnaires provide detailed control over order, presentation,
    phraseology and grouping to allow coherent, consistent data collection.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        linkId: Optional[Any] = None,
        definition: Optional[Any] = None,
        code: Optional[Any] = None,
        prefix: Optional[Any] = None,
        text: Optional[Any] = None,
        type_: Optional[Any] = None,
        enableWhen: Optional[Any] = None,
        enableBehavior: Optional[Any] = None,
        required: Optional[Any] = None,
        repeats: Optional[Any] = None,
        readOnly: Optional[Any] = None,
        maxLength: Optional[Any] = None,
        answerValueSet: Optional[Any] = None,
        answerOption: Optional[Any] = None,
        initial: Optional[Any] = None,
        item: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            linkId=linkId,
            definition=definition,
            code=code,
            prefix=prefix,
            text=text,
            type_=type_,
            enableWhen=enableWhen,
            enableBehavior=enableBehavior,
            required=required,
            repeats=repeats,
            readOnly=readOnly,
            maxLength=maxLength,
            answerValueSet=answerValueSet,
            answerOption=answerOption,
            initial=initial,
            item=item,
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

        linkId: An identifier that is unique within the Questionnaire allowing linkage to the
            equivalent item in a QuestionnaireResponse resource.

        definition: This element is a URI that refers to an [[[ElementDefinition]]] that provides
            information about this item, including information that might otherwise be
            included in the instance of the Questionnaire resource. A detailed description
            of the construction of the URI is shown in Comments, below. If this element is
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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.questionnaire_enablewhen import (
            AutoMapperElasticSearchQuestionnaire_EnableWhen as Questionnaire_EnableWhenSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.questionnaire_answeroption import (
            AutoMapperElasticSearchQuestionnaire_AnswerOption as Questionnaire_AnswerOptionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.questionnaire_initial import (
            AutoMapperElasticSearchQuestionnaire_Initial as Questionnaire_InitialSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Questionnaire_Item") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Questionnaire_Item"]
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
                # An identifier that is unique within the Questionnaire allowing linkage to the
                # equivalent item in a QuestionnaireResponse resource.
                StructField("linkId", StringType(), True),
                # This element is a URI that refers to an [[[ElementDefinition]]] that provides
                # information about this item, including information that might otherwise be
                # included in the instance of the Questionnaire resource. A detailed description
                # of the construction of the URI is shown in Comments, below. If this element is
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
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A terminology code that corresponds to this group or question (e.g. a code
                # from LOINC, which defines many questions and answers).
                StructField(
                    "code",
                    ArrayType(
                        CodingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
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
                StructField("type", StringType(), True),
                # A constraint indicating that this item should only be enabled (displayed/allow
                # answers to be captured) when the specified condition is true.
                StructField(
                    "enableWhen",
                    ArrayType(
                        Questionnaire_EnableWhenSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Controls how multiple enableWhen values are interpreted -  whether all or any
                # must be true.
                StructField("enableBehavior", StringType(), True),
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
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a value set containing a list of codes representing permitted
                # answers for a "choice" or "open-choice" question.
                StructField(
                    "answerValueSet",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # One of the permitted answers for a "choice" or "open-choice" question.
                StructField(
                    "answerOption",
                    ArrayType(
                        Questionnaire_AnswerOptionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # One or more values that should be pre-populated in the answer when initially
                # rendering the questionnaire for user input.
                StructField(
                    "initial",
                    ArrayType(
                        Questionnaire_InitialSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Text, questions and other groups to be nested beneath a question or group.
                StructField(
                    "item",
                    ArrayType(
                        Questionnaire_ItemSchema.schema(
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
