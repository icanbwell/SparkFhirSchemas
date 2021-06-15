from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchImplementationGuide_Resource(
    AutoMapperDataTypeComplexBase
):
    """
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used to
    gather all the parts of an implementation guide into a logical whole and to
    publish a computable definition of all the parts.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        reference: Optional[Any] = None,
        fhirVersion: Optional[Any] = None,
        name: Optional[Any] = None,
        description: Optional[Any] = None,
        exampleBoolean: Optional[Any] = None,
        exampleCanonical: Optional[Any] = None,
        groupingId: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            reference=reference,
            fhirVersion=fhirVersion,
            name=name,
            description=description,
            exampleBoolean=exampleBoolean,
            exampleCanonical=exampleCanonical,
            groupingId=groupingId,
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
        A set of rules of how a particular interoperability or standards problem is
        solved - typically through the use of FHIR resources. This resource is used to
        gather all the parts of an implementation guide into a logical whole and to
        publish a computable definition of all the parts.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        reference: Where this resource is found.

        fhirVersion: Indicates the FHIR Version(s) this artifact is intended to apply to. If no
            versions are specified, the resource is assumed to apply to all the versions
            stated in ImplementationGuide.fhirVersion.

        name: A human assigned name for the resource. All resources SHOULD have a name, but
            the name may be extracted from the resource (e.g. ValueSet.name).

        description: A description of the reason that a resource has been included in the
            implementation guide.

        exampleBoolean: If true or a reference, indicates the resource is an example instance.  If a
            reference is present, indicates that the example is an example of the
            specified profile.

        exampleCanonical: If true or a reference, indicates the resource is an example instance.  If a
            reference is present, indicates that the example is an example of the
            specified profile.

        groupingId: Reference to the id of the grouping this resource appears in.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ImplementationGuide_Resource")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["ImplementationGuide_Resource"]
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
                # Where this resource is found.
                StructField(
                    "reference",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates the FHIR Version(s) this artifact is intended to apply to. If no
                # versions are specified, the resource is assumed to apply to all the versions
                # stated in ImplementationGuide.fhirVersion.
                # A human assigned name for the resource. All resources SHOULD have a name, but
                # the name may be extracted from the resource (e.g. ValueSet.name).
                StructField("name", StringType(), True),
                # A description of the reason that a resource has been included in the
                # implementation guide.
                StructField("description", StringType(), True),
                # If true or a reference, indicates the resource is an example instance.  If a
                # reference is present, indicates that the example is an example of the
                # specified profile.
                StructField("exampleBoolean", BooleanType(), True),
                # If true or a reference, indicates the resource is an example instance.  If a
                # reference is present, indicates that the example is an example of the
                # specified profile.
                StructField("exampleCanonical", StringType(), True),
                # Reference to the id of the grouping this resource appears in.
                StructField(
                    "groupingId",
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
