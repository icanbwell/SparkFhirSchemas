from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class MeasureReport_Stratum:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
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

        value: The value for this stratum, expressed as a CodeableConcept. When defining
            stratifiers on complex values, the value must be rendered such that the value
            for each stratum within the stratifier is unique.

        component: A stratifier component value.

        population: The populations that make up the stratum, one for each type of population
            appropriate to the measure.

        measureScore: The measure score for this stratum, calculated as appropriate for the measure
            type and scoring method, and based on only the members of this stratum.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.measurereport_component import MeasureReport_Component
        from spark_fhir_schemas.r4.complex_types.measurereport_population1 import MeasureReport_Population1
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
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
                # The value for this stratum, expressed as a CodeableConcept. When defining
                # stratifiers on complex values, the value must be rendered such that the value
                # for each stratum within the stratifier is unique.
                StructField(
                    "value", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # A stratifier component value.
                StructField(
                    "component",
                    ArrayType(
                        MeasureReport_Component.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The populations that make up the stratum, one for each type of population
                # appropriate to the measure.
                StructField(
                    "population",
                    ArrayType(
                        MeasureReport_Population1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # The measure score for this stratum, calculated as appropriate for the measure
                # type and scoring method, and based on only the members of this stratum.
                StructField(
                    "measureScore", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
