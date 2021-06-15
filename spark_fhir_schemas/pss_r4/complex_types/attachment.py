from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchAttachment(AutoMapperDataTypeComplexBase):
    """
    For referring to data content defined in other formats.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        contentType: Optional[Any] = None,
        language: Optional[Any] = None,
        data: Optional[Any] = None,
        url: Optional[Any] = None,
        size: Optional[Any] = None,
        hash_: Optional[Any] = None,
        title: Optional[Any] = None,
        creation: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            contentType=contentType,
            language=language,
            data=data,
            url=url,
            size=size,
            hash_=hash_,
            title=title,
            creation=creation,
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
        For referring to data content defined in other formats.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        contentType: Identifies the type of the data in the attachment and allows a method to be
            chosen to interpret or render the data. Includes mime type parameters such as
            charset where appropriate.

        language: The human language of the content. The value can be any valid value according
            to BCP 47.

        data: The actual data of the attachment - a sequence of bytes, base64 encoded.

        url: A location where the data can be accessed.

        size: The number of bytes of data that make up this attachment (before base64
            encoding, if that is done).

        hash: The calculated hash of the data using SHA-1. Represented using base64.

        title: A label or set of text to display in place of the data.

        creation: The date that the attachment was first created.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.base64binary import (
            AutoMapperElasticSearchbase64Binary as base64BinarySchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.url import (
            AutoMapperElasticSearchurl as urlSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.datetime import (
            AutoMapperElasticSearchdateTime as dateTimeSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Attachment") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Attachment"]
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
                # Identifies the type of the data in the attachment and allows a method to be
                # chosen to interpret or render the data. Includes mime type parameters such as
                # charset where appropriate.
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
                # The human language of the content. The value can be any valid value according
                # to BCP 47.
                StructField(
                    "language",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The actual data of the attachment - a sequence of bytes, base64 encoded.
                StructField(
                    "data",
                    base64BinarySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A location where the data can be accessed.
                StructField(
                    "url",
                    urlSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The number of bytes of data that make up this attachment (before base64
                # encoding, if that is done).
                StructField(
                    "size",
                    unsignedIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The calculated hash of the data using SHA-1. Represented using base64.
                StructField(
                    "hash",
                    base64BinarySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A label or set of text to display in place of the data.
                StructField("title", StringType(), True),
                # The date that the attachment was first created.
                StructField(
                    "creation",
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
