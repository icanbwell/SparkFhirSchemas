from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceSourceMaterial(AutoMapperDataTypeComplexBase):
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
        resourceType: Optional[Any] = None,
        id_: Optional[Any] = None,
        meta: Optional[Any] = None,
        implicitRules: Optional[Any] = None,
        language: Optional[Any] = None,
        text: Optional[Any] = None,
        contained: Optional[Any] = None,
        extension: Optional[Any] = None,
        sourceMaterialClass: Optional[Any] = None,
        sourceMaterialType: Optional[Any] = None,
        sourceMaterialState: Optional[Any] = None,
        organismId: Optional[Any] = None,
        organismName: Optional[Any] = None,
        parentSubstanceId: Optional[Any] = None,
        parentSubstanceName: Optional[Any] = None,
        countryOfOrigin: Optional[Any] = None,
        geographicalLocation: Optional[Any] = None,
        developmentStage: Optional[Any] = None,
        fractionDescription: Optional[Any] = None,
        organism: Optional[Any] = None,
        partDescription: Optional[Any] = None,
    ) -> None:
        super().__init__(
            resourceType=resourceType,
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            sourceMaterialClass=sourceMaterialClass,
            sourceMaterialType=sourceMaterialType,
            sourceMaterialState=sourceMaterialState,
            organismId=organismId,
            organismName=organismName,
            parentSubstanceId=parentSubstanceId,
            parentSubstanceName=parentSubstanceName,
            countryOfOrigin=countryOfOrigin,
            geographicalLocation=geographicalLocation,
            developmentStage=developmentStage,
            fractionDescription=fractionDescription,
            organism=organism,
            partDescription=partDescription,
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


        resourceType: This is a SubstanceSourceMaterial resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        sourceMaterialClass: General high level classification of the source material specific to the
            origin of the material.

        sourceMaterialType: The type of the source material shall be specified based on a controlled
            vocabulary. For vaccines, this subclause refers to the class of infectious
            agent.

        sourceMaterialState: The state of the source material when extracted.

        organismId: The unique identifier associated with the source material parent organism
            shall be specified.

        organismName: The organism accepted Scientific name shall be provided based on the organism
            taxonomy.

        parentSubstanceId: The parent of the herbal drug Ginkgo biloba, Leaf is the substance ID of the
            substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L. (Whole plant).

        parentSubstanceName: The parent substance of the Herbal Drug, or Herbal preparation.

        countryOfOrigin: The country where the plant material is harvested or the countries where the
            plasma is sourced from as laid down in accordance with the Plasma Master File.
            For “Plasma-derived substances” the attribute country of origin provides
            information about the countries used for the manufacturing of the Cryopoor
            plama or Crioprecipitate.

        geographicalLocation: The place/region where the plant is harvested or the places/regions where the
            animal source material has its habitat.

        developmentStage: Stage of life for animals, plants, insects and microorganisms. This
            information shall be provided only when the substance is significantly
            different in these stages (e.g. foetal bovine serum).

        fractionDescription: Many complex materials are fractions of parts of plants, animals, or minerals.
            Fraction elements are often necessary to define both Substances and Specified
            Group 1 Substances. For substances derived from Plants, fraction information
            will be captured at the Substance information level ( . Oils, Juices and
            Exudates). Additional information for Extracts, such as extraction solvent
            composition, will be captured at the Specified Substance Group 1 information
            level. For plasma-derived products fraction information will be captured at
            the Substance and the Specified Substance Group 1 levels.

        organism: This subclause describes the organism which the substance is derived from. For
            vaccines, the parent organism shall be specified based on these subclause
            elements. As an example, full taxonomy will be described for the Substance
            Name: ., Leaf.

        partDescription: To do.

        """
        from spark_fhir_schemas.pss_r4.simple_types.id import (
            AutoMapperElasticSearchid as idSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.meta import (
            AutoMapperElasticSearchMeta as MetaSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.code import (
            AutoMapperElasticSearchcode as codeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.narrative import (
            AutoMapperElasticSearchNarrative as NarrativeSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.resourcelist import (
            AutoMapperElasticSearchResourceList as ResourceListSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancesourcematerial_fractiondescription import (
            AutoMapperElasticSearchSubstanceSourceMaterial_FractionDescription as SubstanceSourceMaterial_FractionDescriptionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancesourcematerial_organism import (
            AutoMapperElasticSearchSubstanceSourceMaterial_Organism as SubstanceSourceMaterial_OrganismSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancesourcematerial_partdescription import (
            AutoMapperElasticSearchSubstanceSourceMaterial_PartDescription as SubstanceSourceMaterial_PartDescriptionSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceSourceMaterial") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SubstanceSourceMaterial"]
        schema = StructType(
            [
                # This is a SubstanceSourceMaterial resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField(
                    "id",
                    idSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta",
                    MetaSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The base language in which the resource is written.
                StructField(
                    "language",
                    codeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text",
                    NarrativeSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(
                        ResourceListSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
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
                # General high level classification of the source material specific to the
                # origin of the material.
                StructField(
                    "sourceMaterialClass",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The type of the source material shall be specified based on a controlled
                # vocabulary. For vaccines, this subclause refers to the class of infectious
                # agent.
                StructField(
                    "sourceMaterialType",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The state of the source material when extracted.
                StructField(
                    "sourceMaterialState",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The unique identifier associated with the source material parent organism
                # shall be specified.
                StructField(
                    "organismId",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The organism accepted Scientific name shall be provided based on the organism
                # taxonomy.
                StructField("organismName", StringType(), True),
                # The parent of the herbal drug Ginkgo biloba, Leaf is the substance ID of the
                # substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L. (Whole plant).
                StructField(
                    "parentSubstanceId",
                    ArrayType(
                        IdentifierSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The parent substance of the Herbal Drug, or Herbal preparation.
                StructField("parentSubstanceName", ArrayType(StringType()), True),
                # The country where the plant material is harvested or the countries where the
                # plasma is sourced from as laid down in accordance with the Plasma Master File.
                # For “Plasma-derived substances” the attribute country of origin provides
                # information about the countries used for the manufacturing of the Cryopoor
                # plama or Crioprecipitate.
                StructField(
                    "countryOfOrigin",
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
                # The place/region where the plant is harvested or the places/regions where the
                # animal source material has its habitat.
                StructField("geographicalLocation", ArrayType(StringType()), True),
                # Stage of life for animals, plants, insects and microorganisms. This
                # information shall be provided only when the substance is significantly
                # different in these stages (e.g. foetal bovine serum).
                StructField(
                    "developmentStage",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Many complex materials are fractions of parts of plants, animals, or minerals.
                # Fraction elements are often necessary to define both Substances and Specified
                # Group 1 Substances. For substances derived from Plants, fraction information
                # will be captured at the Substance information level ( . Oils, Juices and
                # Exudates). Additional information for Extracts, such as extraction solvent
                # composition, will be captured at the Specified Substance Group 1 information
                # level. For plasma-derived products fraction information will be captured at
                # the Substance and the Specified Substance Group 1 levels.
                StructField(
                    "fractionDescription",
                    ArrayType(
                        SubstanceSourceMaterial_FractionDescriptionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # This subclause describes the organism which the substance is derived from. For
                # vaccines, the parent organism shall be specified based on these subclause
                # elements. As an example, full taxonomy will be described for the Substance
                # Name: ., Leaf.
                StructField(
                    "organism",
                    SubstanceSourceMaterial_OrganismSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # To do.
                StructField(
                    "partDescription",
                    ArrayType(
                        SubstanceSourceMaterial_PartDescriptionSchema.schema(
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