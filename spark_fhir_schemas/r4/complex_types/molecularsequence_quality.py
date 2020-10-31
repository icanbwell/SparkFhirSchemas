from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MolecularSequence_Quality:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Raw data describing a biological sequence.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.molecularsequence_roc import MolecularSequence_Roc
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # INDEL / SNP / Undefined variant.
                StructField("type", StringType(), True),
                # Gold standard sequence used for comparing against.
                StructField(
                    "standardSequence",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Start position of the sequence. If the coordinate system is either 0-based or
                # 1-based, then start position is inclusive.
                StructField(
                    "start", integer.get_schema(recursion_depth + 1), True
                ),
                # End position of the sequence. If the coordinate system is 0-based then end is
                # exclusive and does not include the last position. If the coordinate system is
                # 1-base, then end is inclusive and includes the last position.
                StructField(
                    "end", integer.get_schema(recursion_depth + 1), True
                ),
                # The score of an experimentally derived feature such as a p-value ([SO:0001685]
                # (http://www.sequenceontology.org/browser/current_svn/term/SO:0001685)).
                StructField(
                    "score", Quantity.get_schema(recursion_depth + 1), True
                ),
                # Which method is used to get sequence quality.
                StructField(
                    "method", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # True positives, from the perspective of the truth data, i.e. the number of
                # sites in the Truth Call Set for which there are paths through the Query Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField(
                    "truthTP", decimal.get_schema(recursion_depth + 1), True
                ),
                # True positives, from the perspective of the query data, i.e. the number of
                # sites in the Query Call Set for which there are paths through the Truth Call
                # Set that are consistent with all of the alleles at this site, and for which
                # there is an accurate genotype call for the event.
                StructField(
                    "queryTP", decimal.get_schema(recursion_depth + 1), True
                ),
                # False negatives, i.e. the number of sites in the Truth Call Set for which
                # there is no path through the Query Call Set that is consistent with all of the
                # alleles at this site, or sites for which there is an inaccurate genotype call
                # for the event. Sites with correct variant but incorrect genotype are counted
                # here.
                StructField(
                    "truthFN", decimal.get_schema(recursion_depth + 1), True
                ),
                # False positives, i.e. the number of sites in the Query Call Set for which
                # there is no path through the Truth Call Set that is consistent with this site.
                # Sites with correct variant but incorrect genotype are counted here.
                StructField(
                    "queryFP", decimal.get_schema(recursion_depth + 1), True
                ),
                # The number of false positives where the non-REF alleles in the Truth and Query
                # Call Sets match (i.e. cases where the truth is 1/1 and the query is 0/1 or
                # similar).
                StructField(
                    "gtFP", decimal.get_schema(recursion_depth + 1), True
                ),
                # QUERY.TP / (QUERY.TP + QUERY.FP).
                StructField(
                    "precision", decimal.get_schema(recursion_depth + 1), True
                ),
                # TRUTH.TP / (TRUTH.TP + TRUTH.FN).
                StructField(
                    "recall", decimal.get_schema(recursion_depth + 1), True
                ),
                # Harmonic mean of Recall and Precision, computed as: 2 * precision * recall /
                # (precision + recall).
                StructField(
                    "fScore", decimal.get_schema(recursion_depth + 1), True
                ),
                # Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity
                # tradeoff.
                StructField(
                    "roc",
                    MolecularSequence_Roc.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
