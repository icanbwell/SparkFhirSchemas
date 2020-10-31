from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Contract_ValuedItem:
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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
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
                # Specific type of Contract Valued Item that may be priced.
                StructField(
                    "entityCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Specific type of Contract Valued Item that may be priced.
                StructField(
                    "entityReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # Identifies a Contract Valued Item instance.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the time during which this Contract ValuedItem information is
                # effective.
                StructField(
                    "effectiveTime", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Specifies the units by which the Contract Valued Item is measured or counted,
                # and quantifies the countable or measurable Contract Valued Item instances.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # A Contract Valued Item unit valuation measure.
                StructField(
                    "unitPrice", Money.get_schema(recursion_depth + 1), True
                ),
                # A real number that represents a multiplier used in determining the overall
                # value of the Contract Valued Item delivered. The concept of a Factor allows
                # for a discount or surcharge multiplier to be applied to a monetary amount.
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                # An amount that expresses the weighting (based on difficulty, cost and/or
                # resource intensiveness) associated with the Contract Valued Item delivered.
                # The concept of Points allows for assignment of point values for a Contract
                # Valued Item, such that a monetary amount can be assigned to each point.
                StructField(
                    "points", decimal.get_schema(recursion_depth + 1), True
                ),
                # Expresses the product of the Contract Valued Item unitQuantity and the
                # unitPriceAmt. For example, the formula: unit Quantity * unit Price (Cost per
                # Point) * factor Number  * points = net Amount. Quantity, factor and points are
                # assumed to be 1 if not supplied.
                StructField(
                    "net", Money.get_schema(recursion_depth + 1), True
                ),
                # Terms of valuation.
                StructField("payment", StringType(), True),
                # When payment is due.
                StructField(
                    "paymentDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                # Who will make payment.
                StructField(
                    "responsible", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Who will receive payment.
                StructField(
                    "recipient", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Id  of the clause or question text related to the context of this valuedItem
                # in the referenced form or QuestionnaireResponse.
                StructField("linkId", ArrayType(StringType()), True),
                # A set of security labels that define which terms are controlled by this
                # condition.
                StructField(
                    "securityLabelNumber",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )
        return schema
