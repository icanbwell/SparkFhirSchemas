from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Attachment:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.base64binary import base64Binary
        from spark_fhir_schemas.r4.simple_types.url import url
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
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
                # Identifies the type of the data in the attachment and allows a method to be
                # chosen to interpret or render the data. Includes mime type parameters such as
                # charset where appropriate.
                StructField(
                    "contentType", code.get_schema(recursion_depth + 1), True
                ),
                # The human language of the content. The value can be any valid value according
                # to BCP 47.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # The actual data of the attachment - a sequence of bytes, base64 encoded.
                StructField(
                    "data", base64Binary.get_schema(recursion_depth + 1), True
                ),
                # A location where the data can be accessed.
                StructField("url", url.get_schema(recursion_depth + 1), True),
                # The number of bytes of data that make up this attachment (before base64
                # encoding, if that is done).
                StructField(
                    "size", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # The calculated hash of the data using SHA-1. Represented using base64.
                StructField(
                    "hash", base64Binary.get_schema(recursion_depth + 1), True
                ),
                # A label or set of text to display in place of the data.
                StructField("title", StringType(), True),
                # The date that the attachment was first created.
                StructField(
                    "creation", dateTime.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
