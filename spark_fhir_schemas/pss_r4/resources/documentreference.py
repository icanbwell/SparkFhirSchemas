from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchDocumentReference(AutoMapperDataTypeComplexBase):
    """
    A reference to a document of any kind for any purpose. Provides metadata about
    the document so that the document can be discovered and managed. The scope of
    a document is any seralized object with a mime-type, so includes formal
    patient centric documents (CDA), cliical notes, scanned paper, and non-patient
    specific documents like policy text.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        resourceType: Optional[Any] = None,
        id_: Optional[Any] = None,
        meta: Optional[Any] = None,
        implicitRules: Optional[Any] = None,
        language: Optional[Any] = None,
        text: Optional[Any] = None,
        contained: Optional[Any] = None,
        extension: Optional[Any] = None,
        masterIdentifier: Optional[Any] = None,
        identifier: Optional[Any] = None,
        status: Optional[Any] = None,
        docStatus: Optional[Any] = None,
        type_: Optional[Any] = None,
        category: Optional[Any] = None,
        subject: Optional[Any] = None,
        date: Optional[Any] = None,
        author: Optional[Any] = None,
        authenticator: Optional[Any] = None,
        custodian: Optional[Any] = None,
        relatesTo: Optional[Any] = None,
        description: Optional[Any] = None,
        securityLabel: Optional[Any] = None,
        content: Optional[Any] = None,
        context: Optional[Any] = None,
    ) -> None:
        super().__init__(
            resourceType=resourceType,
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            masterIdentifier=masterIdentifier,
            identifier=identifier,
            status=status,
            docStatus=docStatus,
            type_=type_,
            category=category,
            subject=subject,
            date=date,
            author=author,
            authenticator=authenticator,
            custodian=custodian,
            relatesTo=relatesTo,
            description=description,
            securityLabel=securityLabel,
            content=content,
            context=context,
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
        A reference to a document of any kind for any purpose. Provides metadata about
        the document so that the document can be discovered and managed. The scope of
        a document is any seralized object with a mime-type, so includes formal
        patient centric documents (CDA), cliical notes, scanned paper, and non-patient
        specific documents like policy text.


        resourceType: This is a DocumentReference resource

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

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        masterIdentifier: Document identifier as assigned by the source of the document. This identifier
            is specific to this version of the document. This unique identifier may be
            used elsewhere to identify this version of the document.

        identifier: Other identifiers associated with the document, including version independent
            identifiers.

        status: The status of this document reference.

        docStatus: The status of the underlying document.

        type: Specifies the particular kind of document referenced  (e.g. History and
            Physical, Discharge Summary, Progress Note). This usually equates to the
            purpose of making the document referenced.

        category: A categorization for the type of document referenced - helps for indexing and
            searching. This may be implied by or derived from the code specified in the
            DocumentReference.type.

        subject: Who or what the document is about. The document can be about a person,
            (patient or healthcare practitioner), a device (e.g. a machine) or even a
            group of subjects (such as a document about a herd of farm animals, or a set
            of patients that share a common exposure).

        date: When the document reference was created.

        author: Identifies who is responsible for adding the information to the document.

        authenticator: Which person or organization authenticates that this document is valid.

        custodian: Identifies the organization or group who is responsible for ongoing
            maintenance of and access to the document.

        relatesTo: Relationships that this document has with other document references that
            already exist.

        description: Human-readable description of the source document.

        securityLabel: A set of Security-Tag codes specifying the level of privacy/security of the
            Document. Note that DocumentReference.meta.security contains the security
            labels of the "reference" to the document, while
            DocumentReference.securityLabel contains a snapshot of the security labels on
            the document the reference refers to.

        content: The document and format referenced. There may be multiple content element
            repetitions, each with a different format.

        context: The clinical context in which the document was prepared.

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
        from spark_fhir_schemas.pss_r4.complex_types.narrative import (
            AutoMapperElasticSearchNarrative as NarrativeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.instant import (
            AutoMapperElasticSearchinstant as instantSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.documentreference_relatesto import (
            AutoMapperElasticSearchDocumentReference_RelatesTo as DocumentReference_RelatesToSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.documentreference_content import (
            AutoMapperElasticSearchDocumentReference_Content as DocumentReference_ContentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.documentreference_context import (
            AutoMapperElasticSearchDocumentReference_Context as DocumentReference_ContextSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("DocumentReference") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["DocumentReference"]
        schema = StructType(
            [
                # This is a DocumentReference resource
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
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
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
                # Document identifier as assigned by the source of the document. This identifier
                # is specific to this version of the document. This unique identifier may be
                # used elsewhere to identify this version of the document.
                StructField(
                    "masterIdentifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Other identifiers associated with the document, including version independent
                # identifiers.
                StructField(
                    "identifier",
                    ArrayType(
                        IdentifierSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The status of this document reference.
                StructField("status", StringType(), True),
                # The status of the underlying document.
                StructField(
                    "docStatus",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies the particular kind of document referenced  (e.g. History and
                # Physical, Discharge Summary, Progress Note). This usually equates to the
                # purpose of making the document referenced.
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A categorization for the type of document referenced - helps for indexing and
                # searching. This may be implied by or derived from the code specified in the
                # DocumentReference.type.
                StructField(
                    "category",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Who or what the document is about. The document can be about a person,
                # (patient or healthcare practitioner), a device (e.g. a machine) or even a
                # group of subjects (such as a document about a herd of farm animals, or a set
                # of patients that share a common exposure).
                StructField(
                    "subject",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # When the document reference was created.
                StructField(
                    "date",
                    instantSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies who is responsible for adding the information to the document.
                StructField(
                    "author",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Which person or organization authenticates that this document is valid.
                StructField(
                    "authenticator",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the organization or group who is responsible for ongoing
                # maintenance of and access to the document.
                StructField(
                    "custodian",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Relationships that this document has with other document references that
                # already exist.
                StructField(
                    "relatesTo",
                    ArrayType(
                        DocumentReference_RelatesToSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Human-readable description of the source document.
                StructField("description", StringType(), True),
                # A set of Security-Tag codes specifying the level of privacy/security of the
                # Document. Note that DocumentReference.meta.security contains the security
                # labels of the "reference" to the document, while
                # DocumentReference.securityLabel contains a snapshot of the security labels on
                # the document the reference refers to.
                StructField(
                    "securityLabel",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The document and format referenced. There may be multiple content element
                # repetitions, each with a different format.
                StructField(
                    "content",
                    ArrayType(
                        DocumentReference_ContentSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The clinical context in which the document was prepared.
                StructField(
                    "context",
                    DocumentReference_ContextSchema.schema(
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