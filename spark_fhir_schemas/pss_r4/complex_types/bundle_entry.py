from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchBundle_Entry(AutoMapperDataTypeComplexBase):
    """
    A container for a collection of resources.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        link: Optional[Any] = None,
        fullUrl: Optional[Any] = None,
        resource: Optional[Any] = None,
        search: Optional[Any] = None,
        request: Optional[Any] = None,
        response: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            link=link,
            fullUrl=fullUrl,
            resource=resource,
            search=search,
            request=request,
            response=response,
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
        A container for a collection of resources.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        link: A series of links that provide context to this entry.

        fullUrl: The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id
            in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be
            version-independent URL consistent with the Resource.id. The fullUrl is a
            version independent reference to the resource. The fullUrl element SHALL have
            a value except that:
            * fullUrl can be empty on a POST (although it does not need to when specifying
            a temporary id for reference in the bundle)
            * Results from operations might involve resources that are not identified.

        resource: The Resource for the entry. The purpose/meaning of the resource is determined
            by the Bundle.type.

        search: Information about the search process that lead to the creation of this entry.

        request: Additional information about how this entry should be processed as part of a
            transaction or batch.  For history, it shows how the entry was processed to
            create the version contained in the entry.

        response: Indicates the results of processing the corresponding 'request' entry in the
            batch or transaction being responded to or what the results of an operation
            where when returning history.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.bundle_link import (
            AutoMapperElasticSearchBundle_Link as Bundle_LinkSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.bundle_search import (
            AutoMapperElasticSearchBundle_Search as Bundle_SearchSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.bundle_request import (
            AutoMapperElasticSearchBundle_Request as Bundle_RequestSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.bundle_response import (
            AutoMapperElasticSearchBundle_Response as Bundle_ResponseSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Bundle_Entry") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Bundle_Entry"]
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
                # A series of links that provide context to this entry.
                StructField(
                    "link",
                    ArrayType(
                        Bundle_LinkSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id
                # in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be
                # version-independent URL consistent with the Resource.id. The fullUrl is a
                # version independent reference to the resource. The fullUrl element SHALL have
                # a value except that:
                # * fullUrl can be empty on a POST (although it does not need to when specifying
                # a temporary id for reference in the bundle)
                # * Results from operations might involve resources that are not identified.
                StructField(
                    "fullUrl",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The Resource for the entry. The purpose/meaning of the resource is determined
                # by the Bundle.type.
                StructField(
                    "resource",
                    ResourceListSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Information about the search process that lead to the creation of this entry.
                StructField(
                    "search",
                    Bundle_SearchSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional information about how this entry should be processed as part of a
                # transaction or batch.  For history, it shows how the entry was processed to
                # create the version contained in the entry.
                StructField(
                    "request",
                    Bundle_RequestSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the results of processing the corresponding 'request' entry in the
                # batch or transaction being responded to or what the results of an operation
                # where when returning history.
                StructField(
                    "response",
                    Bundle_ResponseSchema.schema(
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
