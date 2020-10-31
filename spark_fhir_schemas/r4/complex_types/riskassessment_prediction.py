from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class RiskAssessment_Prediction:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        An assessment of the likely outcome(s) for a patient or other subject as well
        as the likelihood of each outcome.


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

        outcome: One of the potential outcomes for the patient (e.g. remission, death,  a
            particular condition).

        probabilityDecimal: Indicates how likely the outcome is (in the specified timeframe).

        probabilityRange: Indicates how likely the outcome is (in the specified timeframe).

        qualitativeRisk: Indicates how likely the outcome is (in the specified timeframe), expressed as
            a qualitative value (e.g. low, medium, or high).

        relativeRisk: Indicates the risk for this particular subject (with their specific
            characteristics) divided by the risk of the population in general.  (Numbers
            greater than 1 = higher risk than the population, numbers less than 1 = lower
            risk.).

        whenPeriod: Indicates the period of time or age range of the subject to which the
            specified probability applies.

        whenRange: Indicates the period of time or age range of the subject to which the
            specified probability applies.

        rationale: Additional information explaining the basis for the prediction.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.period import Period
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
                # One of the potential outcomes for the patient (e.g. remission, death,  a
                # particular condition).
                StructField(
                    "outcome", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates how likely the outcome is (in the specified timeframe).
                StructField("probabilityDecimal", IntegerType(), True),
                # Indicates how likely the outcome is (in the specified timeframe).
                StructField(
                    "probabilityRange", Range.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates how likely the outcome is (in the specified timeframe), expressed as
                # a qualitative value (e.g. low, medium, or high).
                StructField(
                    "qualitativeRisk",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Indicates the risk for this particular subject (with their specific
                # characteristics) divided by the risk of the population in general.  (Numbers
                # greater than 1 = higher risk than the population, numbers less than 1 = lower
                # risk.).
                StructField(
                    "relativeRisk", decimal.get_schema(recursion_depth + 1),
                    True
                ),
                # Indicates the period of time or age range of the subject to which the
                # specified probability applies.
                StructField(
                    "whenPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # Indicates the period of time or age range of the subject to which the
                # specified probability applies.
                StructField(
                    "whenRange", Range.get_schema(recursion_depth + 1), True
                ),
                # Additional information explaining the basis for the prediction.
                StructField("rationale", StringType(), True),
            ]
        )
        return schema
