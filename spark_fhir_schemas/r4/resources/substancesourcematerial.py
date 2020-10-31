from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class SubstanceSourceMaterial:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_fractiondescription import SubstanceSourceMaterial_FractionDescription
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_organism import SubstanceSourceMaterial_Organism
        from spark_fhir_schemas.r4.complex_types.substancesourcematerial_partdescription import SubstanceSourceMaterial_PartDescription
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a SubstanceSourceMaterial resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # General high level classification of the source material specific to the
                # origin of the material.
                StructField(
                    "sourceMaterialClass",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The type of the source material shall be specified based on a controlled
                # vocabulary. For vaccines, this subclause refers to the class of infectious
                # agent.
                StructField(
                    "sourceMaterialType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The state of the source material when extracted.
                StructField(
                    "sourceMaterialState",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The unique identifier associated with the source material parent organism
                # shall be specified.
                StructField(
                    "organismId", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                # The organism accepted Scientific name shall be provided based on the organism
                # taxonomy.
                StructField("organismName", StringType(), True),
                # The parent of the herbal drug Ginkgo biloba, Leaf is the substance ID of the
                # substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L. (Whole plant).
                StructField(
                    "parentSubstanceId",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The parent substance of the Herbal Drug, or Herbal preparation.
                StructField(
                    "parentSubstanceName", ArrayType(StringType()), True
                ),
                # The country where the plant material is harvested or the countries where the
                # plasma is sourced from as laid down in accordance with the Plasma Master File.
                # For “Plasma-derived substances” the attribute country of origin provides
                # information about the countries used for the manufacturing of the Cryopoor
                # plama or Crioprecipitate.
                StructField(
                    "countryOfOrigin",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The place/region where the plant is harvested or the places/regions where the
                # animal source material has its habitat.
                StructField(
                    "geographicalLocation", ArrayType(StringType()), True
                ),
                # Stage of life for animals, plants, insects and microorganisms. This
                # information shall be provided only when the substance is significantly
                # different in these stages (e.g. foetal bovine serum).
                StructField(
                    "developmentStage",
                    CodeableConcept.get_schema(recursion_depth + 1), True
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
                        SubstanceSourceMaterial_FractionDescription.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # This subclause describes the organism which the substance is derived from. For
                # vaccines, the parent organism shall be specified based on these subclause
                # elements. As an example, full taxonomy will be described for the Substance
                # Name: ., Leaf.
                StructField(
                    "organism",
                    SubstanceSourceMaterial_Organism.
                    get_schema(recursion_depth + 1), True
                ),
                # To do.
                StructField(
                    "partDescription",
                    ArrayType(
                        SubstanceSourceMaterial_PartDescription.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
