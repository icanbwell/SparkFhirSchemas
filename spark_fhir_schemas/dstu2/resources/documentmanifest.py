from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class DocumentManifestSchema:
    """
    A manifest that defines a set of documents.
    If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = [
            "valueBoolean",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInteger",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueQuantity",
        ],
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
    ) -> Union[StructType, DataType]:
        """
        A manifest that defines a set of documents.
        If the element is present, it must have either a @value, an @id, or extensions


            id: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content may not always be associated with
        version changes to the resource.
            implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content.
            language: The base language in which the resource is written.
            text: A human-readable narrative that contains a summary of the resource, and may be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            extension: May be used to represent additional information that is not part of the basic
        definition of the resource. In order to make the use of extensions safe and
        manageable, there is a strict set of governance  applied to the definition and
        use of extensions. Though any implementer is allowed to define an extension,
        there is a set of requirements that SHALL be met as part of the definition of
        the extension.
            modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource, and that modifies the understanding of the element
        that contains it. Usually modifier elements provide negation or qualification.
        In order to make the use of extensions safe and manageable, there is a strict
        set of governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.
            masterIdentifier: A single identifier that uniquely identifies this manifest. Principally used
        to refer to the manifest in non-FHIR contexts.
            identifier: Other identifiers associated with the document manifest, including version
        independent  identifiers.
            subject: Who or what the set of documents is about. The documents can be about a
        person, (patient or healthcare practitioner), a device (i.e. machine) or even
        a group of subjects (such as a document about a herd of farm animals, or a set
        of patients that share a common exposure). If the documents cross more than
        one subject, then more than one subject is allowed here (unusual use case).
            recipient: A patient, practitioner, or organization for which this set of documents is
        intended.
            type: Specifies the kind of this set of documents (e.g. Patient Summary, Discharge
        Summary, Prescription, etc.). The type of a set of documents may be the same
        as one of the documents in it - especially if there is only one - but it may
        be wider.
            author: Identifies who is responsible for creating the manifest, and adding  documents
        to it.
            created: When the document manifest was created for submission to the server (not
        necessarily the same thing as the actual resource last modified time, since it
        may be modified, replicated, etc.).
            source: Identifies the source system, application, or software that produced the
        document manifest.
            status: The status of this document manifest.
            description: Human-readable description of the source document. This is sometimes known as
        the "title".
            content: The list of Documents included in the manifest.
            related: Related identifiers or resources associated with the DocumentManifest.
        """
        # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema

        # meta
        from spark_fhir_schemas.dstu2.complex_types.meta import MetaSchema

        # implicitRules
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema

        # language
        # type = code
        # text
        from spark_fhir_schemas.dstu2.complex_types.narrative import NarrativeSchema

        # contained
        from spark_fhir_schemas.dstu2.complex_types.resourcecontainer import (
            ResourceContainerSchema,
        )

        # extension
        from spark_fhir_schemas.dstu2.complex_types.extension import ExtensionSchema

        # masterIdentifier
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema

        # subject
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema

        # type
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import (
            CodeableConceptSchema,
        )

        # created
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema

        # content
        from spark_fhir_schemas.dstu2.backbone_elements.documentmanifestcontent import (
            DocumentManifestContentSchema,
        )

        # related
        from spark_fhir_schemas.dstu2.backbone_elements.documentmanifestrelated import (
            DocumentManifestRelatedSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("DocumentManifest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["DocumentManifest"]
        schema = StructType(
            [
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content may not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content.
                StructField(
                    "implicitRules",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The base language in which the resource is written.
                StructField("language", StringType(), True),
                # A human-readable narrative that contains a summary of the resource, and may be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceContainerSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource, and that modifies the understanding of the element
                # that contains it. Usually modifier elements provide negation or qualification.
                # In order to make the use of extensions safe and manageable, there is a strict
                # set of governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                StructField(
                    "modifierExtension",
                    ArrayType(
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # A single identifier that uniquely identifies this manifest. Principally used
                # to refer to the manifest in non-FHIR contexts.
                StructField(
                    "masterIdentifier",
                    IdentifierSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
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
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
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
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
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
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
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
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
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
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # When the document manifest was created for submission to the server (not
                # necessarily the same thing as the actual resource last modified time, since it
                # may be modified, replicated, etc.).
                StructField(
                    "created",
                    dateTimeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # Identifies the source system, application, or software that produced the
                # document manifest.
                StructField(
                    "source",
                    uriSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                    ),
                    True,
                ),
                # The status of this document manifest.
                StructField("status", StringType(), True),
                # Human-readable description of the source document. This is sometimes known as
                # the "title".
                StructField("description", StringType(), True),
                # The list of Documents included in the manifest.
                StructField(
                    "content",
                    ArrayType(
                        DocumentManifestContentSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Related identifiers or resources associated with the DocumentManifest.
                StructField(
                    "related",
                    ArrayType(
                        DocumentManifestRelatedSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth + 1,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                (
                    c
                    if c.name != "extension"
                    else StructField("extension", StringType(), True)
                )
                for c in schema.fields
            ]

        return schema
