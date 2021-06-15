from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceProtein_Subunit(AutoMapperDataTypeComplexBase):
    """
    A SubstanceProtein is defined as a single unit of a linear amino acid
    sequence, or a combination of subunits that are either covalently linked or
    have a defined invariant stoichiometric relationship. This includes all
    synthetic, recombinant and purified SubstanceProteins of defined sequence,
    whether the use is therapeutic or prophylactic. This set of elements will be
    used to describe albumins, coagulation factors, cytokines, growth factors,
    peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant
    vaccines, and immunomodulators.
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
        nTerminalModificationId: Optional[Any] = None,
        nTerminalModification: Optional[Any] = None,
        cTerminalModificationId: Optional[Any] = None,
        cTerminalModification: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            subunit=subunit,
            sequence=sequence,
            length=length,
            sequenceAttachment=sequenceAttachment,
            nTerminalModificationId=nTerminalModificationId,
            nTerminalModification=nTerminalModification,
            cTerminalModificationId=cTerminalModificationId,
            cTerminalModification=cTerminalModification,
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
        A SubstanceProtein is defined as a single unit of a linear amino acid
        sequence, or a combination of subunits that are either covalently linked or
        have a defined invariant stoichiometric relationship. This includes all
        synthetic, recombinant and purified SubstanceProteins of defined sequence,
        whether the use is therapeutic or prophylactic. This set of elements will be
        used to describe albumins, coagulation factors, cytokines, growth factors,
        peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant
        vaccines, and immunomodulators.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        subunit: Index of primary sequences of amino acids linked through peptide bonds in
            order of decreasing length. Sequences of the same length will be ordered by
            molecular weight. Subunits that have identical sequences will be repeated and
            have sequential subscripts.

        sequence: The sequence information shall be provided enumerating the amino acids from N-
            to C-terminal end using standard single-letter amino acid codes. Uppercase
            shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
            SubstanceProteins will always be described using the translated sequence; for
            synthetic peptide containing amino acids that are not represented with a
            single letter code an X should be used within the sequence. The modified amino
            acids will be distinguished by their position in the sequence.

        length: Length of linear sequences of amino acids contained in the subunit.

        sequenceAttachment: The sequence information shall be provided enumerating the amino acids from N-
            to C-terminal end using standard single-letter amino acid codes. Uppercase
            shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
            SubstanceProteins will always be described using the translated sequence; for
            synthetic peptide containing amino acids that are not represented with a
            single letter code an X should be used within the sequence. The modified amino
            acids will be distinguished by their position in the sequence.

        nTerminalModificationId: Unique identifier for molecular fragment modification based on the ISO 11238
            Substance ID.

        nTerminalModification: The name of the fragment modified at the N-terminal of the SubstanceProtein
            shall be specified.

        cTerminalModificationId: Unique identifier for molecular fragment modification based on the ISO 11238
            Substance ID.

        cTerminalModification: The modification at the C-terminal shall be specified.

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
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceProtein_Subunit") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SubstanceProtein_Subunit"]
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
                # Index of primary sequences of amino acids linked through peptide bonds in
                # order of decreasing length. Sequences of the same length will be ordered by
                # molecular weight. Subunits that have identical sequences will be repeated and
                # have sequential subscripts.
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
                # The sequence information shall be provided enumerating the amino acids from N-
                # to C-terminal end using standard single-letter amino acid codes. Uppercase
                # shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
                # SubstanceProteins will always be described using the translated sequence; for
                # synthetic peptide containing amino acids that are not represented with a
                # single letter code an X should be used within the sequence. The modified amino
                # acids will be distinguished by their position in the sequence.
                StructField("sequence", StringType(), True),
                # Length of linear sequences of amino acids contained in the subunit.
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
                # The sequence information shall be provided enumerating the amino acids from N-
                # to C-terminal end using standard single-letter amino acid codes. Uppercase
                # shall be used for L-amino acids and lowercase for D-amino acids. Transcribed
                # SubstanceProteins will always be described using the translated sequence; for
                # synthetic peptide containing amino acids that are not represented with a
                # single letter code an X should be used within the sequence. The modified amino
                # acids will be distinguished by their position in the sequence.
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
                # Unique identifier for molecular fragment modification based on the ISO 11238
                # Substance ID.
                StructField(
                    "nTerminalModificationId",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The name of the fragment modified at the N-terminal of the SubstanceProtein
                # shall be specified.
                StructField("nTerminalModification", StringType(), True),
                # Unique identifier for molecular fragment modification based on the ISO 11238
                # Substance ID.
                StructField(
                    "cTerminalModificationId",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The modification at the C-terminal shall be specified.
                StructField("cTerminalModification", StringType(), True),
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
