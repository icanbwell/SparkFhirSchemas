from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMeasureReport_Stratum(AutoMapperDataTypeComplexBase):
    """
    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        value: Optional[Any] = None,
        component: Optional[Any] = None,
        population: Optional[Any] = None,
        measureScore: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            value=value,
            component=component,
            population=population,
            measureScore=measureScore,
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
        The MeasureReport resource contains the results of the calculation of a
        measure; and optionally a reference to the resources involved in that
        calculation.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        value: The value for this stratum, expressed as a CodeableConcept. When defining
            stratifiers on complex values, the value must be rendered such that the value
            for each stratum within the stratifier is unique.

        component: A stratifier component value.

        population: The populations that make up the stratum, one for each type of population
            appropriate to the measure.

        measureScore: The measure score for this stratum, calculated as appropriate for the measure
            type and scoring method, and based on only the members of this stratum.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.measurereport_component import (
            AutoMapperElasticSearchMeasureReport_Component as MeasureReport_ComponentSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.measurereport_population1 import (
            AutoMapperElasticSearchMeasureReport_Population1 as MeasureReport_Population1Schema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MeasureReport_Stratum") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MeasureReport_Stratum"]
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
                # The value for this stratum, expressed as a CodeableConcept. When defining
                # stratifiers on complex values, the value must be rendered such that the value
                # for each stratum within the stratifier is unique.
                StructField(
                    "value",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # A stratifier component value.
                StructField(
                    "component",
                    ArrayType(
                        MeasureReport_ComponentSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The populations that make up the stratum, one for each type of population
                # appropriate to the measure.
                StructField(
                    "population",
                    ArrayType(
                        MeasureReport_Population1Schema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # The measure score for this stratum, calculated as appropriate for the measure
                # type and scoring method, and based on only the members of this stratum.
                StructField(
                    "measureScore",
                    QuantitySchema.schema(
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
