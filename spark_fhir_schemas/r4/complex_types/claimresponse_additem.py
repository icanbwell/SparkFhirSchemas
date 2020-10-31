from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ClaimResponse_AddItem:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        This resource provides the adjudication details from the processing of a Claim
        resource.


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

        itemSequence: Claim items which this service line is intended to replace.

        detailSequence: The sequence number of the details within the claim item which this line is
            intended to replace.

        subdetailSequence: The sequence number of the sub-details within the details within the claim
            item which this line is intended to replace.

        provider: The providers who are authorized for the services rendered to the patient.

        productOrService: When the value is a group code then this item collects a set of related claim
            details, otherwise this contains the product, service, drug or other billing
            code for the item.

        modifier: Item typification or modifiers codes to convey additional context for the
            product or service.

        programCode: Identifies the program under which this may be recovered.

        servicedDate: The date or dates when the service or product was supplied, performed or
            completed.

        servicedPeriod: The date or dates when the service or product was supplied, performed or
            completed.

        locationCodeableConcept: Where the product or service was provided.

        locationAddress: Where the product or service was provided.

        locationReference: Where the product or service was provided.

        quantity: The number of repetitions of a service or product.

        unitPrice: If the item is not a group then this is the fee for the product or service,
            otherwise this is the total of the fees for the details of the group.

        factor: A real number that represents a multiplier used in determining the overall
            value of services delivered and/or goods received. The concept of a Factor
            allows for a discount or surcharge multiplier to be applied to a monetary
            amount.

        net: The quantity times the unit price for an additional service or product or
            charge.

        bodySite: Physical service site on the patient (limb, tooth, etc.).

        subSite: A region or surface of the bodySite, e.g. limb region or tooth surface(s).

        noteNumber: The numbers associated with notes below which apply to the adjudication of
            this item.

        adjudication: The adjudication results.

        detail: The second-tier service adjudications for payor added services.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.claimresponse_adjudication import ClaimResponse_Adjudication
        from spark_fhir_schemas.r4.complex_types.claimresponse_detail1 import ClaimResponse_Detail1
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
                # Claim items which this service line is intended to replace.
                StructField(
                    "itemSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                # The sequence number of the details within the claim item which this line is
                # intended to replace.
                StructField(
                    "detailSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                # The sequence number of the sub-details within the details within the claim
                # item which this line is intended to replace.
                StructField(
                    "subdetailSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                # The providers who are authorized for the services rendered to the patient.
                StructField(
                    "provider",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # When the value is a group code then this item collects a set of related claim
                # details, otherwise this contains the product, service, drug or other billing
                # code for the item.
                StructField(
                    "productOrService",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Item typification or modifiers codes to convey additional context for the
                # product or service.
                StructField(
                    "modifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Identifies the program under which this may be recovered.
                StructField(
                    "programCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The date or dates when the service or product was supplied, performed or
                # completed.
                StructField("servicedDate", StringType(), True),
                # The date or dates when the service or product was supplied, performed or
                # completed.
                StructField(
                    "servicedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                # Where the product or service was provided.
                StructField(
                    "locationCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Where the product or service was provided.
                StructField(
                    "locationAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                # Where the product or service was provided.
                StructField(
                    "locationReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The number of repetitions of a service or product.
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # If the item is not a group then this is the fee for the product or service,
                # otherwise this is the total of the fees for the details of the group.
                StructField(
                    "unitPrice", Money.get_schema(recursion_depth + 1), True
                ),
                # A real number that represents a multiplier used in determining the overall
                # value of services delivered and/or goods received. The concept of a Factor
                # allows for a discount or surcharge multiplier to be applied to a monetary
                # amount.
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                # The quantity times the unit price for an additional service or product or
                # charge.
                StructField(
                    "net", Money.get_schema(recursion_depth + 1), True
                ),
                # Physical service site on the patient (limb, tooth, etc.).
                StructField(
                    "bodySite",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A region or surface of the bodySite, e.g. limb region or tooth surface(s).
                StructField(
                    "subSite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The numbers associated with notes below which apply to the adjudication of
                # this item.
                StructField(
                    "noteNumber",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                # The adjudication results.
                StructField(
                    "adjudication",
                    ArrayType(
                        ClaimResponse_Adjudication.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The second-tier service adjudications for payor added services.
                StructField(
                    "detail",
                    ArrayType(
                        ClaimResponse_Detail1.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
