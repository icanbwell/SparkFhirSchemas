from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchContract_Asset(AutoMapperDataTypeComplexBase):
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        scope: Optional[Any] = None,
        type_: Optional[Any] = None,
        typeReference: Optional[Any] = None,
        subtype: Optional[Any] = None,
        relationship: Optional[Any] = None,
        context: Optional[Any] = None,
        condition: Optional[Any] = None,
        periodType: Optional[Any] = None,
        period: Optional[Any] = None,
        usePeriod: Optional[Any] = None,
        text: Optional[Any] = None,
        linkId: Optional[Any] = None,
        answer: Optional[Any] = None,
        securityLabelNumber: Optional[Any] = None,
        valuedItem: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            scope=scope,
            type_=type_,
            typeReference=typeReference,
            subtype=subtype,
            relationship=relationship,
            context=context,
            condition=condition,
            periodType=periodType,
            period=period,
            usePeriod=usePeriod,
            text=text,
            linkId=linkId,
            answer=answer,
            securityLabelNumber=securityLabelNumber,
            valuedItem=valuedItem,
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
        Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
        a policy or agreement.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        scope: Differentiates the kind of the asset .

        type: Target entity type about which the term may be concerned.

        typeReference: Associated entities.

        subtype: May be a subtype or part of an offered asset.

        relationship: Specifies the applicability of the term to an asset resource instance, and
            instances it refers to orinstances that refer to it, and/or are owned by the
            offeree.

        context: Circumstance of the asset.

        condition: Description of the quality and completeness of the asset that imay be a factor
            in its valuation.

        periodType: Type of Asset availability for use or ownership.

        period: Asset relevant contractual time period.

        usePeriod: Time period of asset use.

        text: Clause or question text (Prose Object) concerning the asset in a linked form,
            such as a QuestionnaireResponse used in the formation of the contract.

        linkId: Id [identifier??] of the clause or question text about the asset in the
            referenced form or QuestionnaireResponse.

        answer: Response to assets.

        securityLabelNumber: Security labels that protects the asset.

        valuedItem: Contract Valued Item List.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_context import (
            AutoMapperElasticSearchContract_Context as Contract_ContextSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_answer import (
            AutoMapperElasticSearchContract_Answer as Contract_AnswerSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_valueditem import (
            AutoMapperElasticSearchContract_ValuedItem as Contract_ValuedItemSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Contract_Asset") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Contract_Asset"]
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
                # Differentiates the kind of the asset .
                StructField(
                    "scope",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Target entity type about which the term may be concerned.
                StructField(
                    "type",
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
                # Associated entities.
                StructField(
                    "typeReference",
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
                # May be a subtype or part of an offered asset.
                StructField(
                    "subtype",
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
                # Specifies the applicability of the term to an asset resource instance, and
                # instances it refers to orinstances that refer to it, and/or are owned by the
                # offeree.
                StructField(
                    "relationship",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Circumstance of the asset.
                StructField(
                    "context",
                    ArrayType(
                        Contract_ContextSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Description of the quality and completeness of the asset that imay be a factor
                # in its valuation.
                StructField("condition", StringType(), True),
                # Type of Asset availability for use or ownership.
                StructField(
                    "periodType",
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
                # Asset relevant contractual time period.
                StructField(
                    "period",
                    ArrayType(
                        PeriodSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Time period of asset use.
                StructField(
                    "usePeriod",
                    ArrayType(
                        PeriodSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Clause or question text (Prose Object) concerning the asset in a linked form,
                # such as a QuestionnaireResponse used in the formation of the contract.
                StructField("text", StringType(), True),
                # Id [identifier??] of the clause or question text about the asset in the
                # referenced form or QuestionnaireResponse.
                StructField("linkId", ArrayType(StringType()), True),
                # Response to assets.
                StructField(
                    "answer",
                    ArrayType(
                        Contract_AnswerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Security labels that protects the asset.
                StructField(
                    "securityLabelNumber",
                    ArrayType(
                        unsignedIntSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Contract Valued Item List.
                StructField(
                    "valuedItem",
                    ArrayType(
                        Contract_ValuedItemSchema.schema(
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