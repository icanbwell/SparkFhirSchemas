from typing import List
from typing import Optional
from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DocumentManifestSchema:
    """
    A collection of documents compiled for a purpose together with metadata that
    applies to the collection.
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False
    ) -> Union[StructType, DataType]:
        """
        A collection of documents compiled for a purpose together with metadata that
        applies to the collection.


        resourceType: This is a DocumentManifest resource

        masterIdentifier: A single identifier that uniquely identifies this manifest. Principally used
            to refer to the manifest in non-FHIR contexts.

        identifier: Other identifiers associated with the document manifest, including version
            independent  identifiers.

        status: The status of this document manifest.

        type: Specifies the kind of this set of documents (e.g. Patient Summary, Discharge
            Summary, Prescription, etc.). The type of a set of documents may be the same
            as one of the documents in it - especially if there is only one - but it may
            be wider.

        subject: Who or what the set of documents is about. The documents can be about a
            person, (patient or healthcare practitioner), a device (i.e. machine) or even
            a group of subjects (such as a document about a herd of farm animals, or a set
            of patients that share a common exposure). If the documents cross more than
            one subject, then more than one subject is allowed here (unusual use case).

        created: When the document manifest was created for submission to the server (not
            necessarily the same thing as the actual resource last modified time, since it
            may be modified, replicated, etc.).

        author: Identifies who is responsible for creating the manifest, and adding  documents
            to it.

        recipient: A patient, practitioner, or organization for which this set of documents is
            intended.

        source: Identifies the source system, application, or software that produced the
            document manifest.

        description: Human-readable description of the source document. This is sometimes known as
            the "title".

        content: The list of Documents included in the manifest.

        related: Related identifiers or resources associated with the DocumentManifest.

        """
        from spark_fhir_schemas.stu3.complex_types.identifier import IdentifierSchema
        from spark_fhir_schemas.stu3.complex_types.codeableconcept import CodeableConceptSchema
        from spark_fhir_schemas.stu3.complex_types.reference import ReferenceSchema
        from spark_fhir_schemas.stu3.complex_types.documentmanifest_content import DocumentManifest_ContentSchema
        from spark_fhir_schemas.stu3.complex_types.documentmanifest_related import DocumentManifest_RelatedSchema
        if (
            max_recursion_limit
            and nesting_list.count("DocumentManifest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["DocumentManifest"]
        schema = StructType(
            [
                # This is a DocumentManifest resource
                StructField("resourceType", StringType(), True),
                # A single identifier that uniquely identifies this manifest. Principally used
                # to refer to the manifest in non-FHIR contexts.
                StructField(
                    "masterIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Other identifiers associated with the document manifest, including version
                # independent  identifiers.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # The status of this document manifest.
                StructField("status", StringType(), True),
                # Specifies the kind of this set of documents (e.g. Patient Summary, Discharge
                # Summary, Prescription, etc.). The type of a set of documents may be the same
                # as one of the documents in it - especially if there is only one - but it may
                # be wider.
                StructField(
                    "type",
                    CodeableConceptSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # Who or what the set of documents is about. The documents can be about a
                # person, (patient or healthcare practitioner), a device (i.e. machine) or even
                # a group of subjects (such as a document about a herd of farm animals, or a set
                # of patients that share a common exposure). If the documents cross more than
                # one subject, then more than one subject is allowed here (unusual use case).
                StructField(
                    "subject",
                    ReferenceSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension
                    ), True
                ),
                # When the document manifest was created for submission to the server (not
                # necessarily the same thing as the actual resource last modified time, since it
                # may be modified, replicated, etc.).
                StructField("created", StringType(), True),
                # Identifies who is responsible for creating the manifest, and adding  documents
                # to it.
                StructField(
                    "author",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # A patient, practitioner, or organization for which this set of documents is
                # intended.
                StructField(
                    "recipient",
                    ArrayType(
                        ReferenceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Identifies the source system, application, or software that produced the
                # document manifest.
                StructField("source", StringType(), True),
                # Human-readable description of the source document. This is sometimes known as
                # the "title".
                StructField("description", StringType(), True),
                # The list of Documents included in the manifest.
                StructField(
                    "content",
                    ArrayType(
                        DocumentManifest_ContentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
                # Related identifiers or resources associated with the DocumentManifest.
                StructField(
                    "related",
                    ArrayType(
                        DocumentManifest_RelatedSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension
                        )
                    ), True
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c if c.name != "extension" else
                StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema