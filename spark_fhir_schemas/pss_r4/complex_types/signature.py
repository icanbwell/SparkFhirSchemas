from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSignature(AutoMapperDataTypeComplexBase):
    """
    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature acceptable
    to the domain. This other signature may be as simple as a graphical image
    representing a hand-written signature, or a signature ceremony Different
    signature approaches have different utilities.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        when: Optional[Any] = None,
        who: Optional[Any] = None,
        onBehalfOf: Optional[Any] = None,
        targetFormat: Optional[Any] = None,
        sigFormat: Optional[Any] = None,
        data: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            when=when,
            who=who,
            onBehalfOf=onBehalfOf,
            targetFormat=targetFormat,
            sigFormat=sigFormat,
            data=data,
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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.coding import (
            AutoMapperElasticSearchCoding as CodingSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.instant import (
            AutoMapperElasticSearchinstant as instantSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.base64binary import (
            AutoMapperElasticSearchbase64Binary as base64BinarySchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Signature") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Signature"]
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
                # An indication of the reason that the entity signed this document. This may be
                # explicitly included as part of the signature information and can be used when
                # determining accountability for various actions concerning the document.
                StructField(
                    "type",
                    ArrayType(
                        CodingSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # When the digital signature was signed.
                StructField(
                    "when",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to an application-usable description of the identity that signed
                # (e.g. the signature used their private key).
                StructField(
                    "who",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to an application-usable description of the identity that is
                # represented by the signature.
                StructField(
                    "onBehalfOf",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A mime type that indicates the technical format of the target resources signed
                # by the signature.
                StructField(
                    "targetFormat",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A mime type that indicates the technical format of the signature. Important
                # mime types are application/signature+xml for X ML DigSig, application/jose for
                # JWS, and image/* for a graphical image of a signature, etc.
                StructField(
                    "sigFormat",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The base64 encoding of the Signature content. When signature is not recorded
                # electronically this element would be empty.
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
