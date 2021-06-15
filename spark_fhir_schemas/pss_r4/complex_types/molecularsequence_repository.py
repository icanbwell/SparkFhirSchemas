from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMolecularSequence_Repository(
    AutoMapperDataTypeComplexBase
):
    """
    Raw data describing a biological sequence.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        url: Optional[Any] = None,
        name: Optional[Any] = None,
        datasetId: Optional[Any] = None,
        variantsetId: Optional[Any] = None,
        readsetId: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            url=url,
            name=name,
            datasetId=datasetId,
            variantsetId=variantsetId,
            readsetId=readsetId,
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

        type: Click and see / RESTful API / Need login to see / RESTful API with
            authentication / Other ways to see resource.

        url: URI of an external repository which contains further details about the
            genetics data.

        name: URI of an external repository which contains further details about the
            genetics data.

        datasetId: Id of the variant in this external repository. The server will understand how
            to use this id to call for more info about datasets in external repository.

        variantsetId: Id of the variantset in this external repository. The server will understand
            how to use this id to call for more info about variantsets in external
            repository.

        readsetId: Id of the read in this external repository.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.uri import (
            AutoMapperElasticSearchuri as uriSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MolecularSequence_Repository")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MolecularSequence_Repository"]
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
                # Click and see / RESTful API / Need login to see / RESTful API with
                # authentication / Other ways to see resource.
                StructField("type", StringType(), True),
                # URI of an external repository which contains further details about the
                # genetics data.
                StructField(
                    "url",
                    uriSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # URI of an external repository which contains further details about the
                # genetics data.
                StructField("name", StringType(), True),
                # Id of the variant in this external repository. The server will understand how
                # to use this id to call for more info about datasets in external repository.
                StructField("datasetId", StringType(), True),
                # Id of the variantset in this external repository. The server will understand
                # how to use this id to call for more info about variantsets in external
                # repository.
                StructField("variantsetId", StringType(), True),
                # Id of the read in this external repository.
                StructField("readsetId", StringType(), True),
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
