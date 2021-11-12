from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    IntegerType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchImmunizationRecommendation_Recommendation(
    AutoMapperDataTypeComplexBase
):
    """
    A patient's point-in-time set of recommendations (i.e. forecasting) according
    to a published schedule with optional supporting justification.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        vaccineCode: Optional[Any] = None,
        targetDisease: Optional[Any] = None,
        contraindicatedVaccineCode: Optional[Any] = None,
        forecastStatus: Optional[Any] = None,
        forecastReason: Optional[Any] = None,
        dateCriterion: Optional[Any] = None,
        description: Optional[Any] = None,
        series: Optional[Any] = None,
        doseNumberPositiveInt: Optional[Any] = None,
        doseNumberString: Optional[Any] = None,
        seriesDosesPositiveInt: Optional[Any] = None,
        seriesDosesString: Optional[Any] = None,
        supportingImmunization: Optional[Any] = None,
        supportingPatientInformation: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            vaccineCode=vaccineCode,
            targetDisease=targetDisease,
            contraindicatedVaccineCode=contraindicatedVaccineCode,
            forecastStatus=forecastStatus,
            forecastReason=forecastReason,
            dateCriterion=dateCriterion,
            description=description,
            series=series,
            doseNumberPositiveInt=doseNumberPositiveInt,
            doseNumberString=doseNumberString,
            seriesDosesPositiveInt=seriesDosesPositiveInt,
            seriesDosesString=seriesDosesString,
            supportingImmunization=supportingImmunization,
            supportingPatientInformation=supportingPatientInformation,
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
        A patient's point-in-time set of recommendations (i.e. forecasting) according
        to a published schedule with optional supporting justification.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

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
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.immunizationrecommendation_datecriterion import (
            AutoMapperElasticSearchImmunizationRecommendation_DateCriterion as ImmunizationRecommendation_DateCriterionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("ImmunizationRecommendation_Recommendation")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "ImmunizationRecommendation_Recommendation"
        ]
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
                # Vaccine(s) or vaccine group that pertain to the recommendation.
                StructField(
                    "vaccineCode",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The targeted disease for the recommendation.
                StructField(
                    "targetDisease",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Vaccine(s) which should not be used to fulfill the recommendation.
                StructField(
                    "contraindicatedVaccineCode",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates the patient status with respect to the path to immunity for the
                # target disease.
                StructField(
                    "forecastStatus",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The reason for the assigned forecast status.
                StructField(
                    "forecastReason",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Vaccine date recommendations.  For example, earliest date to administer,
                # latest date to administer, etc.
                StructField(
                    "dateCriterion",
                    ArrayType(
                        ImmunizationRecommendation_DateCriterionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
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
                    ArrayType(
                        ReferenceSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Patient Information that supports the status and recommendation.  This
                # includes patient observations, adverse reactions and allergy/intolerance
                # information.
                StructField(
                    "supportingPatientInformation",
                    ArrayType(
                        ReferenceSchema.schema(
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
