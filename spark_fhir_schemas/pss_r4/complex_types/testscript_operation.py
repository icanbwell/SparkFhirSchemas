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
class AutoMapperElasticSearchTestScript_Operation(AutoMapperDataTypeComplexBase):
    """
    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        resource: Optional[Any] = None,
        label: Optional[Any] = None,
        description: Optional[Any] = None,
        accept: Optional[Any] = None,
        contentType: Optional[Any] = None,
        destination: Optional[Any] = None,
        encodeRequestUrl: Optional[Any] = None,
        method: Optional[Any] = None,
        origin: Optional[Any] = None,
        params: Optional[Any] = None,
        requestHeader: Optional[Any] = None,
        requestId: Optional[Any] = None,
        responseId: Optional[Any] = None,
        sourceId: Optional[Any] = None,
        targetId: Optional[Any] = None,
        url: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            resource=resource,
            label=label,
            description=description,
            accept=accept,
            contentType=contentType,
            destination=destination,
            encodeRequestUrl=encodeRequestUrl,
            method=method,
            origin=origin,
            params=params,
            requestHeader=requestHeader,
            requestId=requestId,
            responseId=responseId,
            sourceId=sourceId,
            targetId=targetId,
            url=url,
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
        A structured set of tests against a FHIR server or client implementation to
        determine compliance against the FHIR specification.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: Server interaction or operation type.

        resource: The type of the resource.  See http://build.fhir.org/resourcelist.html.

        label: The label would be used for tracking/logging purposes by test engines.

        description: The description would be used by test engines for tracking and reporting
            purposes.

        accept: The mime-type to use for RESTful operation in the 'Accept' header.

        contentType: The mime-type to use for RESTful operation in the 'Content-Type' header.

        destination: The server where the request message is destined for.  Must be one of the
            server numbers listed in TestScript.destination section.

        encodeRequestUrl: Whether or not to implicitly send the request url in encoded format. The
            default is true to match the standard RESTful client behavior. Set to false
            when communicating with a server that does not support encoded url paths.

        method: The HTTP method the test engine MUST use for this operation regardless of any
            other operation details.

        origin: The server where the request message originates from.  Must be one of the
            server numbers listed in TestScript.origin section.

        params: Path plus parameters after [type].  Used to set parts of the request URL
            explicitly.

        requestHeader: Header elements would be used to set HTTP headers.

        requestId: The fixture id (maybe new) to map to the request.

        responseId: The fixture id (maybe new) to map to the response.

        sourceId: The id of the fixture used as the body of a PUT or POST request.

        targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET
            requests.

        url: Complete request URL.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.testscript_requestheader import (
            AutoMapperElasticSearchTestScript_RequestHeader as TestScript_RequestHeaderSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("TestScript_Operation") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TestScript_Operation"]
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
                # Server interaction or operation type.
                StructField(
                    "type",
                    CodingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The type of the resource.  See http://build.fhir.org/resourcelist.html.
                StructField(
                    "resource",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The label would be used for tracking/logging purposes by test engines.
                StructField("label", StringType(), True),
                # The description would be used by test engines for tracking and reporting
                # purposes.
                StructField("description", StringType(), True),
                # The mime-type to use for RESTful operation in the 'Accept' header.
                StructField(
                    "accept",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The mime-type to use for RESTful operation in the 'Content-Type' header.
                StructField(
                    "contentType",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The server where the request message is destined for.  Must be one of the
                # server numbers listed in TestScript.destination section.
                StructField(
                    "destination",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Whether or not to implicitly send the request url in encoded format. The
                # default is true to match the standard RESTful client behavior. Set to false
                # when communicating with a server that does not support encoded url paths.
                StructField("encodeRequestUrl", BooleanType(), True),
                # The HTTP method the test engine MUST use for this operation regardless of any
                # other operation details.
                StructField("method", StringType(), True),
                # The server where the request message originates from.  Must be one of the
                # server numbers listed in TestScript.origin section.
                StructField(
                    "origin",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Path plus parameters after [type].  Used to set parts of the request URL
                # explicitly.
                StructField("params", StringType(), True),
                # Header elements would be used to set HTTP headers.
                StructField(
                    "requestHeader",
                    ArrayType(
                        TestScript_RequestHeaderSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The fixture id (maybe new) to map to the request.
                StructField(
                    "requestId",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The fixture id (maybe new) to map to the response.
                StructField(
                    "responseId",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The id of the fixture used as the body of a PUT or POST request.
                StructField(
                    "sourceId",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Id of fixture used for extracting the [id],  [type], and [vid] for GET
                # requests.
                StructField(
                    "targetId",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Complete request URL.
                StructField("url", StringType(), True),
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
