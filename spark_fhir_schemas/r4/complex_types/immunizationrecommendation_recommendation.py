from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class ImmunizationRecommendation_Recommendation:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A patient's point-in-time set of recommendations (i.e. forecasting) according
        to a published schedule with optional supporting justification.


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

        vaccineCode: Vaccine(s) or vaccine group that pertain to the recommendation.

        targetDisease: The targeted disease for the recommendation.

        contraindicatedVaccineCode: Vaccine(s) which should not be used to fulfill the recommendation.

        forecastStatus: Indicates the patient status with respect to the path to immunity for the
            target disease.

        forecastReason: The reason for the assigned forecast status.

        dateCriterion: Vaccine date recommendations.  For example, earliest date to administer,
            latest date to administer, etc.

        description: Contains the description about the protocol under which the vaccine was
            administered.

        series: One possible path to achieve presumed immunity against a disease - within the
            context of an authority.

        doseNumberPositiveInt: Nominal position of the recommended dose in a series (e.g. dose 2 is the next
            recommended dose).

        doseNumberString: Nominal position of the recommended dose in a series (e.g. dose 2 is the next
            recommended dose).

        seriesDosesPositiveInt: The recommended number of doses to achieve immunity.

        seriesDosesString: The recommended number of doses to achieve immunity.

        supportingImmunization: Immunization event history and/or evaluation that supports the status and
            recommendation.

        supportingPatientInformation: Patient Information that supports the status and recommendation.  This
            includes patient observations, adverse reactions and allergy/intolerance
            information.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.immunizationrecommendation_datecriterion import ImmunizationRecommendation_DateCriterion
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                # Vaccine(s) or vaccine group that pertain to the recommendation.
                StructField(
                    "vaccineCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # The targeted disease for the recommendation.
                StructField(
                    "targetDisease",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Vaccine(s) which should not be used to fulfill the recommendation.
                StructField(
                    "contraindicatedVaccineCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Indicates the patient status with respect to the path to immunity for the
                # target disease.
                StructField(
                    "forecastStatus",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The reason for the assigned forecast status.
                StructField(
                    "forecastReason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Vaccine date recommendations.  For example, earliest date to administer,
                # latest date to administer, etc.
                StructField(
                    "dateCriterion",
                    ArrayType(
                        ImmunizationRecommendation_DateCriterion.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Contains the description about the protocol under which the vaccine was
                # administered.
                StructField("description", StringType(), True),
                # One possible path to achieve presumed immunity against a disease - within the
                # context of an authority.
                StructField("series", StringType(), True),
                # Nominal position of the recommended dose in a series (e.g. dose 2 is the next
                # recommended dose).
                StructField("doseNumberPositiveInt", IntegerType(), True),
                # Nominal position of the recommended dose in a series (e.g. dose 2 is the next
                # recommended dose).
                StructField("doseNumberString", StringType(), True),
                # The recommended number of doses to achieve immunity.
                StructField("seriesDosesPositiveInt", IntegerType(), True),
                # The recommended number of doses to achieve immunity.
                StructField("seriesDosesString", StringType(), True),
                # Immunization event history and/or evaluation that supports the status and
                # recommendation.
                StructField(
                    "supportingImmunization",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # Patient Information that supports the status and recommendation.  This
                # includes patient observations, adverse reactions and allergy/intolerance
                # information.
                StructField(
                    "supportingPatientInformation",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
