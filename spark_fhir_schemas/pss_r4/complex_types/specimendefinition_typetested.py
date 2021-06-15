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
class AutoMapperElasticSearchSpecimenDefinition_TypeTested(
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
        isDerived: Optional[Any] = None,
        type_: Optional[Any] = None,
        preference: Optional[Any] = None,
        container: Optional[Any] = None,
        requirement: Optional[Any] = None,
        retentionTime: Optional[Any] = None,
        rejectionCriterion: Optional[Any] = None,
        handling: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            isDerived=isDerived,
            type_=type_,
            preference=preference,
            container=container,
            requirement=requirement,
            retentionTime=retentionTime,
            rejectionCriterion=rejectionCriterion,
            handling=handling,
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

        isDerived: Primary of secondary specimen.

        type: The kind of specimen conditioned for testing expected by lab.

        preference: The preference for this type of conditioned specimen.

        container: The specimen's container.

        requirement: Requirements for delivery and special handling of this kind of conditioned
            specimen.

        retentionTime: The usual time that a specimen of this kind is retained after the ordered
            tests are completed, for the purpose of additional testing.

        rejectionCriterion: Criterion for rejection of the specimen in its container by the laboratory.

        handling: Set of instructions for preservation/transport of the specimen at a defined
            temperature interval, prior the testing process.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.specimendefinition_container import (
            AutoMapperElasticSearchSpecimenDefinition_Container as SpecimenDefinition_ContainerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.specimendefinition_handling import (
            AutoMapperElasticSearchSpecimenDefinition_Handling as SpecimenDefinition_HandlingSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SpecimenDefinition_TypeTested")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SpecimenDefinition_TypeTested"]
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
                # Primary of secondary specimen.
                StructField("isDerived", BooleanType(), True),
                # The kind of specimen conditioned for testing expected by lab.
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
                # The preference for this type of conditioned specimen.
                StructField("preference", StringType(), True),
                # The specimen's container.
                StructField(
                    "container",
                    SpecimenDefinition_ContainerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Requirements for delivery and special handling of this kind of conditioned
                # specimen.
                StructField("requirement", StringType(), True),
                # The usual time that a specimen of this kind is retained after the ordered
                # tests are completed, for the purpose of additional testing.
                StructField(
                    "retentionTime",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Criterion for rejection of the specimen in its container by the laboratory.
                StructField(
                    "rejectionCriterion",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Set of instructions for preservation/transport of the specimen at a defined
                # temperature interval, prior the testing process.
                StructField(
                    "handling",
                    ArrayType(
                        SpecimenDefinition_HandlingSchema.schema(
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
