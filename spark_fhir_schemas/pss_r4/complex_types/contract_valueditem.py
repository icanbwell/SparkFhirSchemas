from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchContract_ValuedItem(AutoMapperDataTypeComplexBase):
    """
    Legally enforceable, formally recorded unilateral or bilateral directive i.e.,
    a policy or agreement.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        entityCodeableConcept: Optional[Any] = None,
        entityReference: Optional[Any] = None,
        identifier: Optional[Any] = None,
        effectiveTime: Optional[Any] = None,
        quantity: Optional[Any] = None,
        unitPrice: Optional[Any] = None,
        factor: Optional[Any] = None,
        points: Optional[Any] = None,
        net: Optional[Any] = None,
        payment: Optional[Any] = None,
        paymentDate: Optional[Any] = None,
        responsible: Optional[Any] = None,
        recipient: Optional[Any] = None,
        linkId: Optional[Any] = None,
        securityLabelNumber: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            entityCodeableConcept=entityCodeableConcept,
            entityReference=entityReference,
            identifier=identifier,
            effectiveTime=effectiveTime,
            quantity=quantity,
            unitPrice=unitPrice,
            factor=factor,
            points=points,
            net=net,
            payment=payment,
            paymentDate=paymentDate,
            responsible=responsible,
            recipient=recipient,
            linkId=linkId,
            securityLabelNumber=securityLabelNumber,
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

        entityCodeableConcept: Specific type of Contract Valued Item that may be priced.

        entityReference: Specific type of Contract Valued Item that may be priced.

        identifier: Identifies a Contract Valued Item instance.

        effectiveTime: Indicates the time during which this Contract ValuedItem information is
            effective.

        quantity: Specifies the units by which the Contract Valued Item is measured or counted,
            and quantifies the countable or measurable Contract Valued Item instances.

        unitPrice: A Contract Valued Item unit valuation measure.

        factor: A real number that represents a multiplier used in determining the overall
            value of the Contract Valued Item delivered. The concept of a Factor allows
            for a discount or surcharge multiplier to be applied to a monetary amount.

        points: An amount that expresses the weighting (based on difficulty, cost and/or
            resource intensiveness) associated with the Contract Valued Item delivered.
            The concept of Points allows for assignment of point values for a Contract
            Valued Item, such that a monetary amount can be assigned to each point.

        net: Expresses the product of the Contract Valued Item unitQuantity and the
            unitPriceAmt. For example, the formula: unit Quantity * unit Price (Cost per
            Point) * factor Number  * points = net Amount. Quantity, factor and points are
            assumed to be 1 if not supplied.

        payment: Terms of valuation.

        paymentDate: When payment is due.

        responsible: Who will make payment.

        recipient: Who will receive payment.

        linkId: Id  of the clause or question text related to the context of this valuedItem
            in the referenced form or QuestionnaireResponse.

        securityLabelNumber: A set of security labels that define which terms are controlled by this
            condition.

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
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.money import (
            AutoMapperElasticSearchMoney as MoneySchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.decimal import (
            AutoMapperElasticSearchdecimal as decimalSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Contract_ValuedItem") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Contract_ValuedItem"]
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
                # Specific type of Contract Valued Item that may be priced.
                StructField(
                    "entityCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specific type of Contract Valued Item that may be priced.
                StructField(
                    "entityReference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies a Contract Valued Item instance.
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
                # Indicates the time during which this Contract ValuedItem information is
                # effective.
                StructField(
                    "effectiveTime",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies the units by which the Contract Valued Item is measured or counted,
                # and quantifies the countable or measurable Contract Valued Item instances.
                StructField(
                    "quantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A Contract Valued Item unit valuation measure.
                StructField(
                    "unitPrice",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A real number that represents a multiplier used in determining the overall
                # value of the Contract Valued Item delivered. The concept of a Factor allows
                # for a discount or surcharge multiplier to be applied to a monetary amount.
                StructField(
                    "factor",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An amount that expresses the weighting (based on difficulty, cost and/or
                # resource intensiveness) associated with the Contract Valued Item delivered.
                # The concept of Points allows for assignment of point values for a Contract
                # Valued Item, such that a monetary amount can be assigned to each point.
                StructField(
                    "points",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Expresses the product of the Contract Valued Item unitQuantity and the
                # unitPriceAmt. For example, the formula: unit Quantity * unit Price (Cost per
                # Point) * factor Number  * points = net Amount. Quantity, factor and points are
                # assumed to be 1 if not supplied.
                StructField(
                    "net",
                    MoneySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Terms of valuation.
                StructField("payment", StringType(), True),
                # When payment is due.
                StructField(
                    "paymentDate",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Who will make payment.
                StructField(
                    "responsible",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Who will receive payment.
                StructField(
                    "recipient",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Id  of the clause or question text related to the context of this valuedItem
                # in the referenced form or QuestionnaireResponse.
                StructField("linkId", ArrayType(StringType()), True),
                # A set of security labels that define which terms are controlled by this
                # condition.
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
