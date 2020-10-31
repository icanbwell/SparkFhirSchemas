from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Signature:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A signature along with supporting context. The signature may be a digital
        signature that is cryptographic in nature, or some other signature acceptable
        to the domain. This other signature may be as simple as a graphical image
        representing a hand-written signature, or a signature ceremony Different
        signature approaches have different utilities.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: An indication of the reason that the entity signed this document. This may be
            explicitly included as part of the signature information and can be used when
            determining accountability for various actions concerning the document.

        when: When the digital signature was signed.

        who: A reference to an application-usable description of the identity that signed
            (e.g. the signature used their private key).

        onBehalfOf: A reference to an application-usable description of the identity that is
            represented by the signature.

        targetFormat: A mime type that indicates the technical format of the target resources signed
            by the signature.

        sigFormat: A mime type that indicates the technical format of the signature. Important
            mime types are application/signature+xml for X ML DigSig, application/jose for
            JWS, and image/* for a graphical image of a signature, etc.

        data: The base64 encoding of the Signature content. When signature is not recorded
            electronically this element would be empty.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.simple_types.base64binary import base64Binary
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
                # An indication of the reason that the entity signed this document. This may be
                # explicitly included as part of the signature information and can be used when
                # determining accountability for various actions concerning the document.
                StructField(
                    "type", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
                # When the digital signature was signed.
                StructField(
                    "when", instant.get_schema(recursion_depth + 1), True
                ),
                # A reference to an application-usable description of the identity that signed
                # (e.g. the signature used their private key).
                StructField(
                    "who", Reference.get_schema(recursion_depth + 1), True
                ),
                # A reference to an application-usable description of the identity that is
                # represented by the signature.
                StructField(
                    "onBehalfOf", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # A mime type that indicates the technical format of the target resources signed
                # by the signature.
                StructField(
                    "targetFormat", code.get_schema(recursion_depth + 1), True
                ),
                # A mime type that indicates the technical format of the signature. Important
                # mime types are application/signature+xml for X ML DigSig, application/jose for
                # JWS, and image/* for a graphical image of a signature, etc.
                StructField(
                    "sigFormat", code.get_schema(recursion_depth + 1), True
                ),
                # The base64 encoding of the Signature content. When signature is not recorded
                # electronically this element would be empty.
                StructField(
                    "data", base64Binary.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
