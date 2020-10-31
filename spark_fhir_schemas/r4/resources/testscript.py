from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TestScript:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A structured set of tests against a FHIR server or client implementation to
        determine compliance against the FHIR specification.


        resourceType: This is a TestScript resource

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

        url: An absolute URI that is used to identify this test script when it is
            referenced in a specification, model, design or an instance; also called its
            canonical identifier. This SHOULD be globally unique and SHOULD be a literal
            address at which at which an authoritative instance of this test script is (or
            will be) published. This URL can be the target of a canonical reference. It
            SHALL remain the same when the test script is stored on different servers.

        identifier: A formal identifier that is used to identify this test script when it is
            represented in other formats, or referenced in a specification, model, design
            or an instance.

        version: The identifier that is used to identify this version of the test script when
            it is referenced in a specification, model, design or instance. This is an
            arbitrary value managed by the test script author and is not expected to be
            globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
            managed version is not available. There is also no expectation that versions
            can be placed in a lexicographical sequence.

        name: A natural language name identifying the test script. This name should be
            usable as an identifier for the module by machine processing applications such
            as code generation.

        title: A short, descriptive, user-friendly title for the test script.

        status: The status of this test script. Enables tracking the life-cycle of the
            content.

        experimental: A Boolean value to indicate that this test script is authored for testing
            purposes (or education/evaluation/marketing) and is not intended to be used
            for genuine usage.

        date: The date  (and optionally time) when the test script was published. The date
            must change when the business version changes and it must change if the status
            code changes. In addition, it should change when the substantive content of
            the test script changes.

        publisher: The name of the organization or individual that published the test script.

        contact: Contact details to assist a user in finding and communicating with the
            publisher.

        description: A free text natural language description of the test script from a consumer's
            perspective.

        useContext: The content was developed with a focus and intent of supporting the contexts
            that are listed. These contexts may be general categories (gender, age, ...)
            or may be references to specific programs (insurance plans, studies, ...) and
            may be used to assist with indexing and searching for appropriate test script
            instances.

        jurisdiction: A legal or geographic region in which the test script is intended to be used.

        purpose: Explanation of why this test script is needed and why it has been designed as
            it has.

        copyright: A copyright statement relating to the test script and/or its contents.
            Copyright statements are generally legal restrictions on the use and
            publishing of the test script.

        origin: An abstract server used in operations within this test script in the origin
            element.

        destination: An abstract server used in operations within this test script in the
            destination element.

        metadata: The required capability must exist and are assumed to function correctly on
            the FHIR server being tested.

        fixture: Fixture in the test script - by reference (uri). All fixtures are required for
            the test script to execute.

        profile: Reference to the profile to be used for validation.

        variable: Variable is set based either on element value in response body or on header
            field value in the response headers.

        setup: A series of required setup operations before tests are executed.

        test: A test in this script.

        teardown: A series of operations required to clean up after all the tests are executed
            (successfully or otherwise).

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
        from spark_fhir_schemas.r4.complex_types.testscript_origin import TestScript_Origin
        from spark_fhir_schemas.r4.complex_types.testscript_destination import TestScript_Destination
        from spark_fhir_schemas.r4.complex_types.testscript_metadata import TestScript_Metadata
        from spark_fhir_schemas.r4.complex_types.testscript_fixture import TestScript_Fixture
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.testscript_variable import TestScript_Variable
        from spark_fhir_schemas.r4.complex_types.testscript_setup import TestScript_Setup
        from spark_fhir_schemas.r4.complex_types.testscript_test import TestScript_Test
        from spark_fhir_schemas.r4.complex_types.testscript_teardown import TestScript_Teardown
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a TestScript resource
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
                # An absolute URI that is used to identify this test script when it is
                # referenced in a specification, model, design or an instance; also called its
                # canonical identifier. This SHOULD be globally unique and SHOULD be a literal
                # address at which at which an authoritative instance of this test script is (or
                # will be) published. This URL can be the target of a canonical reference. It
                # SHALL remain the same when the test script is stored on different servers.
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                # A formal identifier that is used to identify this test script when it is
                # represented in other formats, or referenced in a specification, model, design
                # or an instance.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # The identifier that is used to identify this version of the test script when
                # it is referenced in a specification, model, design or instance. This is an
                # arbitrary value managed by the test script author and is not expected to be
                # globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a
                # managed version is not available. There is also no expectation that versions
                # can be placed in a lexicographical sequence.
                StructField("version", StringType(), True),
                # A natural language name identifying the test script. This name should be
                # usable as an identifier for the module by machine processing applications such
                # as code generation.
                StructField("name", StringType(), True),
                # A short, descriptive, user-friendly title for the test script.
                StructField("title", StringType(), True),
                # The status of this test script. Enables tracking the life-cycle of the
                # content.
                StructField("status", StringType(), True),
                # A Boolean value to indicate that this test script is authored for testing
                # purposes (or education/evaluation/marketing) and is not intended to be used
                # for genuine usage.
                StructField("experimental", BooleanType(), True),
                # The date  (and optionally time) when the test script was published. The date
                # must change when the business version changes and it must change if the status
                # code changes. In addition, it should change when the substantive content of
                # the test script changes.
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The name of the organization or individual that published the test script.
                StructField("publisher", StringType(), True),
                # Contact details to assist a user in finding and communicating with the
                # publisher.
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                # A free text natural language description of the test script from a consumer's
                # perspective.
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                # The content was developed with a focus and intent of supporting the contexts
                # that are listed. These contexts may be general categories (gender, age, ...)
                # or may be references to specific programs (insurance plans, studies, ...) and
                # may be used to assist with indexing and searching for appropriate test script
                # instances.
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # A legal or geographic region in which the test script is intended to be used.
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Explanation of why this test script is needed and why it has been designed as
                # it has.
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                # A copyright statement relating to the test script and/or its contents.
                # Copyright statements are generally legal restrictions on the use and
                # publishing of the test script.
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                # An abstract server used in operations within this test script in the origin
                # element.
                StructField(
                    "origin",
                    ArrayType(
                        TestScript_Origin.get_schema(recursion_depth + 1)
                    ), True
                ),
                # An abstract server used in operations within this test script in the
                # destination element.
                StructField(
                    "destination",
                    ArrayType(
                        TestScript_Destination.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The required capability must exist and are assumed to function correctly on
                # the FHIR server being tested.
                StructField(
                    "metadata",
                    TestScript_Metadata.get_schema(recursion_depth + 1), True
                ),
                # Fixture in the test script - by reference (uri). All fixtures are required for
                # the test script to execute.
                StructField(
                    "fixture",
                    ArrayType(
                        TestScript_Fixture.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Reference to the profile to be used for validation.
                StructField(
                    "profile",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Variable is set based either on element value in response body or on header
                # field value in the response headers.
                StructField(
                    "variable",
                    ArrayType(
                        TestScript_Variable.get_schema(recursion_depth + 1)
                    ), True
                ),
                # A series of required setup operations before tests are executed.
                StructField(
                    "setup", TestScript_Setup.get_schema(recursion_depth + 1),
                    True
                ),
                # A test in this script.
                StructField(
                    "test",
                    ArrayType(TestScript_Test.get_schema(recursion_depth + 1)),
                    True
                ),
                # A series of operations required to clean up after all the tests are executed
                # (successfully or otherwise).
                StructField(
                    "teardown",
                    TestScript_Teardown.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
