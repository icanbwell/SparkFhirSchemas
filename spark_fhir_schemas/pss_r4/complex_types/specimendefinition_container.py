from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSpecimenDefinition_Container(
    AutoMapperDataTypeComplexBase
):
    """
    A kind of specimen with associated set of requirements.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        material: Optional[Any] = None,
        type_: Optional[Any] = None,
        cap: Optional[Any] = None,
        description: Optional[Any] = None,
        capacity: Optional[Any] = None,
        minimumVolumeQuantity: Optional[Any] = None,
        minimumVolumeString: Optional[Any] = None,
        additive: Optional[Any] = None,
        preparation: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            material=material,
            type_=type_,
            cap=cap,
            description=description,
            capacity=capacity,
            minimumVolumeQuantity=minimumVolumeQuantity,
            minimumVolumeString=minimumVolumeString,
            additive=additive,
            preparation=preparation,
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
        A kind of specimen with associated set of requirements.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        material: The type of material of the container.

        type: The type of container used to contain this kind of specimen.

        cap: Color of container cap.

        description: The textual description of the kind of container.

        capacity: The capacity (volume or other measure) of this kind of container.

        minimumVolumeQuantity: The minimum volume to be conditioned in the container.

        minimumVolumeString: The minimum volume to be conditioned in the container.

        additive: Substance introduced in the kind of container to preserve, maintain or enhance
            the specimen. Examples: Formalin, Citrate, EDTA.

        preparation: Special processing that should be applied to the container for this kind of
            specimen.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.specimendefinition_additive import (
            AutoMapperElasticSearchSpecimenDefinition_Additive as SpecimenDefinition_AdditiveSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SpecimenDefinition_Container")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SpecimenDefinition_Container"]
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
                # The type of material of the container.
                StructField(
                    "material",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The type of container used to contain this kind of specimen.
                StructField(
                    "type",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Color of container cap.
                StructField(
                    "cap",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The textual description of the kind of container.
                StructField("description", StringType(), True),
                # The capacity (volume or other measure) of this kind of container.
                StructField(
                    "capacity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The minimum volume to be conditioned in the container.
                StructField(
                    "minimumVolumeQuantity",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The minimum volume to be conditioned in the container.
                StructField("minimumVolumeString", StringType(), True),
                # Substance introduced in the kind of container to preserve, maintain or enhance
                # the specimen. Examples: Formalin, Citrate, EDTA.
                StructField(
                    "additive",
                    ArrayType(
                        SpecimenDefinition_AdditiveSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Special processing that should be applied to the container for this kind of
                # specimen.
                StructField("preparation", StringType(), True),
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
