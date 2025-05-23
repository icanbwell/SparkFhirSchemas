from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    DateType,
    BooleanType,
    IntegerType,
    DataType,
    TimestampType,
    FloatType,
)


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class Questionnaire_EnableWhenSchema:
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
        A structured set of questions intended to guide the collection of answers from
        end-users. Questionnaires provide detailed control over order, presentation,
        phraseology and grouping to allow coherent, consistent data collection.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        question: The linkId for the question whose answer (or lack of answer) governs whether
            this item is enabled.

        hasAnswer: An indication that this item should be enabled only if the specified question
            is answered (hasAnswer=true) or not answered (hasAnswer=false).

        answerBoolean: An answer that the referenced question must match in order for the item to be
            enabled.

        answerDecimal: An answer that the referenced question must match in order for the item to be
            enabled.

        answerInteger: An answer that the referenced question must match in order for the item to be
            enabled.

        answerDate: An answer that the referenced question must match in order for the item to be
            enabled.

        answerDateTime: An answer that the referenced question must match in order for the item to be
            enabled.

        answerTime: An answer that the referenced question must match in order for the item to be
            enabled.

        answerString: An answer that the referenced question must match in order for the item to be
            enabled.

        answerUri: An answer that the referenced question must match in order for the item to be
            enabled.

        answerAttachment: An answer that the referenced question must match in order for the item to be
            enabled.

        answerCoding: An answer that the referenced question must match in order for the item to be
            enabled.

        answerQuantity: An answer that the referenced question must match in order for the item to be
            enabled.

        answerReference: An answer that the referenced question must match in order for the item to be
            enabled.

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.attachment import AttachmentSchema
        from spark_fhir_schemas.stu3.complex_types.coding import CodingSchema
        from spark_fhir_schemas.stu3.complex_types.quantity import QuantitySchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema

        if (
            max_recursion_limit
            and nesting_list.count("Questionnaire_EnableWhen") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Questionnaire_EnableWhen"]
        schema = StructType(
            [
                # unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
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
                # The linkId for the question whose answer (or lack of answer) governs whether
                # this item is enabled.
                StructField("question", StringType(), True),
                # An indication that this item should be enabled only if the specified question
                # is answered (hasAnswer=true) or not answered (hasAnswer=false).
                StructField("hasAnswer", BooleanType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerBoolean", BooleanType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerDecimal", FloatType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerInteger", IntegerType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerDate", DateType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerDateTime", TimestampType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerTime", StringType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerString", StringType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField("answerUri", StringType(), True),
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField(
                    "answerAttachment",
                    AttachmentSchema.get_schema(
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
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField(
                    "answerCoding",
                    CodingSchema.get_schema(
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
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField(
                    "answerQuantity",
                    QuantitySchema.get_schema(
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
                # An answer that the referenced question must match in order for the item to be
                # enabled.
                StructField(
                    "answerReference",
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
