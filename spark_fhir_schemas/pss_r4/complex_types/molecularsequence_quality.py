from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMolecularSequence_Quality(AutoMapperDataTypeComplexBase):
    """
    Raw data describing a biological sequence.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        type_: Optional[Any] = None,
        standardSequence: Optional[Any] = None,
        start: Optional[Any] = None,
        end: Optional[Any] = None,
        score: Optional[Any] = None,
        method: Optional[Any] = None,
        truthTP: Optional[Any] = None,
        queryTP: Optional[Any] = None,
        truthFN: Optional[Any] = None,
        queryFP: Optional[Any] = None,
        gtFP: Optional[Any] = None,
        precision: Optional[Any] = None,
        recall: Optional[Any] = None,
        fScore: Optional[Any] = None,
        roc: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            standardSequence=standardSequence,
            start=start,
            end=end,
            score=score,
            method=method,
            truthTP=truthTP,
            queryTP=queryTP,
            truthFN=truthFN,
            queryFP=queryFP,
            gtFP=gtFP,
            precision=precision,
            recall=recall,
            fScore=fScore,
            roc=roc,
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

        type: INDEL / SNP / Undefined variant.

        standardSequence: Gold standard sequence used for comparing against.

        start: Start position of the sequence. If the coordinate system is either 0-based or
            1-based, then start position is inclusive.

        end: End position of the sequence. If the coordinate system is 0-based then end is
            exclusive and does not include the last position. If the coordinate system is
            1-base, then end is inclusive and includes the last position.

        score: The score of an experimentally derived feature such as a p-value ([SO:0001685]
            (http://www.sequenceontology.org/browser/current_svn/term/SO:0001685)).

        method: Which method is used to get sequence quality.

        truthTP: True positives, from the perspective of the truth data, i.e. the number of
            sites in the Truth Call Set for which there are paths through the Query Call
            Set that are consistent with all of the alleles at this site, and for which
            there is an accurate genotype call for the event.

        queryTP: True positives, from the perspective of the query data, i.e. the number of
            sites in the Query Call Set for which there are paths through the Truth Call
            Set that are consistent with all of the alleles at this site, and for which
            there is an accurate genotype call for the event.

        truthFN: False negatives, i.e. the number of sites in the Truth Call Set for which
            there is no path through the Query Call Set that is consistent with all of the
            alleles at this site, or sites for which there is an inaccurate genotype call
            for the event. Sites with correct variant but incorrect genotype are counted
            here.

        queryFP: False positives, i.e. the number of sites in the Query Call Set for which
            there is no path through the Truth Call Set that is consistent with this site.
            Sites with correct variant but incorrect genotype are counted here.

        gtFP: The number of false positives where the non-REF alleles in the Truth and Query
            Call Sets match (i.e. cases where the truth is 1/1 and the query is 0/1 or
            similar).

        precision: QUERY.TP / (QUERY.TP + QUERY.FP).

        recall: TRUTH.TP / (TRUTH.TP + TRUTH.FN).

        fScore: Harmonic mean of Recall and Precision, computed as: 2 * precision * recall /
            (precision + recall).

        roc: Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity
            tradeoff.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.decimal import (
            AutoMapperElasticSearchdecimal as decimalSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.molecularsequence_roc import (
            AutoMapperElasticSearchMolecularSequence_Roc as MolecularSequence_RocSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MolecularSequence_Quality") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MolecularSequence_Quality"]
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
                # INDEL / SNP / Undefined variant.
                StructField("type", StringType(), True),
                # Gold standard sequence used for comparing against.
                StructField(
                    "standardSequence",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Start position of the sequence. If the coordinate system is either 0-based or
                # 1-based, then start position is inclusive.
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
                # End position of the sequence. If the coordinate system is 0-based then end is
                # exclusive and does not include the last position. If the coordinate system is
                # 1-base, then end is inclusive and includes the last position.
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
                # The score of an experimentally derived feature such as a p-value ([SO:0001685]
                # (http://www.sequenceontology.org/browser/current_svn/term/SO:0001685)).
                StructField(
                    "score",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Which method is used to get sequence quality.
                StructField(
                    "method",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # True positives, from the perspective of the truth data, i.e. the number of
                # sites in the Truth Call Set for which there are paths through the Query Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField(
                    "truthTP",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # True positives, from the perspective of the query data, i.e. the number of
                # sites in the Query Call Set for which there are paths through the Truth Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField(
                    "queryTP",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # False negatives, i.e. the number of sites in the Truth Call Set for which
                # there is no path through the Query Call Set that is consistent with all of the
                # alleles at this site, or sites for which there is an inaccurate genotype call
                # for the event. Sites with correct variant but incorrect genotype are counted
                # here.
                StructField(
                    "truthFN",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # False positives, i.e. the number of sites in the Query Call Set for which
                # there is no path through the Truth Call Set that is consistent with this site.
                # Sites with correct variant but incorrect genotype are counted here.
                StructField(
                    "queryFP",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The number of false positives where the non-REF alleles in the Truth and Query
                # Call Sets match (i.e. cases where the truth is 1/1 and the query is 0/1 or
                # similar).
                StructField(
                    "gtFP",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # QUERY.TP / (QUERY.TP + QUERY.FP).
                StructField(
                    "precision",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # TRUTH.TP / (TRUTH.TP + TRUTH.FN).
                StructField(
                    "recall",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Harmonic mean of Recall and Precision, computed as: 2 * precision * recall /
                # (precision + recall).
                StructField(
                    "fScore",
                    decimalSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity
                # tradeoff.
                StructField(
                    "roc",
                    MolecularSequence_RocSchema.schema(
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