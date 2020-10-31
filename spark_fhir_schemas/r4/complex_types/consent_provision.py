from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Consent_Provision:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.consent_actor import Consent_Actor
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.consent_data import Consent_Data
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
                StructField("type", StringType(), True),
                StructField(
                    "period", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "actor",
                    ArrayType(Consent_Actor.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "action",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "securityLabel",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "purpose",
                    ArrayType(Coding.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "class", ArrayType(Coding.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "code",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "dataPeriod", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "data",
                    ArrayType(Consent_Data.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "provision",
                    ArrayType(
                        Consent_Provision.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
