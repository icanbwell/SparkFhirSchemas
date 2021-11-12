from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceSpecification_Structure(
    AutoMapperDataTypeComplexBase
):
    """
    The detailed description of a substance, typically at a level beyond what is
    used for prescribing.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        stereochemistry: Optional[Any] = None,
        opticalActivity: Optional[Any] = None,
        molecularFormula: Optional[Any] = None,
        molecularFormulaByMoiety: Optional[Any] = None,
        isotope: Optional[Any] = None,
        molecularWeight: Optional[Any] = None,
        source: Optional[Any] = None,
        representation: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            stereochemistry=stereochemistry,
            opticalActivity=opticalActivity,
            molecularFormula=molecularFormula,
            molecularFormulaByMoiety=molecularFormulaByMoiety,
            isotope=isotope,
            molecularWeight=molecularWeight,
            source=source,
            representation=representation,
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
        The detailed description of a substance, typically at a level beyond what is
        used for prescribing.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        stereochemistry: Stereochemistry type.

        opticalActivity: Optical activity type.

        molecularFormula: Molecular formula.

        molecularFormulaByMoiety: Specified per moiety according to the Hill system, i.e. first C, then H, then
            alphabetical, each moiety separated by a dot.

        isotope: Applicable for single substances that contain a radionuclide or a non-natural
            isotopic ratio.

        molecularWeight: The molecular weight or weight range (for proteins, polymers or nucleic
            acids).

        source: Supporting literature.

        representation: Molecular structural representation.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancespecification_isotope import (
            AutoMapperElasticSearchSubstanceSpecification_Isotope as SubstanceSpecification_IsotopeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancespecification_molecularweight import (
            AutoMapperElasticSearchSubstanceSpecification_MolecularWeight as SubstanceSpecification_MolecularWeightSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancespecification_representation import (
            AutoMapperElasticSearchSubstanceSpecification_Representation as SubstanceSpecification_RepresentationSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceSpecification_Structure")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SubstanceSpecification_Structure"]
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
                # Stereochemistry type.
                StructField(
                    "stereochemistry",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Optical activity type.
                StructField(
                    "opticalActivity",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Molecular formula.
                StructField("molecularFormula", StringType(), True),
                # Specified per moiety according to the Hill system, i.e. first C, then H, then
                # alphabetical, each moiety separated by a dot.
                StructField("molecularFormulaByMoiety", StringType(), True),
                # Applicable for single substances that contain a radionuclide or a non-natural
                # isotopic ratio.
                StructField(
                    "isotope",
                    ArrayType(
                        SubstanceSpecification_IsotopeSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The molecular weight or weight range (for proteins, polymers or nucleic
                # acids).
                StructField(
                    "molecularWeight",
                    SubstanceSpecification_MolecularWeightSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Supporting literature.
                StructField(
                    "source",
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Molecular structural representation.
                StructField(
                    "representation",
                    ArrayType(
                        SubstanceSpecification_RepresentationSchema.schema(
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
