from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Contract_Offer:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.contract_party import Contract_Party
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.contract_answer import Contract_Answer
        from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
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
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "party",
                    ArrayType(Contract_Party.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "topic", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "decision",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "decisionMode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "answer",
                    ArrayType(Contract_Answer.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("text", StringType(), True),
                StructField("linkId", ArrayType(StringType()), True),
                StructField(
                    "securityLabelNumber",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )

        return schema
