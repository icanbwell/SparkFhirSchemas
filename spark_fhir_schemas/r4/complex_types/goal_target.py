from pyspark.sql.types import ArrayType, BooleanType, IntegerType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Goal_Target:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.range import Range
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.duration import Duration
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
                    "measure", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "detailQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "detailRange", Range.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "detailCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("detailString", StringType(), True),
                StructField("detailBoolean", BooleanType(), True),
                StructField("detailInteger", IntegerType(), True),
                StructField(
                    "detailRatio", Ratio.get_schema(recursion_depth + 1), True
                ),
                StructField("dueDate", StringType(), True),
                StructField(
                    "dueDuration", Duration.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
