from typing import Union, List, Optional

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)


# This file is auto-generated by generate_schema so do not edit it manually
# noinspection PyPep8Naming
class TestScript_AssertSchema:
    """
    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """

    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
        extension_fields: Optional[List[str]] = None,
        extension_depth: int = 0,
        max_extension_depth: Optional[int] = 2,
        include_modifierExtension: Optional[bool] = False,
        use_date_for: Optional[List[str]] = None,
        parent_path: Optional[str] = "",
    ) -> Union[StructType, DataType]:
        """
        A structured set of tests against a FHIR server or client implementation to
        determine compliance against the FHIR specification.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        label: The label would be used for tracking/logging purposes by test engines.

        description: The description would be used by test engines for tracking and reporting
            purposes.

        direction: The direction to use for the assertion.

        compareToSourceId: Id of the source fixture used as the contents to be evaluated by either the
            "source/expression" or "sourceId/path" definition.

        compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture. When
            compareToSourceId is defined, either compareToSourceExpression or
            compareToSourcePath must be defined, but not both.

        compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture. When
            compareToSourceId is defined, either compareToSourceExpression or
            compareToSourcePath must be defined, but not both.

        contentType: The mime-type contents to compare against the request or response message
            'Content-Type' header.

        expression: The FHIRPath expression to be evaluated against the request or response
            message contents - HTTP headers and payload.

        headerField: The HTTP header field name e.g. 'Location'.

        minimumId: The ID of a fixture.  Asserts that the response contains at a minimum the
            fixture specified by minimumId.

        navigationLinks: Whether or not the test execution performs validation on the bundle navigation
            links.

        operator: The operator type defines the conditional behavior of the assert. If not
            defined, the default is equals.

        path: The XPath or JSONPath expression to be evaluated against the fixture
            representing the response received from server.

        requestMethod: The request method or HTTP operation code to compare against that used by the
            client system under test.

        requestURL: The value to use in a comparison against the request URL path string.

        resource: The type of the resource.  See http://build.fhir.org/resourcelist.html.

        response: okay | created | noContent | notModified | bad | forbidden | notFound |
            methodNotAllowed | conflict | gone | preconditionFailed | unprocessable.

        responseCode: The value of the HTTP response code to be tested.

        sourceId: Fixture to evaluate the XPath/JSONPath expression or the headerField  against.

        validateProfileId: The ID of the Profile to validate against.

        value: The value to compare to.

        warningOnly: Whether or not the test execution will produce a warning only on error for
            this assert.

        """
        if extension_fields is None:
            extension_fields = [
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
                "valueUrl",
                "valueReference",
                "valueCodeableConcept",
                "valueAddress",
            ]
        from spark_fhir_schemas.r4b.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.r4b.simple_types.code import codeSchema
        from spark_fhir_schemas.r4b.simple_types.id import idSchema

        if (
            max_recursion_limit
            and nesting_list.count("TestScript_Assert") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TestScript_Assert"]
        my_parent_path = (
            parent_path + ".testscript_assert" if parent_path else "testscript_assert"
        )
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
                        ExtensionSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
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
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                            include_modifierExtension=include_modifierExtension,
                            use_date_for=use_date_for,
                            parent_path=my_parent_path,
                        )
                    ),
                    True,
                ),
                # The label would be used for tracking/logging purposes by test engines.
                StructField("label", StringType(), True),
                # The description would be used by test engines for tracking and reporting
                # purposes.
                StructField("description", StringType(), True),
                # The direction to use for the assertion.
                StructField(
                    "direction",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".direction",
                    ),
                    True,
                ),
                # Id of the source fixture used as the contents to be evaluated by either the
                # "source/expression" or "sourceId/path" definition.
                StructField("compareToSourceId", StringType(), True),
                # The FHIRPath expression to evaluate against the source fixture. When
                # compareToSourceId is defined, either compareToSourceExpression or
                # compareToSourcePath must be defined, but not both.
                StructField("compareToSourceExpression", StringType(), True),
                # XPath or JSONPath expression to evaluate against the source fixture. When
                # compareToSourceId is defined, either compareToSourceExpression or
                # compareToSourcePath must be defined, but not both.
                StructField("compareToSourcePath", StringType(), True),
                # The mime-type contents to compare against the request or response message
                # 'Content-Type' header.
                StructField(
                    "contentType",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".contenttype",
                    ),
                    True,
                ),
                # The FHIRPath expression to be evaluated against the request or response
                # message contents - HTTP headers and payload.
                StructField("expression", StringType(), True),
                # The HTTP header field name e.g. 'Location'.
                StructField("headerField", StringType(), True),
                # The ID of a fixture.  Asserts that the response contains at a minimum the
                # fixture specified by minimumId.
                StructField("minimumId", StringType(), True),
                # Whether or not the test execution performs validation on the bundle navigation
                # links.
                StructField("navigationLinks", BooleanType(), True),
                # The operator type defines the conditional behavior of the assert. If not
                # defined, the default is equals.
                StructField(
                    "operator",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".operator",
                    ),
                    True,
                ),
                # The XPath or JSONPath expression to be evaluated against the fixture
                # representing the response received from server.
                StructField("path", StringType(), True),
                # The request method or HTTP operation code to compare against that used by the
                # client system under test.
                StructField(
                    "requestMethod",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".requestmethod",
                    ),
                    True,
                ),
                # The value to use in a comparison against the request URL path string.
                StructField("requestURL", StringType(), True),
                # The type of the resource.  See http://build.fhir.org/resourcelist.html.
                StructField(
                    "resource",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".resource",
                    ),
                    True,
                ),
                # okay | created | noContent | notModified | bad | forbidden | notFound |
                # methodNotAllowed | conflict | gone | preconditionFailed | unprocessable.
                StructField(
                    "response",
                    codeSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".response",
                    ),
                    True,
                ),
                # The value of the HTTP response code to be tested.
                StructField("responseCode", StringType(), True),
                # Fixture to evaluate the XPath/JSONPath expression or the headerField  against.
                StructField(
                    "sourceId",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".sourceid",
                    ),
                    True,
                ),
                # The ID of the Profile to validate against.
                StructField(
                    "validateProfileId",
                    idSchema.get_schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                        extension_fields=extension_fields,
                        extension_depth=extension_depth + 1,
                        max_extension_depth=max_extension_depth,
                        include_modifierExtension=include_modifierExtension,
                        use_date_for=use_date_for,
                        parent_path=my_parent_path + ".validateprofileid",
                    ),
                    True,
                ),
                # The value to compare to.
                StructField("value", StringType(), True),
                # Whether or not the test execution will produce a warning only on error for
                # this assert.
                StructField("warningOnly", BooleanType(), True),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]

        if not include_modifierExtension:
            schema.fields = [
                c
                if c.name != "modifierExtension"
                else StructField("modifierExtension", StringType(), True)
                for c in schema.fields
            ]

        return schema