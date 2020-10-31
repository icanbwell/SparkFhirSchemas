from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_Asset:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.contract_context import Contract_Context
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.contract_answer import Contract_Answer
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.contract_valueditem import Contract_ValuedItem
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Differentiates the kind of the asset .
                StructField(
                    "scope", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Target entity type about which the term may be concerned.
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Associated entities.
                StructField(
                    "typeReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # May be a subtype or part of an offered asset.
                StructField(
                    "subtype",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Specifies the applicability of the term to an asset resource instance, and
                # instances it refers to orinstances that refer to it, and/or are owned by the
                # offeree.
                StructField(
                    "relationship", Coding.get_schema(recursion_depth + 1),
                    True
                ),
                # Circumstance of the asset.
                StructField(
                    "context",
                    ArrayType(
                        Contract_Context.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Description of the quality and completeness of the asset that imay be a factor
                # in its valuation.
                StructField("condition", StringType(), True),
                # Type of Asset availability for use or ownership.
                StructField(
                    "periodType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Asset relevant contractual time period.
                StructField(
                    "period",
                    ArrayType(Period.get_schema(recursion_depth + 1)), True
                ),
                # Time period of asset use.
                StructField(
                    "usePeriod",
                    ArrayType(Period.get_schema(recursion_depth + 1)), True
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
                    ArrayType(Contract_Answer.get_schema(recursion_depth + 1)),
                    True
                ),
                # Security labels that protects the asset.
                StructField(
                    "securityLabelNumber",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
                # Contract Valued Item List.
                StructField(
                    "valuedItem",
                    ArrayType(
                        Contract_ValuedItem.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
