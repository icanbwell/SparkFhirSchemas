from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ValueSet:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A ValueSet resource instance specifies a set of codes drawn from one or more
        code systems, intended for use in a particular context. Value sets link
        between [[[CodeSystem]]] definitions and their use in [coded
        elements](terminologies.html).


        resourceType: This is a ValueSet resource

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

        url: An absolute URI that is used to identify this value set when it is referenced
            in a specification, model, design or an instance; also called its canonical
            identifier. This SHOULD be globally unique and SHOULD be a literal address at
            which at which an authoritative instance of this value set is (or will be)
            published. This URL can be the target of a canonical reference. It SHALL
            remain the same when the value set is stored on different servers.

        identifier: A formal identifier that is used to identify this value set when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the value set when it
            is referenced in a specification, model, design or instance. This is an
            arbitrary value managed by the value set author and is not expected to be
            globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
            managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the value set. This name should be usable
            as an identifier for the module by machine processing applications such as
            code generation.

        title: A short, descriptive, user-friendly title for the value set.

        status: The status of this value set. Enables tracking the life-cycle of the content.
            The status of the value set applies to the value set definition
            (ValueSet.compose) and the associated ValueSet metadata. Expansions do not
            have a state.

        experimental: A Boolean value to indicate that this value set is authored for testing
            purposes (or education/evaluation/marketing) and is not intended to be used
            for genuine usage.

        date: The date (and optionally time) when the value set was created or revised (e.g.
            the 'content logical definition').

        publisher: The name of the organization or individual that published the value set.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the value set from a consumer's
            perspective. The textual description specifies the span of meanings for
            concepts to be included within the Value Set Expansion, and also may specify
            the intended use and limitations of the Value Set.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate value set
            instances.

        jurisdiction: A legal or geographic region in which the value set is intended to be used.

        immutable: If this is set to 'true', then no new versions of the content logical
            definition can be created.  Note: Other metadata might still change.

        purpose: Explanation of why this value set is needed and why it has been designed as it
            has.

        copyright: A copyright statement relating to the value set and/or its contents. Copyright
            statements are generally legal restrictions on the use and publishing of the
            value set.

        compose: A set of criteria that define the contents of the value set by including or
            excluding codes selected from the specified code system(s) that the value set
            draws from. This is also known as the Content Logical Definition (CLD).

        expansion: A value set can also be "expanded", where the value set is turned into a
            simple collection of enumerated codes. This element holds the expansion, if it
            has been performed.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.valueset_compose import ValueSet_Compose
        from spark_fhir_schemas.r4.complex_types.valueset_expansion import ValueSet_Expansion
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a ValueSet resource
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
                # An absolute URI that is used to identify this value set when it is referenced
                # in a specification, model, design or an instance; also called its canonical
                # identifier. This SHOULD be globally unique and SHOULD be a literal address at
                # which at which an authoritative instance of this value set is (or will be)
                # published. This URL can be the target of a canonical reference. It SHALL
                # remain the same when the value set is stored on different servers.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # A formal identifier that is used to identify this value set when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The identifier that is used to identify this version of the value set when it
                # is referenced in a specification, model, design or instance. This is an
                # arbitrary value managed by the value set author and is not expected to be
                # globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
                # managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the value set. This name should be usable
                # as an identifier for the module by machine processing applications such as
                # code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the value set.
                StructField("title", StringType(), True),
                # The status of this value set. Enables tracking the life-cycle of the content.
                # The status of the value set applies to the value set definition
                # (ValueSet.compose) and the associated ValueSet metadata. Expansions do not
                # have a state.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this value set is authored for testing
                # purposes (or education/evaluation/marketing) and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date (and optionally time) when the value set was created or revised (e.g.
                # the 'content logical definition').
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the value set.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the value set from a consumer's
                # perspective. The textual description specifies the span of meanings for
                # concepts to be included within the Value Set Expansion, and also may specify
                # the intended use and limitations of the Value Set.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate value set
                # instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the value set is intended to be used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # If this is set to 'true', then no new versions of the content logical
                # definition can be created.  Note: Other metadata might still change.
                StructField("immutable", BooleanType(), True),
                # Explanation of why this value set is needed and why it has been designed as it
                # has.
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                # A copyright statement relating to the value set and/or its contents. Copyright
                # statements are generally legal restrictions on the use and publishing of the
                # value set.
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                # A set of criteria that define the contents of the value set by including or
                # excluding codes selected from the specified code system(s) that the value set
                # draws from. This is also known as the Content Logical Definition (CLD).
                StructField(
                    "compose",
                    ValueSet_Compose.get_schema(recursion_depth + 1), True
                ),
                # A value set can also be "expanded", where the value set is turned into a
                # simple collection of enumerated codes. This element holds the expansion, if it
                # has been performed.
                StructField(
                    "expansion",
                    ValueSet_Expansion.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
