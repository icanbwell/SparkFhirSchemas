from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchBundle_Request(AutoMapperDataTypeComplexBase):
    """
    A container for a collection of resources.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        method: Optional[Any] = None,
        url: Optional[Any] = None,
        ifNoneMatch: Optional[Any] = None,
        ifModifiedSince: Optional[Any] = None,
        ifMatch: Optional[Any] = None,
        ifNoneExist: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            method=method,
            url=url,
            ifNoneMatch=ifNoneMatch,
            ifModifiedSince=ifModifiedSince,
            ifMatch=ifMatch,
            ifNoneExist=ifNoneExist,
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

        method: In a transaction or batch, this is the HTTP action to be executed for this
            entry. In a history bundle, this indicates the HTTP action that occurred.

        url: The URL for this entry, relative to the root (the address to which the request
            is posted).

        ifNoneMatch: If the ETag values match, return a 304 Not Modified status. See the API
            documentation for ["Conditional Read"](http.html#cread).

        ifModifiedSince: Only perform the operation if the last updated date matches. See the API
            documentation for ["Conditional Read"](http.html#cread).

        ifMatch: Only perform the operation if the Etag value matches. For more information,
            see the API section ["Managing Resource Contention"](http.html#concurrency).

        ifNoneExist: Instruct the server not to perform the create if a specified resource already
            exists. For further information, see the API documentation for ["Conditional
            Create"](http.html#ccreate). This is just the query portion of the URL - what
            follows the "?" (not including the "?").

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

        if (
            max_recursion_limit
            and nesting_list.count("Bundle_Request") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Bundle_Request"]
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
                # In a transaction or batch, this is the HTTP action to be executed for this
                # entry. In a history bundle, this indicates the HTTP action that occurred.
                StructField("method", StringType(), True),
                # The URL for this entry, relative to the root (the address to which the request
                # is posted).
                StructField(
                    "url",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If the ETag values match, return a 304 Not Modified status. See the API
                # documentation for ["Conditional Read"](http.html#cread).
                StructField("ifNoneMatch", StringType(), True),
                # Only perform the operation if the last updated date matches. See the API
                # documentation for ["Conditional Read"](http.html#cread).
                StructField(
                    "ifModifiedSince",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Only perform the operation if the Etag value matches. For more information,
                # see the API section ["Managing Resource Contention"](http.html#concurrency).
                StructField("ifMatch", StringType(), True),
                # Instruct the server not to perform the create if a specified resource already
                # exists. For further information, see the API documentation for ["Conditional
                # Create"](http.html#ccreate). This is just the query portion of the URL - what
                # follows the "?" (not including the "?").
                StructField("ifNoneExist", StringType(), True),
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