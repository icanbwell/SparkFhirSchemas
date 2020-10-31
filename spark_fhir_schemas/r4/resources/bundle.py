from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Bundle:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.simple_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.bundle_link import Bundle_Link
        from spark_fhir_schemas.r4.complex_types.bundle_entry import Bundle_Entry
        from spark_fhir_schemas.r4.complex_types.signature import Signature
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Bundle resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A persistent identifier for the bundle that won't change as a bundle is copied
                # from server to server.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the purpose of this bundle - how it is intended to be used.
                StructField("type", StringType(), True),
                # The date/time that the bundle was assembled - i.e. when the resources were
                # placed in the bundle.
                StructField(
                    "timestamp", instant.get_schema(recursion_depth + 1), True
                ),
                # If a set of search matches, this is the total number of entries of type
                # 'match' across all pages in the search.  It does not include search.mode =
                # 'include' or 'outcome' entries and it does not provide a count of the number
                # of entries in the Bundle.
                StructField(
                    "total", unsignedInt.get_schema(recursion_depth + 1), True
                ),
                # A series of links that provide context to this bundle.
                StructField(
                    "link",
                    ArrayType(Bundle_Link.get_schema(recursion_depth + 1)),
                    True
                ),
                # An entry in a bundle resource - will either contain a resource or information
                # about a resource (transactions and history only).
                StructField(
                    "entry",
                    ArrayType(Bundle_Entry.get_schema(recursion_depth + 1)),
                    True
                ),
                # Digital Signature - base64 encoded. XML-DSig or a JWT.
                StructField(
                    "signature", Signature.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
