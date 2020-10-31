from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Observation_Component:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Measurements and simple assertions made about a patient, device or other
        subject.


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

        code: Describes what was observed. Sometimes this is called the observation "code".

        valueQuantity: The information determined as a result of making the observation, if the
            information has a simple value.

        valueCodeableConcept: The information determined as a result of making the observation, if the
            information has a simple value.

        valueString: The information determined as a result of making the observation, if the
            information has a simple value.

        valueBoolean: The information determined as a result of making the observation, if the
            information has a simple value.

        valueInteger: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRange: The information determined as a result of making the observation, if the
            information has a simple value.

        valueRatio: The information determined as a result of making the observation, if the
            information has a simple value.

        valueSampledData: The information determined as a result of making the observation, if the
            information has a simple value.

        valueTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valueDateTime: The information determined as a result of making the observation, if the
            information has a simple value.

        valuePeriod: The information determined as a result of making the observation, if the
            information has a simple value.

        dataAbsentReason: Provides a reason why the expected value in the element
            Observation.component.value[x] is missing.

        interpretation: A categorical assessment of an observation value.  For example, high, low,
            normal.

        referenceRange: Guidance on how to interpret the value by comparison to a normal or
            recommended range.

        """
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.sampleddata import SampledData
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.observation_referencerange import Observation_ReferenceRange
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
                # Describes what was observed. Sometimes this is called the observation "code".
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueString", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueBoolean", BooleanType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueInteger", IntegerType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueTime", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField("valueDateTime", StringType(), True),
                # The information determined as a result of making the observation, if the
                # information has a simple value.
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                # Provides a reason why the expected value in the element
                # Observation.component.value[x] is missing.
                StructField(
                    "dataAbsentReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # A categorical assessment of an observation value.  For example, high, low,
                # normal.
                StructField(
                    "interpretation",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Guidance on how to interpret the value by comparison to a normal or
                # recommended range.
                StructField(
                    "referenceRange",
                    ArrayType(
                        Observation_ReferenceRange.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
