from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchTestScript_Variable(AutoMapperDataTypeComplexBase):
    """
    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        name: Optional[Any] = None,
        defaultValue: Optional[Any] = None,
        description: Optional[Any] = None,
        expression: Optional[Any] = None,
        headerField: Optional[Any] = None,
        hint: Optional[Any] = None,
        path: Optional[Any] = None,
        sourceId: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            name=name,
            defaultValue=defaultValue,
            description=description,
            expression=expression,
            headerField=headerField,
            hint=hint,
            path=path,
            sourceId=sourceId,
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
        A structured set of tests against a FHIR server or client implementation to
        determine compliance against the FHIR specification.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        name: Descriptive name for this variable.

        defaultValue: A default, hard-coded, or user-defined value for this variable.

        description: A free text natural language description of the variable and its purpose.

        expression: The FHIRPath expression to evaluate against the fixture body. When variables
            are defined, only one of either expression, headerField or path must be
            specified.

        headerField: Will be used to grab the HTTP header field value from the headers that
            sourceId is pointing to.

        hint: Displayable text string with hint help information to the user when entering a
            default value.

        path: XPath or JSONPath to evaluate against the fixture body.  When variables are
            defined, only one of either expression, headerField or path must be specified.

        sourceId: Fixture to evaluate the XPath/JSONPath expression or the headerField  against
            within this variable.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("TestScript_Variable") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["TestScript_Variable"]
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
                # Descriptive name for this variable.
                StructField("name", StringType(), True),
                # A default, hard-coded, or user-defined value for this variable.
                StructField("defaultValue", StringType(), True),
                # A free text natural language description of the variable and its purpose.
                StructField("description", StringType(), True),
                # The FHIRPath expression to evaluate against the fixture body. When variables
                # are defined, only one of either expression, headerField or path must be
                # specified.
                StructField("expression", StringType(), True),
                # Will be used to grab the HTTP header field value from the headers that
                # sourceId is pointing to.
                StructField("headerField", StringType(), True),
                # Displayable text string with hint help information to the user when entering a
                # default value.
                StructField("hint", StringType(), True),
                # XPath or JSONPath to evaluate against the fixture body.  When variables are
                # defined, only one of either expression, headerField or path must be specified.
                StructField("path", StringType(), True),
                # Fixture to evaluate the XPath/JSONPath expression or the headerField  against
                # within this variable.
                StructField(
                    "sourceId",
                    idSchema.schema(
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