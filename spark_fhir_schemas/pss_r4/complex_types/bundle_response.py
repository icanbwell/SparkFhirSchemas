from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchBundle_Response(AutoMapperDataTypeComplexBase):
    """
    A container for a collection of resources.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        status: Optional[Any] = None,
        location: Optional[Any] = None,
        etag: Optional[Any] = None,
        lastModified: Optional[Any] = None,
        outcome: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            status=status,
            location=location,
            etag=etag,
            lastModified=lastModified,
            outcome=outcome,
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

        status: The status code returned by processing this entry. The status SHALL start with
            a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description
            associated with the status code.

        location: The location header created by processing this operation, populated if the
            operation returns a location.

        etag: The Etag for the resource, if the operation for the entry produced a versioned
            resource (see [Resource Metadata and Versioning](http.html#versioning) and
            [Managing Resource Contention](http.html#concurrency)).

        lastModified: The date/time that the resource was modified on the server.

        outcome: An OperationOutcome containing hints and warnings produced as part of
            processing this entry in a batch or transaction.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.instant import (
            AutoMapperElasticSearchinstant as instantSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Bundle_Response") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Bundle_Response"]
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
                # The status code returned by processing this entry. The status SHALL start with
                # a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description
                # associated with the status code.
                StructField("status", StringType(), True),
                # The location header created by processing this operation, populated if the
                # operation returns a location.
                StructField(
                    "location",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The Etag for the resource, if the operation for the entry produced a versioned
                # resource (see [Resource Metadata and Versioning](http.html#versioning) and
                # [Managing Resource Contention](http.html#concurrency)).
                StructField("etag", StringType(), True),
                # The date/time that the resource was modified on the server.
                StructField(
                    "lastModified",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An OperationOutcome containing hints and warnings produced as part of
                # processing this entry in a batch or transaction.
                StructField(
                    "outcome",
                    ResourceListSchema.schema(
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