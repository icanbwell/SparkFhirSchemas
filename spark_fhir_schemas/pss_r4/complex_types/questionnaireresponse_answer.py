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
class AutoMapperElasticSearchQuestionnaireResponse_Answer(
    AutoMapperDataTypeComplexBase
):
    """
    A structured set of questions and their answers. The questions are ordered and
    grouped into coherent subsets, corresponding to the structure of the grouping
    of the questionnaire being responded to.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        valueBoolean: Optional[Any] = None,
        valueDecimal: Optional[Any] = None,
        valueInteger: Optional[Any] = None,
        valueDate: Optional[Any] = None,
        valueDateTime: Optional[Any] = None,
        valueTime: Optional[Any] = None,
        valueString: Optional[Any] = None,
        valueUri: Optional[Any] = None,
        valueAttachment: Optional[Any] = None,
        valueCoding: Optional[Any] = None,
        valueQuantity: Optional[Any] = None,
        valueReference: Optional[Any] = None,
        item: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            valueBoolean=valueBoolean,
            valueDecimal=valueDecimal,
            valueInteger=valueInteger,
            valueDate=valueDate,
            valueDateTime=valueDateTime,
            valueTime=valueTime,
            valueString=valueString,
            valueUri=valueUri,
            valueAttachment=valueAttachment,
            valueCoding=valueCoding,
            valueQuantity=valueQuantity,
            valueReference=valueReference,
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
        A structured set of questions and their answers. The questions are ordered and
        grouped into coherent subsets, corresponding to the structure of the grouping
        of the questionnaire being responded to.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        valueBoolean: The answer (or one of the answers) provided by the respondent to the question.

        valueDecimal: The answer (or one of the answers) provided by the respondent to the question.

        valueInteger: The answer (or one of the answers) provided by the respondent to the question.

        valueDate: The answer (or one of the answers) provided by the respondent to the question.

        valueDateTime: The answer (or one of the answers) provided by the respondent to the question.

        valueTime: The answer (or one of the answers) provided by the respondent to the question.

        valueString: The answer (or one of the answers) provided by the respondent to the question.

        valueUri: The answer (or one of the answers) provided by the respondent to the question.

        valueAttachment: The answer (or one of the answers) provided by the respondent to the question.

        valueCoding: The answer (or one of the answers) provided by the respondent to the question.

        valueQuantity: The answer (or one of the answers) provided by the respondent to the question.

        valueReference: The answer (or one of the answers) provided by the respondent to the question.

        item: Nested groups and/or questions found within this particular answer.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
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
        from spark_fhir_schemas.pss_r4.complex_types.questionnaireresponse_item import (
            AutoMapperElasticSearchQuestionnaireResponse_Item as QuestionnaireResponse_ItemSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("QuestionnaireResponse_Answer")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["QuestionnaireResponse_Answer"]
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
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueBoolean", BooleanType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueDecimal", FloatType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueInteger", IntegerType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueDate", DateType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueDateTime", TimestampType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueTime", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueString", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField("valueUri", StringType(), True),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueCoding",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The answer (or one of the answers) provided by the respondent to the question.
                StructField(
                    "valueReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Nested groups and/or questions found within this particular answer.
                StructField(
                    "item",
                    ArrayType(
                        QuestionnaireResponse_ItemSchema.schema(
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
