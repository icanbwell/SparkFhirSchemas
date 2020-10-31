from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class RelatedArtifact:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Related artifacts such as additional documentation, justification, or
        bibliographic references.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        type: The type of relationship to the related artifact.

        label: A short label that can be used to reference the citation from elsewhere in the
            containing artifact, such as a footnote index.

        display: A brief description of the document or knowledge resource being referenced,
            suitable for display to a consumer.

        citation: A bibliographic citation for the related artifact. This text SHOULD be
            formatted according to an accepted citation format.

        url: A url for the artifact that can be followed to access the actual content.

        document: The document being referenced, represented as an attachment. This is exclusive
            with the resource element.

        resource: The related resource, such as a library, value set, profile, or other
            knowledge resource.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.simple_types.url import url
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
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
                # The type of relationship to the related artifact.
                StructField("type", StringType(), True),
                # A short label that can be used to reference the citation from elsewhere in the
                # containing artifact, such as a footnote index.
                StructField("label", StringType(), True),
                # A brief description of the document or knowledge resource being referenced,
                # suitable for display to a consumer.
                StructField("display", StringType(), True),
                # A bibliographic citation for the related artifact. This text SHOULD be
                # formatted according to an accepted citation format.
                StructField(
                    "citation", markdown.get_schema(recursion_depth + 1), True
                ),
                # A url for the artifact that can be followed to access the actual content.
                StructField("url", url.get_schema(recursion_depth + 1), True),
                # The document being referenced, represented as an attachment. This is exclusive
                # with the resource element.
                StructField(
                    "document", Attachment.get_schema(recursion_depth + 1),
                    True
                ),
                # The related resource, such as a library, value set, profile, or other
                # knowledge resource.
                StructField(
                    "resource", canonical.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
