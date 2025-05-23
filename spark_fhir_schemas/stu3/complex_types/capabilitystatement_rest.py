from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class CapabilityStatement_RestSchema:
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR
    Server that may be used as a statement of actual server functionality or a
    statement of required or desired server implementation.
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
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server that may be used as a statement of actual server functionality or a
        statement of required or desired server implementation.


        id: unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. In order to make the use of extensions safe and
            manageable, there is a strict set of governance  applied to the definition and
            use of extensions. Though any implementer is allowed to define an extension,
            there is a set of requirements that SHALL be met as part of the definition of
            the extension.

        mode: Identifies whether this portion of the statement is describing the ability to
            initiate or receive restful operations.

        documentation: Information about the system's restful capabilities that apply across all
            applications, such as security.

        security: Information about security implementation from an interface perspective - what
            a client needs to know.

        resource: A specification of the restful capabilities of the solution for a specific
            resource type.

        interaction: A specification of restful operations supported by the system.

        searchParam: Search parameters that are supported for searching all resources for
            implementations to support and/or make use of - either references to ones
            defined in the specification, or additional ones defined for/by the
            implementation.

        operation: Definition of an operation or a named query together with its parameters and
            their meaning and type.

        compartment: An absolute URI which is a reference to the definition of a compartment that
            the system supports. The reference is to a CompartmentDefinition resource by
            its canonical URL .

        """
        from spark_fhir_schemas.stu3.complex_types.extension import ExtensionSchema
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_security import (
            CapabilityStatement_SecuritySchema,
        )
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_resource import (
            CapabilityStatement_ResourceSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_interaction1 import (
            CapabilityStatement_Interaction1Schema,
        )
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_searchparam import (
            CapabilityStatement_SearchParamSchema,
        )
        from spark_fhir_schemas.stu3.complex_types.capabilitystatement_operation import (
            CapabilityStatement_OperationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("CapabilityStatement_Rest") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CapabilityStatement_Rest"]
        schema = StructType(
            [
                # unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
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
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Identifies whether this portion of the statement is describing the ability to
                # initiate or receive restful operations.
                StructField("mode", StringType(), True),
                # Information about the system's restful capabilities that apply across all
                # applications, such as security.
                StructField("documentation", StringType(), True),
                # Information about security implementation from an interface perspective - what
                # a client needs to know.
                StructField(
                    "security",
                    CapabilityStatement_SecuritySchema.get_schema(
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
                # A specification of the restful capabilities of the solution for a specific
                # resource type.
                StructField(
                    "resource",
                    ArrayType(
                        CapabilityStatement_ResourceSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # A specification of restful operations supported by the system.
                StructField(
                    "interaction",
                    ArrayType(
                        CapabilityStatement_Interaction1Schema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Search parameters that are supported for searching all resources for
                # implementations to support and/or make use of - either references to ones
                # defined in the specification, or additional ones defined for/by the
                # implementation.
                StructField(
                    "searchParam",
                    ArrayType(
                        CapabilityStatement_SearchParamSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # Definition of an operation or a named query together with its parameters and
                # their meaning and type.
                StructField(
                    "operation",
                    ArrayType(
                        CapabilityStatement_OperationSchema.get_schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                            extension_fields=extension_fields,
                            extension_depth=extension_depth,
                            max_extension_depth=max_extension_depth,
                        )
                    ),
                    True,
                ),
                # An absolute URI which is a reference to the definition of a compartment that
                # the system supports. The reference is to a CompartmentDefinition resource by
                # its canonical URL .
                StructField("compartment", ArrayType(StringType()), True),
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
