from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceSourceMaterial_Organism(
    AutoMapperDataTypeComplexBase
):
    """
    Source material shall capture information on the taxonomic and anatomical
    origins as well as the fraction of a material that can result in or can be
    modified to form a substance. This set of data elements shall be used to
    define polymer substances isolated from biological matrices. Taxonomic and
    anatomical origins shall be described using a controlled vocabulary as
    required. This information is captured for naturally derived polymers ( .
    starch) and structurally diverse substances. For Organisms belonging to the
    Kingdom Plantae the Substance level defines the fresh material of a single
    species or infraspecies, the Herbal Drug and the Herbal preparation. For
    Herbal preparations, the fraction information will be captured at the
    Substance information level and additional information for herbal extracts
    will be captured at the Specified Substance Group 1 information level. See for
    further explanation the Substance Class: Structurally Diverse and the herbal
    annex.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        family: Optional[Any] = None,
        genus: Optional[Any] = None,
        species: Optional[Any] = None,
        intraspecificType: Optional[Any] = None,
        intraspecificDescription: Optional[Any] = None,
        author: Optional[Any] = None,
        hybrid: Optional[Any] = None,
        organismGeneral: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            family=family,
            genus=genus,
            species=species,
            intraspecificType=intraspecificType,
            intraspecificDescription=intraspecificDescription,
            author=author,
            hybrid=hybrid,
            organismGeneral=organismGeneral,
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
        Source material shall capture information on the taxonomic and anatomical
        origins as well as the fraction of a material that can result in or can be
        modified to form a substance. This set of data elements shall be used to
        define polymer substances isolated from biological matrices. Taxonomic and
        anatomical origins shall be described using a controlled vocabulary as
        required. This information is captured for naturally derived polymers ( .
        starch) and structurally diverse substances. For Organisms belonging to the
        Kingdom Plantae the Substance level defines the fresh material of a single
        species or infraspecies, the Herbal Drug and the Herbal preparation. For
        Herbal preparations, the fraction information will be captured at the
        Substance information level and additional information for herbal extracts
        will be captured at the Specified Substance Group 1 information level. See for
        further explanation the Substance Class: Structurally Diverse and the herbal
        annex.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        family: The family of an organism shall be specified.

        genus: The genus of an organism shall be specified; refers to the Latin epithet of
            the genus element of the plant/animal scientific name; it is present in names
            for genera, species and infraspecies.

        species: The species of an organism shall be specified; refers to the Latin epithet of
            the species of the plant/animal; it is present in names for species and
            infraspecies.

        intraspecificType: The Intraspecific type of an organism shall be specified.

        intraspecificDescription: The intraspecific description of an organism shall be specified based on a
            controlled vocabulary. For Influenza Vaccine, the intraspecific description
            shall contain the syntax of the antigen in line with the WHO convention.

        author: 4.9.13.6.1 Author type (Conditional).

        hybrid: 4.9.13.8.1 Hybrid species maternal organism ID (Optional).

        organismGeneral: 4.9.13.7.1 Kingdom (Conditional).

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancesourcematerial_author import (
            AutoMapperElasticSearchSubstanceSourceMaterial_Author as SubstanceSourceMaterial_AuthorSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancesourcematerial_hybrid import (
            AutoMapperElasticSearchSubstanceSourceMaterial_Hybrid as SubstanceSourceMaterial_HybridSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancesourcematerial_organismgeneral import (
            AutoMapperElasticSearchSubstanceSourceMaterial_OrganismGeneral as SubstanceSourceMaterial_OrganismGeneralSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceSourceMaterial_Organism")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SubstanceSourceMaterial_Organism"]
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
                # The family of an organism shall be specified.
                StructField(
                    "family",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The genus of an organism shall be specified; refers to the Latin epithet of
                # the genus element of the plant/animal scientific name; it is present in names
                # for genera, species and infraspecies.
                StructField(
                    "genus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The species of an organism shall be specified; refers to the Latin epithet of
                # the species of the plant/animal; it is present in names for species and
                # infraspecies.
                StructField(
                    "species",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The Intraspecific type of an organism shall be specified.
                StructField(
                    "intraspecificType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The intraspecific description of an organism shall be specified based on a
                # controlled vocabulary. For Influenza Vaccine, the intraspecific description
                # shall contain the syntax of the antigen in line with the WHO convention.
                StructField("intraspecificDescription", StringType(), True),
                # 4.9.13.6.1 Author type (Conditional).
                StructField(
                    "author",
                    ArrayType(
                        SubstanceSourceMaterial_AuthorSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
                StructField(
                    "hybrid",
                    SubstanceSourceMaterial_HybridSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # 4.9.13.7.1 Kingdom (Conditional).
                StructField(
                    "organismGeneral",
                    SubstanceSourceMaterial_OrganismGeneralSchema.schema(
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