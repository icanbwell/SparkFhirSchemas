from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchContract_Term(AutoMapperDataTypeComplexBase):
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        identifier: Optional[Any] = None,
        issued: Optional[Any] = None,
        applies: Optional[Any] = None,
        topicCodeableConcept: Optional[Any] = None,
        topicReference: Optional[Any] = None,
        type_: Optional[Any] = None,
        subType: Optional[Any] = None,
        text: Optional[Any] = None,
        securityLabel: Optional[Any] = None,
        offer: Optional[Any] = None,
        asset: Optional[Any] = None,
        action: Optional[Any] = None,
        group: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            identifier=identifier,
            issued=issued,
            applies=applies,
            topicCodeableConcept=topicCodeableConcept,
            topicReference=topicReference,
            type_=type_,
            subType=subType,
            text=text,
            securityLabel=securityLabel,
            offer=offer,
            asset=asset,
            action=action,
            group=group,
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

        identifier: Unique identifier for this particular Contract Provision.

        issued: When this Contract Provision was issued.

        applies: Relevant time or time-period when this Contract Provision is applicable.

        topicCodeableConcept: The entity that the term applies to.

        topicReference: The entity that the term applies to.

        type: A legal clause or condition contained within a contract that requires one or
            both parties to perform a particular requirement by some specified time or
            prevents one or both parties from performing a particular requirement by some
            specified time.

        subType: A specialized legal clause or condition based on overarching contract type.

        text: Statement of a provision in a policy or a contract.

        securityLabel: Security labels that protect the handling of information about the term and
            its elements, which may be specifically identified..

        offer: The matter of concern in the context of this provision of the agrement.

        asset: Contract Term Asset List.

        action: An actor taking a role in an activity for which it can be assigned some degree
            of responsibility for the activity taking place.

        group: Nested group of Contract Provisions.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_securitylabel import (
            AutoMapperElasticSearchContract_SecurityLabel as Contract_SecurityLabelSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_offer import (
            AutoMapperElasticSearchContract_Offer as Contract_OfferSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_asset import (
            AutoMapperElasticSearchContract_Asset as Contract_AssetSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.contract_action import (
            AutoMapperElasticSearchContract_Action as Contract_ActionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Contract_Term") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Contract_Term"]
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
                # Unique identifier for this particular Contract Provision.
                StructField(
                    "identifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # When this Contract Provision was issued.
                StructField(
                    "issued",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Relevant time or time-period when this Contract Provision is applicable.
                StructField(
                    "applies",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The entity that the term applies to.
                StructField(
                    "topicCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The entity that the term applies to.
                StructField(
                    "topicReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A legal clause or condition contained within a contract that requires one or
                # both parties to perform a particular requirement by some specified time or
                # prevents one or both parties from performing a particular requirement by some
                # specified time.
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A specialized legal clause or condition based on overarching contract type.
                StructField(
                    "subType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Statement of a provision in a policy or a contract.
                StructField("text", StringType(), True),
                # Security labels that protect the handling of information about the term and
                # its elements, which may be specifically identified..
                StructField(
                    "securityLabel",
                    ArrayType(
                        Contract_SecurityLabelSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The matter of concern in the context of this provision of the agrement.
                StructField(
                    "offer",
                    Contract_OfferSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Contract Term Asset List.
                StructField(
                    "asset",
                    ArrayType(
                        Contract_AssetSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An actor taking a role in an activity for which it can be assigned some degree
                # of responsibility for the activity taking place.
                StructField(
                    "action",
                    ArrayType(
                        Contract_ActionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Nested group of Contract Provisions.
                StructField(
                    "group",
                    ArrayType(
                        Contract_TermSchema.schema(
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
