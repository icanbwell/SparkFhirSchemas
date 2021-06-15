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
    IntegerType,
    DataType,
    FloatType,
    TimestampType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchQuestionnaire_EnableWhen(AutoMapperDataTypeComplexBase):
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
        question: Optional[Any] = None,
        operator: Optional[Any] = None,
        answerBoolean: Optional[Any] = None,
        answerDecimal: Optional[Any] = None,
        answerInteger: Optional[Any] = None,
        answerDate: Optional[Any] = None,
        answerDateTime: Optional[Any] = None,
        answerTime: Optional[Any] = None,
        answerString: Optional[Any] = None,
        answerCoding: Optional[Any] = None,
        answerQuantity: Optional[Any] = None,
        answerReference: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            question=question,
            operator=operator,
            answerBoolean=answerBoolean,
            answerDecimal=answerDecimal,
            answerInteger=answerInteger,
            answerDate=answerDate,
            answerDateTime=answerDateTime,
            answerTime=answerTime,
            answerString=answerString,
            answerCoding=answerCoding,
            answerQuantity=answerQuantity,
            answerReference=answerReference,
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

        question: The linkId for the question whose answer (or lack of answer) governs whether
            this item is enabled.

        operator: Specifies the criteria by which the question is enabled.

        answerBoolean: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerDecimal: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerInteger: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerDate: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerDateTime: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerTime: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerString: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerCoding: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerQuantity: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        answerReference: A value that the referenced question is tested using the specified operator in
            order for the item to be enabled.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Questionnaire_EnableWhen") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Questionnaire_EnableWhen"]
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
                # The linkId for the question whose answer (or lack of answer) governs whether
                # this item is enabled.
                StructField("question", StringType(), True),
                # Specifies the criteria by which the question is enabled.
                StructField("operator", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerBoolean", BooleanType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerDecimal", FloatType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerInteger", IntegerType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerDate", DateType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerDateTime", TimestampType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerTime", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField("answerString", StringType(), True),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField(
                    "answerCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField(
                    "answerQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A value that the referenced question is tested using the specified operator in
                # order for the item to be enabled.
                StructField(
                    "answerReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
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
