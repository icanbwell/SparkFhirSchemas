from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceNucleicAcid_Subunit(
    AutoMapperDataTypeComplexBase
):
    """
    Nucleic acids are defined by three distinct elements: the base, sugar and
    linkage. Individual substance/moiety IDs will be created for each of these
    elements. The nucleotide sequence will be always entered in the 5’-3’
    direction.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        subunit: Optional[Any] = None,
        sequence: Optional[Any] = None,
        length: Optional[Any] = None,
        sequenceAttachment: Optional[Any] = None,
        fivePrime: Optional[Any] = None,
        threePrime: Optional[Any] = None,
        linkage: Optional[Any] = None,
        sugar: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            subunit=subunit,
            sequence=sequence,
            length=length,
            sequenceAttachment=sequenceAttachment,
            fivePrime=fivePrime,
            threePrime=threePrime,
            linkage=linkage,
            sugar=sugar,
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
        Nucleic acids are defined by three distinct elements: the base, sugar and
        linkage. Individual substance/moiety IDs will be created for each of these
        elements. The nucleotide sequence will be always entered in the 5’-3’
        direction.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        subunit: Index of linear sequences of nucleic acids in order of decreasing length.
            Sequences of the same length will be ordered by molecular weight. Subunits
            that have identical sequences will be repeated and have sequential subscripts.

        sequence: Actual nucleotide sequence notation from 5' to 3' end using standard single
            letter codes. In addition to the base sequence, sugar and type of phosphate or
            non-phosphate linkage should also be captured.

        length: The length of the sequence shall be captured.

        sequenceAttachment: (TBC).

        fivePrime: The nucleotide present at the 5’ terminal shall be specified based on a
            controlled vocabulary. Since the sequence is represented from the 5' to the 3'
            end, the 5’ prime nucleotide is the letter at the first position in the
            sequence. A separate representation would be redundant.

        threePrime: The nucleotide present at the 3’ terminal shall be specified based on a
            controlled vocabulary. Since the sequence is represented from the 5' to the 3'
            end, the 5’ prime nucleotide is the letter at the last position in the
            sequence. A separate representation would be redundant.

        linkage: The linkages between sugar residues will also be captured.

        sugar: 5.3.6.8.1 Sugar ID (Mandatory).

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.attachment import (
            AutoMapperElasticSearchAttachment as AttachmentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancenucleicacid_linkage import (
            AutoMapperElasticSearchSubstanceNucleicAcid_Linkage as SubstanceNucleicAcid_LinkageSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.substancenucleicacid_sugar import (
            AutoMapperElasticSearchSubstanceNucleicAcid_Sugar as SubstanceNucleicAcid_SugarSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceNucleicAcid_Subunit")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SubstanceNucleicAcid_Subunit"]
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
                # Index of linear sequences of nucleic acids in order of decreasing length.
                # Sequences of the same length will be ordered by molecular weight. Subunits
                # that have identical sequences will be repeated and have sequential subscripts.
                StructField(
                    "subunit",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Actual nucleotide sequence notation from 5' to 3' end using standard single
                # letter codes. In addition to the base sequence, sugar and type of phosphate or
                # non-phosphate linkage should also be captured.
                StructField("sequence", StringType(), True),
                # The length of the sequence shall be captured.
                StructField(
                    "length",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # (TBC).
                StructField(
                    "sequenceAttachment",
                    AttachmentSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The nucleotide present at the 5’ terminal shall be specified based on a
                # controlled vocabulary. Since the sequence is represented from the 5' to the 3'
                # end, the 5’ prime nucleotide is the letter at the first position in the
                # sequence. A separate representation would be redundant.
                StructField(
                    "fivePrime",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The nucleotide present at the 3’ terminal shall be specified based on a
                # controlled vocabulary. Since the sequence is represented from the 5' to the 3'
                # end, the 5’ prime nucleotide is the letter at the last position in the
                # sequence. A separate representation would be redundant.
                StructField(
                    "threePrime",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The linkages between sugar residues will also be captured.
                StructField(
                    "linkage",
                    ArrayType(
                        SubstanceNucleicAcid_LinkageSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # 5.3.6.8.1 Sugar ID (Mandatory).
                StructField(
                    "sugar",
                    ArrayType(
                        SubstanceNucleicAcid_SugarSchema.schema(
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
