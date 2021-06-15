from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchBundle(AutoMapperDataTypeComplexBase):
    """
    A container for a collection of resources.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        resourceType: Optional[Any] = None,
        id_: Optional[Any] = None,
        meta: Optional[Any] = None,
        implicitRules: Optional[Any] = None,
        language: Optional[Any] = None,
        identifier: Optional[Any] = None,
        type_: Optional[Any] = None,
        timestamp: Optional[Any] = None,
        total: Optional[Any] = None,
        link: Optional[Any] = None,
        entry: Optional[Any] = None,
        signature: Optional[Any] = None,
    ) -> None:
        super().__init__(
            resourceType=resourceType,
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            identifier=identifier,
            type_=type_,
            timestamp=timestamp,
            total=total,
            link=link,
            entry=entry,
            signature=signature,
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


        resourceType: This is a Bundle resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        identifier: A persistent identifier for the bundle that won't change as a bundle is copied
            from server to server.

        type: Indicates the purpose of this bundle - how it is intended to be used.

        timestamp: The date/time that the bundle was assembled - i.e. when the resources were
            placed in the bundle.

        total: If a set of search matches, this is the total number of entries of type
            'match' across all pages in the search.  It does not include search.mode =
            'include' or 'outcome' entries and it does not provide a count of the number
            of entries in the Bundle.

        link: A series of links that provide context to this bundle.

        entry: An entry in a bundle resource - will either contain a resource or information
            about a resource (transactions and history only).

        signature: Digital Signature - base64 encoded. XML-DSig or a JWT.

        """
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.meta import (
            AutoMapperElasticSearchMeta as MetaSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.instant import (
            AutoMapperElasticSearchinstant as instantSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.unsignedint import (
            AutoMapperElasticSearchunsignedInt as unsignedIntSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.bundle_link import (
            AutoMapperElasticSearchBundle_Link as Bundle_LinkSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.bundle_entry import (
            AutoMapperElasticSearchBundle_Entry as Bundle_EntrySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.signature import (
            AutoMapperElasticSearchSignature as SignatureSchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Bundle") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Bundle"]
        schema = StructType(
            [
                # This is a Bundle resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The base language in which the resource is written.
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
                # A persistent identifier for the bundle that won't change as a bundle is copied
                # from server to server.
                StructField(
                    "identifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the purpose of this bundle - how it is intended to be used.
                StructField("type", StringType(), True),
                # The date/time that the bundle was assembled - i.e. when the resources were
                # placed in the bundle.
                StructField(
                    "timestamp",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # If a set of search matches, this is the total number of entries of type
                # 'match' across all pages in the search.  It does not include search.mode =
                # 'include' or 'outcome' entries and it does not provide a count of the number
                # of entries in the Bundle.
                StructField(
                    "total",
                    unsignedIntSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A series of links that provide context to this bundle.
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
                # An entry in a bundle resource - will either contain a resource or information
                # about a resource (transactions and history only).
                StructField(
                    "entry",
                    ArrayType(
                        Bundle_EntrySchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Digital Signature - base64 encoded. XML-DSig or a JWT.
                StructField(
                    "signature",
                    SignatureSchema.schema(
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
