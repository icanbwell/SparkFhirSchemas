from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Observation_Component:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
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
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "code", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "valueCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("valueString", StringType(), True),
                StructField("valueBoolean", BooleanType(), True),
                StructField("valueInteger", IntegerType(), True),
                StructField(
                    "valueRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "valueSampledData",
                    SampledData.get_schema(recursion_depth + 1), True
                ),
                StructField("valueTime", StringType(), True),
                StructField("valueDateTime", StringType(), True),
                StructField(
                    "valuePeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dataAbsentReason",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "interpretation",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
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
