from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchCodeSystem_Concept(AutoMapperDataTypeComplexBase):
    """
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and optionally
    define a part or all of its content.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        code: Optional[Any] = None,
        display: Optional[Any] = None,
        definition: Optional[Any] = None,
        designation: Optional[Any] = None,
        property_: Optional[Any] = None,
        concept: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            display=display,
            definition=definition,
            designation=designation,
            property_=property_,
            concept=concept,
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
        The CodeSystem resource is used to declare the existence of and describe a
        code system or code system supplement and its key properties, and optionally
        define a part or all of its content.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        code: A code - a text symbol - that uniquely identifies the concept within the code
            system.

        display: A human readable string that is the recommended default way to present this
            concept to a user.

        definition: The formal definition of the concept. The code system resource does not make
            formal definitions required, because of the prevalence of legacy systems.
            However, they are highly recommended, as without them there is no formal
            meaning associated with the concept.

        designation: Additional representations for the concept - other languages, aliases,
            specialized purposes, used for particular purposes, etc.

        property: A property value for this concept.

        concept: Defines children of a concept to produce a hierarchy of concepts. The nature
            of the relationships is variable (is-a/contains/categorizes) - see
            hierarchyMeaning.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codesystem_designation import (
            AutoMapperElasticSearchCodeSystem_Designation as CodeSystem_DesignationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codesystem_property1 import (
            AutoMapperElasticSearchCodeSystem_Property1 as CodeSystem_Property1Schema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("CodeSystem_Concept") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["CodeSystem_Concept"]
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
                # A code - a text symbol - that uniquely identifies the concept within the code
                # system.
                StructField(
                    "code",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A human readable string that is the recommended default way to present this
                # concept to a user.
                StructField("display", StringType(), True),
                # The formal definition of the concept. The code system resource does not make
                # formal definitions required, because of the prevalence of legacy systems.
                # However, they are highly recommended, as without them there is no formal
                # meaning associated with the concept.
                StructField("definition", StringType(), True),
                # Additional representations for the concept - other languages, aliases,
                # specialized purposes, used for particular purposes, etc.
                StructField(
                    "designation",
                    ArrayType(
                        CodeSystem_DesignationSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # A property value for this concept.
                StructField(
                    "property",
                    ArrayType(
                        CodeSystem_Property1Schema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Defines children of a concept to produce a hierarchy of concepts. The nature
                # of the relationships is variable (is-a/contains/categorizes) - see
                # hierarchyMeaning.
                StructField(
                    "concept",
                    ArrayType(
                        CodeSystem_ConceptSchema.schema(
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
