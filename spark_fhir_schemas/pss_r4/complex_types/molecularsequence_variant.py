from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMolecularSequence_Variant(AutoMapperDataTypeComplexBase):
    """
    Raw data describing a biological sequence.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        start: Optional[Any] = None,
        end: Optional[Any] = None,
        observedAllele: Optional[Any] = None,
        referenceAllele: Optional[Any] = None,
        cigar: Optional[Any] = None,
        variantPointer: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            start=start,
            end=end,
            observedAllele=observedAllele,
            referenceAllele=referenceAllele,
            cigar=cigar,
            variantPointer=variantPointer,
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
        Raw data describing a biological sequence.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        start: Start position of the variant on the  reference sequence. If the coordinate
            system is either 0-based or 1-based, then start position is inclusive.

        end: End position of the variant on the reference sequence. If the coordinate
            system is 0-based then end is exclusive and does not include the last
            position. If the coordinate system is 1-base, then end is inclusive and
            includes the last position.

        observedAllele: An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
            23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
            Nucleotide(s)/amino acids from start position of sequence to stop position of
            sequence on the positive (+) strand of the observed  sequence. When the
            sequence  type is DNA, it should be the sequence on the positive (+) strand.
            This will lay in the range between variant.start and variant.end.

        referenceAllele: An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
            23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
            Nucleotide(s)/amino acids from start position of sequence to stop position of
            sequence on the positive (+) strand of the reference sequence. When the
            sequence  type is DNA, it should be the sequence on the positive (+) strand.
            This will lay in the range between variant.start and variant.end.

        cigar: Extended CIGAR string for aligning the sequence with reference bases. See
            detailed documentation [here](http://support.illumina.com/help/SequencingAnaly
            sisWorkflow/Content/Vault/Informatics/Sequencing_Analysis/CASAVA/swSEQ_mCA_Ext
            endedCIGARFormat.htm).

        variantPointer: A pointer to an Observation containing variant information.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MolecularSequence_Variant") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MolecularSequence_Variant"]
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
                # Start position of the variant on the  reference sequence. If the coordinate
                # system is either 0-based or 1-based, then start position is inclusive.
                StructField(
                    "start",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # End position of the variant on the reference sequence. If the coordinate
                # system is 0-based then end is exclusive and does not include the last
                # position. If the coordinate system is 1-base, then end is inclusive and
                # includes the last position.
                StructField(
                    "end",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
                # 23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
                # Nucleotide(s)/amino acids from start position of sequence to stop position of
                # sequence on the positive (+) strand of the observed  sequence. When the
                # sequence  type is DNA, it should be the sequence on the positive (+) strand.
                # This will lay in the range between variant.start and variant.end.
                StructField("observedAllele", StringType(), True),
                # An allele is one of a set of coexisting sequence variants of a gene ([SO:00010
                # 23](http://www.sequenceontology.org/browser/current_svn/term/SO:0001023)).
                # Nucleotide(s)/amino acids from start position of sequence to stop position of
                # sequence on the positive (+) strand of the reference sequence. When the
                # sequence  type is DNA, it should be the sequence on the positive (+) strand.
                # This will lay in the range between variant.start and variant.end.
                StructField("referenceAllele", StringType(), True),
                # Extended CIGAR string for aligning the sequence with reference bases. See
                # detailed documentation [here](http://support.illumina.com/help/SequencingAnaly
                # sisWorkflow/Content/Vault/Informatics/Sequencing_Analysis/CASAVA/swSEQ_mCA_Ext
                # endedCIGARFormat.htm).
                StructField("cigar", StringType(), True),
                # A pointer to an Observation containing variant information.
                StructField(
                    "variantPointer",
                    ReferenceSchema.schema(
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