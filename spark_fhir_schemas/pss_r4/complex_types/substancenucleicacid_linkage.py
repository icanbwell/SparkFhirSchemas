from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchSubstanceNucleicAcid_Linkage(
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
        connectivity: Optional[Any] = None,
        identifier: Optional[Any] = None,
        name: Optional[Any] = None,
        residueSite: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            connectivity=connectivity,
            identifier=identifier,
            name=name,
            residueSite=residueSite,
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

        connectivity: The entity that links the sugar residues together should also be captured for
            nearly all naturally occurring nucleic acid the linkage is a phosphate group.
            For many synthetic oligonucleotides phosphorothioate linkages are often seen.
            Linkage connectivity is assumed to be 3’-5’. If the linkage is either 3’-3’ or
            5’-5’ this should be specified.

        identifier: Each linkage will be registered as a fragment and have an ID.

        name: Each linkage will be registered as a fragment and have at least one name. A
            single name shall be assigned to each linkage.

        residueSite: Residues shall be captured as described in 5.3.6.8.3.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.identifier import (
            AutoMapperElasticSearchIdentifier as IdentifierSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("SubstanceNucleicAcid_Linkage")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["SubstanceNucleicAcid_Linkage"]
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
                # The entity that links the sugar residues together should also be captured for
                # nearly all naturally occurring nucleic acid the linkage is a phosphate group.
                # For many synthetic oligonucleotides phosphorothioate linkages are often seen.
                # Linkage connectivity is assumed to be 3’-5’. If the linkage is either 3’-3’ or
                # 5’-5’ this should be specified.
                StructField("connectivity", StringType(), True),
                # Each linkage will be registered as a fragment and have an ID.
                StructField(
                    "identifier",
                    IdentifierSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Each linkage will be registered as a fragment and have at least one name. A
                # single name shall be assigned to each linkage.
                StructField("name", StringType(), True),
                # Residues shall be captured as described in 5.3.6.8.3.
                StructField("residueSite", StringType(), True),
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