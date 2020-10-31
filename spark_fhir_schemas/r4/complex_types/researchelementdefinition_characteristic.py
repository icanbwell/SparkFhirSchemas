from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ResearchElementDefinition_Characteristic:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        The ResearchElementDefinition resource describes a "PICO" element that
        knowledge (evidence, assertion, recommendation) is about.


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

        definitionCodeableConcept: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionCanonical: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionExpression: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        definitionDataRequirement: Define members of the research element using Codes (such as condition,
            medication, or observation), Expressions ( using an expression language such
            as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
            the last year).

        usageContext: Use UsageContext to define the members of the population, such as Age Ranges,
            Genders, Settings.

        exclude: When true, members with this characteristic are excluded from the element.

        unitOfMeasure: Specifies the UCUM unit for the outcome.

        studyEffectiveDescription: A narrative description of the time period the study covers.

        studyEffectiveDateTime: Indicates what effective period the study covers.

        studyEffectivePeriod: Indicates what effective period the study covers.

        studyEffectiveDuration: Indicates what effective period the study covers.

        studyEffectiveTiming: Indicates what effective period the study covers.

        studyEffectiveTimeFromStart: Indicates duration from the study initiation.

        studyEffectiveGroupMeasure: Indicates how elements are aggregated within the study effective period.

        participantEffectiveDescription: A narrative description of the time period the study covers.

        participantEffectiveDateTime: Indicates what effective period the study covers.

        participantEffectivePeriod: Indicates what effective period the study covers.

        participantEffectiveDuration: Indicates what effective period the study covers.

        participantEffectiveTiming: Indicates what effective period the study covers.

        participantEffectiveTimeFromStart: Indicates duration from the participant's study entry.

        participantEffectiveGroupMeasure: Indicates how elements are aggregated within the study effective period.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.expression import Expression
        from spark_fhir_schemas.r4.complex_types.datarequirement import DataRequirement
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.duration import Duration
        from spark_fhir_schemas.r4.complex_types.timing import Timing
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
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField("definitionCanonical", StringType(), True),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionExpression",
                    Expression.get_schema(recursion_depth + 1), True
                ),
                # Define members of the research element using Codes (such as condition,
                # medication, or observation), Expressions ( using an expression language such
                # as FHIRPath or CQL) or DataRequirements (such as Diabetes diagnosis onset in
                # the last year).
                StructField(
                    "definitionDataRequirement",
                    DataRequirement.get_schema(recursion_depth + 1), True
                ),
                # Use UsageContext to define the members of the population, such as Age Ranges,
                # Genders, Settings.
                StructField(
                    "usageContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                # When true, members with this characteristic are excluded from the element.
                StructField("exclude", BooleanType(), True),
                # Specifies the UCUM unit for the outcome.
                StructField(
                    "unitOfMeasure",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A narrative description of the time period the study covers.
                StructField("studyEffectiveDescription", StringType(), True),
                # Indicates what effective period the study covers.
                StructField("studyEffectiveDateTime", StringType(), True),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectivePeriod",
                    Period.get_schema(recursion_depth + 1), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectiveDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "studyEffectiveTiming",
                    Timing.get_schema(recursion_depth + 1), True
                ),
                # Indicates duration from the study initiation.
                StructField(
                    "studyEffectiveTimeFromStart",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                # Indicates how elements are aggregated within the study effective period.
                StructField("studyEffectiveGroupMeasure", StringType(), True),
                # A narrative description of the time period the study covers.
                StructField(
                    "participantEffectiveDescription", StringType(), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveDateTime", StringType(), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectivePeriod",
                    Period.get_schema(recursion_depth + 1), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveDuration",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                # Indicates what effective period the study covers.
                StructField(
                    "participantEffectiveTiming",
                    Timing.get_schema(recursion_depth + 1), True
                ),
                # Indicates duration from the participant's study entry.
                StructField(
                    "participantEffectiveTimeFromStart",
                    Duration.get_schema(recursion_depth + 1), True
                ),
                # Indicates how elements are aggregated within the study effective period.
                StructField(
                    "participantEffectiveGroupMeasure", StringType(), True
                ),
            ]
        )
        return schema
