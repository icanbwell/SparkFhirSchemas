from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class VisionPrescription_LensSpecification:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.visionprescription_prism import VisionPrescription_Prism
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
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
                    "product", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("eye", StringType(), True),
                StructField(
                    "sphere", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "cylinder", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "axis", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "prism",
                    ArrayType(
                        VisionPrescription_Prism.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "add", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "power", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "backCurve", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "diameter", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "duration", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField("color", StringType(), True),
                StructField("brand", StringType(), True),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )

        return schema
