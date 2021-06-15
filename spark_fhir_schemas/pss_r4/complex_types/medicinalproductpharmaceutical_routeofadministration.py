from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMedicinalProductPharmaceutical_RouteOfAdministration(
    AutoMapperDataTypeComplexBase
):
    """
    A pharmaceutical product described in terms of its composition and dose form.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        code: Optional[Any] = None,
        firstDose: Optional[Any] = None,
        maxSingleDose: Optional[Any] = None,
        maxDosePerDay: Optional[Any] = None,
        maxDosePerTreatmentPeriod: Optional[Any] = None,
        maxTreatmentPeriod: Optional[Any] = None,
        targetSpecies: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            firstDose=firstDose,
            maxSingleDose=maxSingleDose,
            maxDosePerDay=maxDosePerDay,
            maxDosePerTreatmentPeriod=maxDosePerTreatmentPeriod,
            maxTreatmentPeriod=maxTreatmentPeriod,
            targetSpecies=targetSpecies,
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
        A pharmaceutical product described in terms of its composition and dose form.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        code: Coded expression for the route.

        firstDose: The first dose (dose quantity) administered in humans can be specified, for a
            product under investigation, using a numerical value and its unit of
            measurement.

        maxSingleDose: The maximum single dose that can be administered as per the protocol of a
            clinical trial can be specified using a numerical value and its unit of
            measurement.

        maxDosePerDay: The maximum dose per day (maximum dose quantity to be administered in any one
            24-h period) that can be administered as per the protocol referenced in the
            clinical trial authorisation.

        maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered as per the
            protocol referenced in the clinical trial authorisation.

        maxTreatmentPeriod: The maximum treatment period during which an Investigational Medicinal Product
            can be administered as per the protocol referenced in the clinical trial
            authorisation.

        targetSpecies: A species for which this route applies.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.duration import (
            AutoMapperElasticSearchDuration as DurationSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.medicinalproductpharmaceutical_targetspecies import (
            AutoMapperElasticSearchMedicinalProductPharmaceutical_TargetSpecies as MedicinalProductPharmaceutical_TargetSpeciesSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count(
                "MedicinalProductPharmaceutical_RouteOfAdministration"
            )
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + [
            "MedicinalProductPharmaceutical_RouteOfAdministration"
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
                # Coded expression for the route.
                StructField(
                    "code",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The first dose (dose quantity) administered in humans can be specified, for a
                # product under investigation, using a numerical value and its unit of
                # measurement.
                StructField(
                    "firstDose",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The maximum single dose that can be administered as per the protocol of a
                # clinical trial can be specified using a numerical value and its unit of
                # measurement.
                StructField(
                    "maxSingleDose",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The maximum dose per day (maximum dose quantity to be administered in any one
                # 24-h period) that can be administered as per the protocol referenced in the
                # clinical trial authorisation.
                StructField(
                    "maxDosePerDay",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The maximum dose per treatment period that can be administered as per the
                # protocol referenced in the clinical trial authorisation.
                StructField(
                    "maxDosePerTreatmentPeriod",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The maximum treatment period during which an Investigational Medicinal Product
                # can be administered as per the protocol referenced in the clinical trial
                # authorisation.
                StructField(
                    "maxTreatmentPeriod",
                    DurationSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A species for which this route applies.
                StructField(
                    "targetSpecies",
                    ArrayType(
                        MedicinalProductPharmaceutical_TargetSpeciesSchema.schema(
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
