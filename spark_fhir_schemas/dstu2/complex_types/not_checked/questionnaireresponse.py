from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireResponseSchema:
    """
    A structured set of questions and their answers. The questions are ordered and
    grouped into coherent subsets, corresponding to the structure of the grouping
    of the questionnaire being responded to.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
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


        resourceType: This is a QuestionnaireResponse resource

        identifier: A business identifier assigned to a particular completed (or partially
            completed) questionnaire.

        basedOn: The order, proposal or plan that is fulfilled in whole or in part by this
            QuestionnaireResponse.  For example, a ProcedureRequest seeking an intake
            assessment or a decision support recommendation to assess for post-partum
            depression.

        parent: A procedure or observation that this questionnaire was performed as part of
            the execution of.  For example, the surgery a checklist was executed as part
            of.

        questionnaire: The Questionnaire that defines and organizes the questions for which answers
            are being provided.

        status: The position of the questionnaire response within its overall lifecycle.

        subject: The subject of the questionnaire response.  This could be a patient,
            organization, practitioner, device, etc.  This is who/what the answers apply
            to, but is not necessarily the source of information.

        context: The encounter or episode of care with primary association to the questionnaire
            response.

        authored: The date and/or time that this set of answers were last changed.

        author: Person who received the answers to the questions in the QuestionnaireResponse
            and recorded them in the system.

        source: The person who answered the questions about the subject.

        item: A group or question item from the original questionnaire for which answers are
            provided.

        """
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.dstu2.complex_types.not_checked.questionnaireresponse_item import (
            QuestionnaireResponse_ItemSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("QuestionnaireResponse") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["QuestionnaireResponse"]
        schema = StructType(
            [
                # This is a QuestionnaireResponse resource
                StructField("resourceType", StringType(), True),
                # A business identifier assigned to a particular completed (or partially
                # completed) questionnaire.
                StructField(
                    "identifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The order, proposal or plan that is fulfilled in whole or in part by this
                # QuestionnaireResponse.  For example, a ProcedureRequest seeking an intake
                # assessment or a decision support recommendation to assess for post-partum
                # depression.
                StructField(
                    "basedOn",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A procedure or observation that this questionnaire was performed as part of
                # the execution of.  For example, the surgery a checklist was executed as part
                # of.
                StructField(
                    "parent",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The Questionnaire that defines and organizes the questions for which answers
                # are being provided.
                StructField(
                    "questionnaire",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The position of the questionnaire response within its overall lifecycle.
                StructField("status", StringType(), True),
                # The subject of the questionnaire response.  This could be a patient,
                # organization, practitioner, device, etc.  This is who/what the answers apply
                # to, but is not necessarily the source of information.
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The encounter or episode of care with primary association to the questionnaire
                # response.
                StructField(
                    "context",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date and/or time that this set of answers were last changed.
                StructField("authored", StringType(), True),
                # Person who received the answers to the questions in the QuestionnaireResponse
                # and recorded them in the system.
                StructField(
                    "author",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The person who answered the questions about the subject.
                StructField(
                    "source",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A group or question item from the original questionnaire for which answers are
                # provided.
                StructField(
                    "item",
                    ArrayType(
                        QuestionnaireResponse_ItemSchema.get_schema(
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