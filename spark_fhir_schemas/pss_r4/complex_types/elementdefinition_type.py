from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchElementDefinition_Type(AutoMapperDataTypeComplexBase):
    """
    Captures constraints on each element within the resource, profile, or
    extension.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        code: Optional[Any] = None,
        profile: Optional[Any] = None,
        targetProfile: Optional[Any] = None,
        aggregation: Optional[Any] = None,
        versioning: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            profile=profile,
            targetProfile=targetProfile,
            aggregation=aggregation,
            versioning=versioning,
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
        Captures constraints on each element within the resource, profile, or
        extension.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        code: URL of Data type or Resource that is a(or the) type used for this element.
            References are URLs that are relative to
            http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference to
            http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed
            in logical models.

        profile: Identifies a profile structure or implementation Guide that applies to the
            datatype this element refers to. If any profiles are specified, then the
            content must conform to at least one of them. The URL can be a local reference
            - to a contained StructureDefinition, or a reference to another
            StructureDefinition or Implementation Guide by a canonical URL. When an
            implementation guide is specified, the type SHALL conform to at least one
            profile defined in the implementation guide.

        targetProfile: Used when the type is "Reference" or "canonical", and identifies a profile
            structure or implementation Guide that applies to the target of the reference
            this element refers to. If any profiles are specified, then the content must
            conform to at least one of them. The URL can be a local reference - to a
            contained StructureDefinition, or a reference to another StructureDefinition
            or Implementation Guide by a canonical URL. When an implementation guide is
            specified, the target resource SHALL conform to at least one profile defined
            in the implementation guide.

        aggregation: If the type is a reference to another resource, how the resource is or can be
            aggregated - is it a contained resource, or a reference, and if the context is
            a bundle, is it included in the bundle.

        versioning: Whether this reference needs to be version specific or version independent, or
            whether either can be used.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.canonical import (
            AutoMapperElasticSearchcanonical as canonicalSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ElementDefinition_Type") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ElementDefinition_Type"]
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
                # URL of Data type or Resource that is a(or the) type used for this element.
                # References are URLs that are relative to
                # http://hl7.org/fhir/StructureDefinition e.g. "string" is a reference to
                # http://hl7.org/fhir/StructureDefinition/string. Absolute URLs are only allowed
                # in logical models.
                StructField(
                    "code",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies a profile structure or implementation Guide that applies to the
                # datatype this element refers to. If any profiles are specified, then the
                # content must conform to at least one of them. The URL can be a local reference
                # - to a contained StructureDefinition, or a reference to another
                # StructureDefinition or Implementation Guide by a canonical URL. When an
                # implementation guide is specified, the type SHALL conform to at least one
                # profile defined in the implementation guide.
                StructField(
                    "profile",
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
                # Used when the type is "Reference" or "canonical", and identifies a profile
                # structure or implementation Guide that applies to the target of the reference
                # this element refers to. If any profiles are specified, then the content must
                # conform to at least one of them. The URL can be a local reference - to a
                # contained StructureDefinition, or a reference to another StructureDefinition
                # or Implementation Guide by a canonical URL. When an implementation guide is
                # specified, the target resource SHALL conform to at least one profile defined
                # in the implementation guide.
                StructField(
                    "targetProfile",
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
                # If the type is a reference to another resource, how the resource is or can be
                # aggregated - is it a contained resource, or a reference, and if the context is
                # a bundle, is it included in the bundle.
                # Whether this reference needs to be version specific or version independent, or
                # whether either can be used.
                StructField("versioning", StringType(), True),
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