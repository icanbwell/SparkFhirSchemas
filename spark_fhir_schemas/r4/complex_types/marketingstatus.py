from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MarketingStatus:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The marketing status describes the date when a medicinal product is actually
        put on the market or the date as of which it is no longer available.


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

        country: The country in which the marketing authorisation has been granted shall be
            specified It should be specified using the ISO 3166 ‑ 1 alpha-2 code elements.

        jurisdiction: Where a Medicines Regulatory Agency has granted a marketing authorisation for
            which specific provisions within a jurisdiction apply, the jurisdiction can be
            specified using an appropriate controlled terminology The controlled term and
            the controlled term identifier shall be specified.

        status: This attribute provides information on the status of the marketing of the
            medicinal product See ISO/TS 20443 for more information and examples.

        dateRange: The date when the Medicinal Product is placed on the market by the Marketing
            Authorisation Holder (or where applicable, the manufacturer/distributor) in a
            country and/or jurisdiction shall be provided A complete date consisting of
            day, month and year shall be specified using the ISO 8601 date format NOTE
            “Placed on the market” refers to the release of the Medicinal Product into the
            distribution chain.

        restoreDate: The date when the Medicinal Product is placed on the market by the Marketing
            Authorisation Holder (or where applicable, the manufacturer/distributor) in a
            country and/or jurisdiction shall be provided A complete date consisting of
            day, month and year shall be specified using the ISO 8601 date format NOTE
            “Placed on the market” refers to the release of the Medicinal Product into the
            distribution chain.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
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
                # The country in which the marketing authorisation has been granted shall be
                # specified It should be specified using the ISO 3166 ‑ 1 alpha-2 code elements.
                StructField(
                    "country", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Where a Medicines Regulatory Agency has granted a marketing authorisation for
                # which specific provisions within a jurisdiction apply, the jurisdiction can be
                # specified using an appropriate controlled terminology The controlled term and
                # the controlled term identifier shall be specified.
                StructField(
                    "jurisdiction",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # This attribute provides information on the status of the marketing of the
                # medicinal product See ISO/TS 20443 for more information and examples.
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The date when the Medicinal Product is placed on the market by the Marketing
                # Authorisation Holder (or where applicable, the manufacturer/distributor) in a
                # country and/or jurisdiction shall be provided A complete date consisting of
                # day, month and year shall be specified using the ISO 8601 date format NOTE
                # “Placed on the market” refers to the release of the Medicinal Product into the
                # distribution chain.
                StructField(
                    "dateRange", Period.get_schema(recursion_depth + 1), True
                ),
                # The date when the Medicinal Product is placed on the market by the Marketing
                # Authorisation Holder (or where applicable, the manufacturer/distributor) in a
                # country and/or jurisdiction shall be provided A complete date consisting of
                # day, month and year shall be specified using the ISO 8601 date format NOTE
                # “Placed on the market” refers to the release of the Medicinal Product into the
                # distribution chain.
                StructField(
                    "restoreDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
