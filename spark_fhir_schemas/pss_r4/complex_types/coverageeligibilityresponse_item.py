from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchCoverageEligibilityResponse_Item(
    AutoMapperDataTypeComplexBase
):
    """
    This resource provides eligibility and plan details from the processing of an
    CoverageEligibilityRequest resource.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        category: Optional[Any] = None,
        productOrService: Optional[Any] = None,
        modifier: Optional[Any] = None,
        provider: Optional[Any] = None,
        excluded: Optional[Any] = None,
        name: Optional[Any] = None,
        description: Optional[Any] = None,
        network: Optional[Any] = None,
        unit: Optional[Any] = None,
        term: Optional[Any] = None,
        benefit: Optional[Any] = None,
        authorizationRequired: Optional[Any] = None,
        authorizationSupporting: Optional[Any] = None,
        authorizationUrl: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            category=category,
            productOrService=productOrService,
            modifier=modifier,
            provider=provider,
            excluded=excluded,
            name=name,
            description=description,
            network=network,
            unit=unit,
            term=term,
            benefit=benefit,
            authorizationRequired=authorizationRequired,
            authorizationSupporting=authorizationSupporting,
            authorizationUrl=authorizationUrl,
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
        This resource provides eligibility and plan details from the processing of an
        CoverageEligibilityRequest resource.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        category: Code to identify the general type of benefits under which products and
            services are provided.

        productOrService: This contains the product, service, drug or other billing code for the item.

        modifier: Item typification or modifiers codes to convey additional context for the
            product or service.

        provider: The practitioner who is eligible for the provision of the product or service.

        excluded: True if the indicated class of service is excluded from the plan, missing or
            False indicates the product or service is included in the coverage.

        name: A short name or tag for the benefit.

        description: A richer description of the benefit or services covered.

        network: Is a flag to indicate whether the benefits refer to in-network providers or
            out-of-network providers.

        unit: Indicates if the benefits apply to an individual or to the family.

        term: The term or period of the values such as 'maximum lifetime benefit' or
            'maximum annual visits'.

        benefit: Benefits used to date.

        authorizationRequired: A boolean flag indicating whether a preauthorization is required prior to
            actual service delivery.

        authorizationSupporting: Codes or comments regarding information or actions associated with the
            preauthorization.

        authorizationUrl: A web location for obtaining requirements or descriptive information regarding
            the preauthorization.

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
        from spark_fhir_schemas.pss_r4.complex_types.coverageeligibilityresponse_benefit import (
            AutoMapperElasticSearchCoverageEligibilityResponse_Benefit as CoverageEligibilityResponse_BenefitSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("CoverageEligibilityResponse_Item")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CoverageEligibilityResponse_Item"]
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
                # Code to identify the general type of benefits under which products and
                # services are provided.
                StructField(
                    "category",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # This contains the product, service, drug or other billing code for the item.
                StructField(
                    "productOrService",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Item typification or modifiers codes to convey additional context for the
                # product or service.
                StructField(
                    "modifier",
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
                # The practitioner who is eligible for the provision of the product or service.
                StructField(
                    "provider",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # True if the indicated class of service is excluded from the plan, missing or
                # False indicates the product or service is included in the coverage.
                StructField("excluded", BooleanType(), True),
                # A short name or tag for the benefit.
                StructField("name", StringType(), True),
                # A richer description of the benefit or services covered.
                StructField("description", StringType(), True),
                # Is a flag to indicate whether the benefits refer to in-network providers or
                # out-of-network providers.
                StructField(
                    "network",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates if the benefits apply to an individual or to the family.
                StructField(
                    "unit",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The term or period of the values such as 'maximum lifetime benefit' or
                # 'maximum annual visits'.
                StructField(
                    "term",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Benefits used to date.
                StructField(
                    "benefit",
                    ArrayType(
                        CoverageEligibilityResponse_BenefitSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A boolean flag indicating whether a preauthorization is required prior to
                # actual service delivery.
                StructField("authorizationRequired", BooleanType(), True),
                # Codes or comments regarding information or actions associated with the
                # preauthorization.
                StructField(
                    "authorizationSupporting",
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
                # A web location for obtaining requirements or descriptive information regarding
                # the preauthorization.
                StructField(
                    "authorizationUrl",
                    uriSchema.schema(
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
