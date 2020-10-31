from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Raw data describing a biological sequence.


        resourceType: This is a MolecularSequence resource

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

        identifier: A unique identifier for this particular sequence instance. This is a FHIR-
            defined id.

        type: Amino Acid Sequence/ DNA Sequence / RNA Sequence.

        coordinateSystem: Whether the sequence is numbered starting at 0 (0-based numbering or
            coordinates, inclusive start, exclusive end) or starting at 1 (1-based
            numbering, inclusive start and inclusive end).

        patient: The patient whose sequencing results are described by this resource.

        specimen: Specimen used for sequencing.

        device: The method for sequencing, for example, chip information.

        performer: The organization or lab that should be responsible for this result.

        quantity: The number of copies of the sequence of interest. (RNASeq).

        referenceSeq: A sequence that is used as a reference to describe variants that are present
            in a sequence analyzed.

        variant: The definition of variant here originates from Sequence ontology ([variant_of]
            (http://www.sequenceontology.org/browser/current_svn/term/variant_of)). This
            element can represent amino acid or nucleic sequence change(including
            insertion,deletion,SNP,etc.)  It can represent some complex mutation or
            segment variation with the assist of CIGAR string.

        observedSeq: Sequence that was observed. It is the result marked by referenceSeq along with
            variant records on referenceSeq. This shall start from
            referenceSeq.windowStart and end by referenceSeq.windowEnd.

        quality: An experimental feature attribute that defines the quality of the feature in a
            quantitative way, such as a phred quality score ([SO:0001686](http://www.seque
            nceontology.org/browser/current_svn/term/SO:0001686)).

        readCoverage: Coverage (read depth or depth) is the average number of reads representing a
            given nucleotide in the reconstructed sequence.

        repository: Configurations of the external repository. The repository shall store target's
            observedSeq or records related with target's observedSeq.

        pointer: Pointer to next atomic sequence which at most contains one variant.

        structureVariant: Information about chromosome structure variation.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.molecularsequence_referenceseq import MolecularSequence_ReferenceSeq
        from spark_fhir_schemas.r4.complex_types.molecularsequence_variant import MolecularSequence_Variant
        from spark_fhir_schemas.r4.complex_types.molecularsequence_quality import MolecularSequence_Quality
        from spark_fhir_schemas.r4.complex_types.molecularsequence_repository import MolecularSequence_Repository
        from spark_fhir_schemas.r4.complex_types.molecularsequence_structurevariant import MolecularSequence_StructureVariant
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a MolecularSequence resource
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
                # A unique identifier for this particular sequence instance. This is a FHIR-
                # defined id.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # Amino Acid Sequence/ DNA Sequence / RNA Sequence.
                StructField("type", StringType(), True),
                # Whether the sequence is numbered starting at 0 (0-based numbering or
                # coordinates, inclusive start, exclusive end) or starting at 1 (1-based
                # numbering, inclusive start and inclusive end).
                StructField(
                    "coordinateSystem",
                    integer.get_schema(recursion_depth + 1), True
                ),
                # The patient whose sequencing results are described by this resource.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # Specimen used for sequencing.
                StructField(
                    "specimen", Reference.get_schema(recursion_depth + 1), True
                ),
                # The method for sequencing, for example, chip information.
                StructField(
                    "device", Reference.get_schema(recursion_depth + 1), True
                ),
                # The organization or lab that should be responsible for this result.
                StructField(
                    "performer", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The number of copies of the sequence of interest. (RNASeq).
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                # A sequence that is used as a reference to describe variants that are present
                # in a sequence analyzed.
                StructField(
                    "referenceSeq",
                    MolecularSequence_ReferenceSeq.
                    get_schema(recursion_depth + 1), True
                ),
                # The definition of variant here originates from Sequence ontology ([variant_of]
                # (http://www.sequenceontology.org/browser/current_svn/term/variant_of)). This
                # element can represent amino acid or nucleic sequence change(including
                # insertion,deletion,SNP,etc.)  It can represent some complex mutation or
                # segment variation with the assist of CIGAR string.
                StructField(
                    "variant",
                    ArrayType(
                        MolecularSequence_Variant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Sequence that was observed. It is the result marked by referenceSeq along with
                # variant records on referenceSeq. This shall start from
                # referenceSeq.windowStart and end by referenceSeq.windowEnd.
                StructField("observedSeq", StringType(), True),
                # An experimental feature attribute that defines the quality of the feature in a
                # quantitative way, such as a phred quality score ([SO:0001686](http://www.seque
                # nceontology.org/browser/current_svn/term/SO:0001686)).
                StructField(
                    "quality",
                    ArrayType(
                        MolecularSequence_Quality.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Coverage (read depth or depth) is the average number of reads representing a
                # given nucleotide in the reconstructed sequence.
                StructField(
                    "readCoverage", integer.get_schema(recursion_depth + 1),
                    True
                ),
                # Configurations of the external repository. The repository shall store target's
                # observedSeq or records related with target's observedSeq.
                StructField(
                    "repository",
                    ArrayType(
                        MolecularSequence_Repository.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Pointer to next atomic sequence which at most contains one variant.
                StructField(
                    "pointer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Information about chromosome structure variation.
                StructField(
                    "structureVariant",
                    ArrayType(
                        MolecularSequence_StructureVariant.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
