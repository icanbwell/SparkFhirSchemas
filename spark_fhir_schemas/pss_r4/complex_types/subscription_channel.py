from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubscription_Channel(AutoMapperDataTypeComplexBase):
    """
    The subscription resource is used to define a push-based subscription from a
    server to another system. Once a subscription is registered with the server,
    the server checks every resource that is created or updated, and if the
    resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        endpoint: Optional[Any] = None,
        payload: Optional[Any] = None,
        header: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            endpoint=endpoint,
            payload=payload,
            header=header,
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
        The subscription resource is used to define a push-based subscription from a
        server to another system. Once a subscription is registered with the server,
        the server checks every resource that is created or updated, and if the
        resource matches the given criteria, it sends a message on the defined
        "channel" so that another system can take an appropriate action.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: The type of channel to send notifications on.

        endpoint: The url that describes the actual end-point to send messages to.

        payload: The mime type to send the payload in - either application/fhir+xml, or
            application/fhir+json. If the payload is not present, then there is no payload
            in the notification, just a notification. The mime type "text/plain" may also
            be used for Email and SMS subscriptions.

        header: Additional headers / information to send as part of the notification.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.url import (
            AutoMapperElasticSearchurl as urlSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Subscription_Channel") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Subscription_Channel"]
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
                # The type of channel to send notifications on.
                StructField("type", StringType(), True),
                # The url that describes the actual end-point to send messages to.
                StructField(
                    "endpoint",
                    urlSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The mime type to send the payload in - either application/fhir+xml, or
                # application/fhir+json. If the payload is not present, then there is no payload
                # in the notification, just a notification. The mime type "text/plain" may also
                # be used for Email and SMS subscriptions.
                StructField(
                    "payload",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Additional headers / information to send as part of the notification.
                StructField("header", ArrayType(StringType()), True),
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
