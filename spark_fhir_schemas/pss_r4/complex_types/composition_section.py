from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchComposition_Section(AutoMapperDataTypeComplexBase):
    """
    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of meaning,
    establishes its own context and that has clinical attestation with regard to
    who is making the statement. A Composition defines the structure and narrative
    content necessary for a document. However, a Composition alone does not
    constitute a document. Rather, the Composition must be the first entry in a
    Bundle where Bundle.type=document, and any other resources referenced from
    Composition must be included as subsequent entries in the Bundle (for example
    Patient, Practitioner, Encounter, etc.).
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        title: Optional[Any] = None,
        code: Optional[Any] = None,
        author: Optional[Any] = None,
        focus: Optional[Any] = None,
        text: Optional[Any] = None,
        mode: Optional[Any] = None,
        orderedBy: Optional[Any] = None,
        entry: Optional[Any] = None,
        emptyReason: Optional[Any] = None,
        section: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            title=title,
            code=code,
            author=author,
            focus=focus,
            text=text,
            mode=mode,
            orderedBy=orderedBy,
            entry=entry,
            emptyReason=emptyReason,
            section=section,
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
        A set of healthcare-related information that is assembled together into a
        single logical package that provides a single coherent statement of meaning,
        establishes its own context and that has clinical attestation with regard to
        who is making the statement. A Composition defines the structure and narrative
        content necessary for a document. However, a Composition alone does not
        constitute a document. Rather, the Composition must be the first entry in a
        Bundle where Bundle.type=document, and any other resources referenced from
        Composition must be included as subsequent entries in the Bundle (for example
        Patient, Practitioner, Encounter, etc.).


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        title: The label for this particular section.  This will be part of the rendered
            content for the document, and is often used to build a table of contents.

        code: A code identifying the kind of content contained within the section. This must
            be consistent with the section title.

        author: Identifies who is responsible for the information in this section, not
            necessarily who typed it in.

        focus: The actual focus of the section when it is not the subject of the composition,
            but instead represents something or someone associated with the subject such
            as (for a patient subject) a spouse, parent, fetus, or donor. If not focus is
            specified, the focus is assumed to be focus of the parent section, or, for a
            section in the Composition itself, the subject of the composition. Sections
            with a focus SHALL only include resources where the logical subject (patient,
            subject, focus, etc.) matches the section focus, or the resources have no
            logical subject (few resources).

        text: A human-readable narrative that contains the attested content of the section,
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.

        mode: How the entry list was prepared - whether it is a working list that is
            suitable for being maintained on an ongoing basis, or if it represents a
            snapshot of a list of items from another source, or whether it is a prepared
            list where items may be marked as added, modified or deleted.

        orderedBy: Specifies the order applied to the items in the section entries.

        entry: A reference to the actual resource from which the narrative in the section is
            derived.

        emptyReason: If the section is empty, why the list is empty. An empty section typically has
            some text explaining the empty reason.

        section: A nested sub-section within this section.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.narrative import (
            AutoMapperElasticSearchNarrative as NarrativeSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Composition_Section") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Composition_Section"]
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
                # The label for this particular section.  This will be part of the rendered
                # content for the document, and is often used to build a table of contents.
                StructField("title", StringType(), True),
                # A code identifying the kind of content contained within the section. This must
                # be consistent with the section title.
                StructField(
                    "code",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies who is responsible for the information in this section, not
                # necessarily who typed it in.
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
                # The actual focus of the section when it is not the subject of the composition,
                # but instead represents something or someone associated with the subject such
                # as (for a patient subject) a spouse, parent, fetus, or donor. If not focus is
                # specified, the focus is assumed to be focus of the parent section, or, for a
                # section in the Composition itself, the subject of the composition. Sections
                # with a focus SHALL only include resources where the logical subject (patient,
                # subject, focus, etc.) matches the section focus, or the resources have no
                # logical subject (few resources).
                StructField(
                    "focus",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A human-readable narrative that contains the attested content of the section,
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
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
                # How the entry list was prepared - whether it is a working list that is
                # suitable for being maintained on an ongoing basis, or if it represents a
                # snapshot of a list of items from another source, or whether it is a prepared
                # list where items may be marked as added, modified or deleted.
                StructField(
                    "mode",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Specifies the order applied to the items in the section entries.
                StructField(
                    "orderedBy",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to the actual resource from which the narrative in the section is
                # derived.
                StructField(
                    "entry",
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
                # If the section is empty, why the list is empty. An empty section typically has
                # some text explaining the empty reason.
                StructField(
                    "emptyReason",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A nested sub-section within this section.
                StructField(
                    "section",
                    ArrayType(
                        Composition_SectionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
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