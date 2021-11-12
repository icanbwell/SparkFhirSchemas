from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchCapabilityStatement_Operation(
    AutoMapperDataTypeComplexBase
):
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
        name: Optional[Any] = None,
        definition: Optional[Any] = None,
        documentation: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            name=name,
            definition=definition,
            documentation=documentation,
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

        name: The name of the operation or query. For an operation, this is the name
            prefixed with $ and used in the URL. For a query, this is the name used in the
            _query parameter when the query is called.

        definition: Where the formal definition can be found. If a server references the base
            definition of an Operation (i.e. from the specification itself such as
            ```http://hl7.org/fhir/OperationDefinition/ValueSet-expand```), that means it
            supports the full capabilities of the operation - e.g. both GET and POST
            invocation.  If it only supports a subset, it must define its own custom
            [[[OperationDefinition]]] with a 'base' of the original OperationDefinition.
            The custom definition would describe the specific subset of functionality
            supported.

        documentation: Documentation that describes anything special about the operation behavior,
            possibly detailing different behavior for system, type and instance-level
            invocation of the operation.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.markdown import (
            AutoMapperElasticSearchmarkdown as markdownSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("CapabilityStatement_Operation")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CapabilityStatement_Operation"]
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
                # The name of the operation or query. For an operation, this is the name
                # prefixed with $ and used in the URL. For a query, this is the name used in the
                # _query parameter when the query is called.
                StructField("name", StringType(), True),
                # Where the formal definition can be found. If a server references the base
                # definition of an Operation (i.e. from the specification itself such as
                # ```http://hl7.org/fhir/OperationDefinition/ValueSet-expand```), that means it
                # supports the full capabilities of the operation - e.g. both GET and POST
                # invocation.  If it only supports a subset, it must define its own custom
                # [[[OperationDefinition]]] with a 'base' of the original OperationDefinition.
                # The custom definition would describe the specific subset of functionality
                # supported.
                StructField(
                    "definition",
                    canonicalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Documentation that describes anything special about the operation behavior,
                # possibly detailing different behavior for system, type and instance-level
                # invocation of the operation.
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
