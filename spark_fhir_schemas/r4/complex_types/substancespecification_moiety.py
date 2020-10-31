from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SubstanceSpecification_Moiety:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
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
                    "role", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("name", StringType(), True),
                StructField(
                    "stereochemistry",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "opticalActivity",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("molecularFormula", StringType(), True),
                StructField(
                    "amountQuantity", Quantity.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("amountString", StringType(), True),
            ]
        )

        return schema
