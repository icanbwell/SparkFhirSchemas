from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TestReport:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A summary of information based on the results of executing a TestScript.


        resourceType: This is a TestReport resource

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

        identifier: Identifier for the TestScript assigned for external purposes outside the
            context of FHIR.

        name: A free text natural language name identifying the executed TestScript.

        status: The current state of this test report.

        testScript: Ideally this is an absolute URL that is used to identify the version-specific
            TestScript that was executed, matching the `TestScript.url`.

        result: The overall result from the execution of the TestScript.

        score: The final score (percentage of tests passed) resulting from the execution of
            the TestScript.

        tester: Name of the tester producing this report (Organization or individual).

        issued: When the TestScript was executed and this TestReport was generated.

        participant: A participant in the test execution, either the execution engine, a client, or
            a server.

        setup: The results of the series of required setup operations before the tests were
            executed.

        test: A test executed from the test script.

        teardown: The results of the series of operations required to clean up after all the
            tests were executed (successfully or otherwise).

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.testreport_participant import TestReport_Participant
        from spark_fhir_schemas.r4.complex_types.testreport_setup import TestReport_Setup
        from spark_fhir_schemas.r4.complex_types.testreport_test import TestReport_Test
        from spark_fhir_schemas.r4.complex_types.testreport_teardown import TestReport_Teardown
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a TestReport resource
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
                # Identifier for the TestScript assigned for external purposes outside the
                # context of FHIR.
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # A free text natural language name identifying the executed TestScript.
                StructField("name", StringType(), True),
                # The current state of this test report.
                StructField("status", StringType(), True),
                # Ideally this is an absolute URL that is used to identify the version-specific
                # TestScript that was executed, matching the `TestScript.url`.
                StructField(
                    "testScript", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The overall result from the execution of the TestScript.
                StructField("result", StringType(), True),
                # The final score (percentage of tests passed) resulting from the execution of
                # the TestScript.
                StructField(
                    "score", decimal.get_schema(recursion_depth + 1), True
                ),
                # Name of the tester producing this report (Organization or individual).
                StructField("tester", StringType(), True),
                # When the TestScript was executed and this TestReport was generated.
                StructField(
                    "issued", dateTime.get_schema(recursion_depth + 1), True
                ),
                # A participant in the test execution, either the execution engine, a client, or
                # a server.
                StructField(
                    "participant",
                    ArrayType(
                        TestReport_Participant.get_schema(recursion_depth + 1)
                    ), True
                ),
                # The results of the series of required setup operations before the tests were
                # executed.
                StructField(
                    "setup", TestReport_Setup.get_schema(recursion_depth + 1),
                    True
                ),
                # A test executed from the test script.
                StructField(
                    "test",
                    ArrayType(TestReport_Test.get_schema(recursion_depth + 1)),
                    True
                ),
                # The results of the series of operations required to clean up after all the
                # tests were executed (successfully or otherwise).
                StructField(
                    "teardown",
                    TestReport_Teardown.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
