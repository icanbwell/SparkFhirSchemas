from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMolecularSequence_Roc(AutoMapperDataTypeComplexBase):
    """
    Raw data describing a biological sequence.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        score: Optional[Any] = None,
        numTP: Optional[Any] = None,
        numFP: Optional[Any] = None,
        numFN: Optional[Any] = None,
        precision: Optional[Any] = None,
        sensitivity: Optional[Any] = None,
        fMeasure: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            score=score,
            numTP=numTP,
            numFP=numFP,
            numFN=numFN,
            precision=precision,
            sensitivity=sensitivity,
            fMeasure=fMeasure,
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

        score: Invidual data point representing the GQ (genotype quality) score threshold.

        numTP: The number of true positives if the GQ score threshold was set to "score"
            field value.

        numFP: The number of false positives if the GQ score threshold was set to "score"
            field value.

        numFN: The number of false negatives if the GQ score threshold was set to "score"
            field value.

        precision: Calculated precision if the GQ score threshold was set to "score" field value.

        sensitivity: Calculated sensitivity if the GQ score threshold was set to "score" field
            value.

        fMeasure: Calculated fScore if the GQ score threshold was set to "score" field value.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.decimal import (
            AutoMapperElasticSearchdecimal as decimalSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MolecularSequence_Roc") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MolecularSequence_Roc"]
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
                # Invidual data point representing the GQ (genotype quality) score threshold.
                StructField(
                    "score",
                    ArrayType(
                        integerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The number of true positives if the GQ score threshold was set to "score"
                # field value.
                StructField(
                    "numTP",
                    ArrayType(
                        integerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The number of false positives if the GQ score threshold was set to "score"
                # field value.
                StructField(
                    "numFP",
                    ArrayType(
                        integerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The number of false negatives if the GQ score threshold was set to "score"
                # field value.
                StructField(
                    "numFN",
                    ArrayType(
                        integerSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Calculated precision if the GQ score threshold was set to "score" field value.
                StructField(
                    "precision",
                    ArrayType(
                        decimalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Calculated sensitivity if the GQ score threshold was set to "score" field
                # value.
                StructField(
                    "sensitivity",
                    ArrayType(
                        decimalSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Calculated fScore if the GQ score threshold was set to "score" field value.
                StructField(
                    "fMeasure",
                    ArrayType(
                        decimalSchema.schema(
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