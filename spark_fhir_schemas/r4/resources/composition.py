from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Composition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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


        resourceType: This is a Composition resource

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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: A version-independent identifier for the Composition. This identifier stays
            constant as the composition is changed over time.

        status: The workflow/clinical status of this composition. The status is a marker for
            the clinical standing of the document.

        type: Specifies the particular kind of composition (e.g. History and Physical,
            Discharge Summary, Progress Note). This usually equates to the purpose of
            making the composition.

        category: A categorization for the type of the composition - helps for indexing and
            searching. This may be implied by or derived from the code specified in the
            Composition Type.

        subject: Who or what the composition is about. The composition can be about a person,
            (patient or healthcare practitioner), a device (e.g. a machine) or even a
            group of subjects (such as a document about a herd of livestock, or a set of
            patients that share a common exposure).

        encounter: Describes the clinical encounter or type of care this documentation is
            associated with.

        date: The composition editing time, when the composition was last logically changed
            by the author.

        author: Identifies who is responsible for the information in the composition, not
            necessarily who typed it in.

        title: Official human-readable label for the composition.

        confidentiality: The code specifying the level of confidentiality of the Composition.

        attester: A participant who has attested to the accuracy of the composition/document.

        custodian: Identifies the organization or group who is responsible for ongoing
            maintenance of and access to the composition/document information.

        relatesTo: Relationships that this composition has with other compositions or documents
            that already exist.

        event: The clinical service, such as a colonoscopy or an appendectomy, being
            documented.

        section: The root of the sections that make up the composition.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.composition_attester import Composition_Attester
        from spark_fhir_schemas.r4.complex_types.composition_relatesto import Composition_RelatesTo
        from spark_fhir_schemas.r4.complex_types.composition_event import Composition_Event
        from spark_fhir_schemas.r4.complex_types.composition_section import Composition_Section
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a Composition resource
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
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # A version-independent identifier for the Composition. This identifier stays
                # constant as the composition is changed over time.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # The workflow/clinical status of this composition. The status is a marker for
                # the clinical standing of the document.
                StructField("status", StringType(), True),
                # Specifies the particular kind of composition (e.g. History and Physical,
                # Discharge Summary, Progress Note). This usually equates to the purpose of
                # making the composition.
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A categorization for the type of the composition - helps for indexing and
                # searching. This may be implied by or derived from the code specified in the
                # Composition Type.
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Who or what the composition is about. The composition can be about a person,
                # (patient or healthcare practitioner), a device (e.g. a machine) or even a
                # group of subjects (such as a document about a herd of livestock, or a set of
                # patients that share a common exposure).
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                # Describes the clinical encounter or type of care this documentation is
                # associated with.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The composition editing time, when the composition was last logically changed
                # by the author.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # Identifies who is responsible for the information in the composition, not
                # necessarily who typed it in.
                StructField(
                    "author",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Official human-readable label for the composition.
                StructField("title", StringType(), True),
                # The code specifying the level of confidentiality of the Composition.
                StructField(
                    "confidentiality", code.get_schema(recursion_depth + 1),
                    True
                ),
                # A participant who has attested to the accuracy of the composition/document.
                StructField(
                    "attester",
                    ArrayType(
                        Composition_Attester.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Identifies the organization or group who is responsible for ongoing
                # maintenance of and access to the composition/document information.
                StructField(
                    "custodian", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # Relationships that this composition has with other compositions or documents
                # that already exist.
                StructField(
                    "relatesTo",
                    ArrayType(
                        Composition_RelatesTo.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The clinical service, such as a colonoscopy or an appendectomy, being
                # documented.
                StructField(
                    "event",
                    ArrayType(
                        Composition_Event.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The root of the sections that make up the composition.
                StructField(
                    "section",
                    ArrayType(
                        Composition_Section.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
