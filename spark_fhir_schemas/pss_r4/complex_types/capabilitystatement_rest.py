from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchCapabilityStatement_Rest(AutoMapperDataTypeComplexBase):
    """
    A Capability Statement documents a set of capabilities (behaviors) of a FHIR
    Server for a particular version of FHIR that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        mode: Optional[Any] = None,
        documentation: Optional[Any] = None,
        security: Optional[Any] = None,
        resource: Optional[Any] = None,
        interaction: Optional[Any] = None,
        searchParam: Optional[Any] = None,
        operation: Optional[Any] = None,
        compartment: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            mode=mode,
            documentation=documentation,
            security=security,
            resource=resource,
            interaction=interaction,
            searchParam=searchParam,
            operation=operation,
            compartment=compartment,
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
        A Capability Statement documents a set of capabilities (behaviors) of a FHIR
        Server for a particular version of FHIR that may be used as a statement of
        actual server functionality or a statement of required or desired server
        implementation.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_security import (
            AutoMapperElasticSearchCapabilityStatement_Security as CapabilityStatement_SecuritySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_resource import (
            AutoMapperElasticSearchCapabilityStatement_Resource as CapabilityStatement_ResourceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_interaction1 import (
            AutoMapperElasticSearchCapabilityStatement_Interaction1 as CapabilityStatement_Interaction1Schema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_searchparam import (
            AutoMapperElasticSearchCapabilityStatement_SearchParam as CapabilityStatement_SearchParamSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.capabilitystatement_operation import (
            AutoMapperElasticSearchCapabilityStatement_Operation as CapabilityStatement_OperationSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
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
                # Identifies whether this portion of the statement is describing the ability to
                # initiate or receive restful operations.
                StructField("mode", StringType(), True),
                # Information about the system's restful capabilities that apply across all
                # applications, such as security.
                StructField(
                    "documentation",
                    markdownSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Information about security implementation from an interface perspective - what
                # a client needs to know.
                StructField(
                    "security",
                    CapabilityStatement_SecuritySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A specification of the restful capabilities of the solution for a specific
                # resource type.
                StructField(
                    "resource",
                    ArrayType(
                        CapabilityStatement_ResourceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A specification of restful operations supported by the system.
                StructField(
                    "interaction",
                    ArrayType(
                        CapabilityStatement_Interaction1Schema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
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
                        CapabilityStatement_SearchParamSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Definition of an operation or a named query together with its parameters and
                # their meaning and type.
                StructField(
                    "operation",
                    ArrayType(
                        CapabilityStatement_OperationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # An absolute URI which is a reference to the definition of a compartment that
                # the system supports. The reference is to a CompartmentDefinition resource by
                # its canonical URL .
                StructField(
                    "compartment",
                    ArrayType(
                        canonicalSchema.schema(
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
