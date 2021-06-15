from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMarketingStatus(AutoMapperDataTypeComplexBase):
    """
    The marketing status describes the date when a medicinal product is actually
    put on the market or the date as of which it is no longer available.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        country: Optional[Any] = None,
        jurisdiction: Optional[Any] = None,
        status: Optional[Any] = None,
        dateRange: Optional[Any] = None,
        restoreDate: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            country=country,
            jurisdiction=jurisdiction,
            status=status,
            dateRange=dateRange,
            restoreDate=restoreDate,
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
        The marketing status describes the date when a medicinal product is actually
        put on the market or the date as of which it is no longer available.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.period import (
            AutoMapperElasticSearchPeriod as PeriodSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MarketingStatus") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MarketingStatus"]
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
                # The country in which the marketing authorisation has been granted shall be
                # specified It should be specified using the ISO 3166 ‑ 1 alpha-2 code elements.
                StructField(
                    "country",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Where a Medicines Regulatory Agency has granted a marketing authorisation for
                # which specific provisions within a jurisdiction apply, the jurisdiction can be
                # specified using an appropriate controlled terminology The controlled term and
                # the controlled term identifier shall be specified.
                StructField(
                    "jurisdiction",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # This attribute provides information on the status of the marketing of the
                # medicinal product See ISO/TS 20443 for more information and examples.
                StructField(
                    "status",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date when the Medicinal Product is placed on the market by the Marketing
                # Authorisation Holder (or where applicable, the manufacturer/distributor) in a
                # country and/or jurisdiction shall be provided A complete date consisting of
                # day, month and year shall be specified using the ISO 8601 date format NOTE
                # “Placed on the market” refers to the release of the Medicinal Product into the
                # distribution chain.
                StructField(
                    "dateRange",
                    PeriodSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The date when the Medicinal Product is placed on the market by the Marketing
                # Authorisation Holder (or where applicable, the manufacturer/distributor) in a
                # country and/or jurisdiction shall be provided A complete date consisting of
                # day, month and year shall be specified using the ISO 8601 date format NOTE
                # “Placed on the market” refers to the release of the Medicinal Product into the
                # distribution chain.
                StructField(
                    "restoreDate",
                    dateTimeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
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
