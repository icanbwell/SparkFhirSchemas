from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Invoice:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Invoice containing collected ChargeItems from an Account with calculated
        individual and total price for Billing purpose.


        resourceType: This is a Invoice resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: Identifier of this Invoice, often used for reference in correspondence about
            this invoice or for tracking of payments.

        status: The current state of the Invoice.

        cancelledReason: In case of Invoice cancellation a reason must be given (entered in error,
            superseded by corrected invoice etc.).

        type: Type of Invoice depending on domain, realm an usage (e.g. internal/external,
            dental, preliminary).

        subject: The individual or set of individuals receiving the goods and services billed
            in this invoice.

        recipient: The individual or Organization responsible for balancing of this invoice.

        date: Date/time(s) of when this Invoice was posted.

        participant: Indicates who or what performed or participated in the charged service.

        issuer: The organizationissuing the Invoice.

        account: Account which is supposed to be balanced with this Invoice.

        lineItem: Each line item represents one charge for goods and services rendered. Details
            such as date, code and amount are found in the referenced ChargeItem resource.

        totalPriceComponent: The total amount for the Invoice may be calculated as the sum of the line
            items with surcharges/deductions that apply in certain conditions.  The
            priceComponent element can be used to offer transparency to the recipient of
            the Invoice of how the total price was calculated.

        totalNet: Invoice total , taxes excluded.

        totalGross: Invoice total, tax included.

        paymentTerms: Payment details such as banking details, period of payment, deductibles,
            methods of payment.

        note: Comments made about the invoice by the issuer, subject, or other participants.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.invoice_participant import Invoice_Participant
        from spark_fhir_schemas.r4.complex_types.invoice_lineitem import Invoice_LineItem
        from spark_fhir_schemas.r4.complex_types.invoice_pricecomponent import Invoice_PriceComponent
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Invoice resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Identifier of this Invoice, often used for reference in correspondence about
                # this invoice or for tracking of payments.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The current state of the Invoice.
                StructField("status", StringType(), True),
                # In case of Invoice cancellation a reason must be given (entered in error,
                # superseded by corrected invoice etc.).
                StructField("cancelledReason", StringType(), True),
                # Type of Invoice depending on domain, realm an usage (e.g. internal/external,
                # dental, preliminary).
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The individual or set of individuals receiving the goods and services billed
                # in this invoice.
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # The individual or Organization responsible for balancing of this invoice.
                StructField(
                    "recipient", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Date/time(s) of when this Invoice was posted.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Indicates who or what performed or participated in the charged service.
                StructField(
                    "participant",
                    ArrayType(
                        Invoice_Participant.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The organizationissuing the Invoice.
                StructField(
                    "issuer", Reference.get_schema(recursion_depth + 1), True
                ),
                # Account which is supposed to be balanced with this Invoice.
                StructField(
                    "account", Reference.get_schema(recursion_depth + 1), True
                ),
                # Each line item represents one charge for goods and services rendered. Details
                # such as date, code and amount are found in the referenced ChargeItem resource.
                StructField(
                    "lineItem",
                    ArrayType(
                        Invoice_LineItem.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The total amount for the Invoice may be calculated as the sum of the line
                # items with surcharges/deductions that apply in certain conditions.  The
                # priceComponent element can be used to offer transparency to the recipient of
                # the Invoice of how the total price was calculated.
                StructField(
                    "totalPriceComponent",
                    ArrayType(
                        Invoice_PriceComponent.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Invoice total , taxes excluded.
                StructField(
                    "totalNet", Money.get_schema(recursion_depth + 1), True
                ),
                # Invoice total, tax included.
                StructField(
                    "totalGross", Money.get_schema(recursion_depth + 1), True
                ),
                # Payment details such as banking details, period of payment, deductibles,
                # methods of payment.
                StructField(
                    "paymentTerms", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # Comments made about the invoice by the issuer, subject, or other participants.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
