from typing import Union

from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Binary:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A resource that represents the data of a single raw artifact as digital
        content accessible in its native format.  A Binary resource can contain any
        content, whether text, image, pdf, zip archive, etc.


        resourceType: This is a Binary resource

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

        contentType: MimeType of the binary content represented as a standard MimeType (BCP 13).

        securityContext: This element identifies another resource that can be used as a proxy of the
            security sensitivity to use when deciding and enforcing access control rules
            for the Binary resource. Given that the Binary resource contains very few
            elements that can be used to determine the sensitivity of the data and
            relationships to individuals, the referenced resource stands in as a proxy
            equivalent for this purpose. This referenced resource may be related to the
            Binary (e.g. Media, DocumentReference), or may be some non-related Resource
            purely as a security proxy. E.g. to identify that the binary resource relates
            to a patient, and access should only be granted to applications that have
            access to the patient.

        data: The actual content, base64 encoded.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.base64binary import base64Binary
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Binary resource
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
                # MimeType of the binary content represented as a standard MimeType (BCP 13).
                StructField(
                    "contentType", code.get_schema(recursion_depth + 1), True
                ),
                # This element identifies another resource that can be used as a proxy of the
                # security sensitivity to use when deciding and enforcing access control rules
                # for the Binary resource. Given that the Binary resource contains very few
                # elements that can be used to determine the sensitivity of the data and
                # relationships to individuals, the referenced resource stands in as a proxy
                # equivalent for this purpose. This referenced resource may be related to the
                # Binary (e.g. Media, DocumentReference), or may be some non-related Resource
                # purely as a security proxy. E.g. to identify that the binary resource relates
                # to a patient, and access should only be granted to applications that have
                # access to the patient.
                StructField(
                    "securityContext",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                # The actual content, base64 encoded.
                StructField(
                    "data", base64Binary.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
