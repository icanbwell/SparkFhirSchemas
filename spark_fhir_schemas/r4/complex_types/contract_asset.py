from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Contract_Asset:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.contract_context import Contract_Context
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.contract_answer import Contract_Answer
        from spark_fhir_schemas.r4.complex_types.unsignedint import unsignedInt
        from spark_fhir_schemas.r4.complex_types.contract_valueditem import Contract_ValuedItem
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
                    "scope", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "type",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "typeReference",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "subtype",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "relationship", Coding.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "context",
                    ArrayType(
                        Contract_Context.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("condition", StringType(), True),
                StructField(
                    "periodType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "period",
                    ArrayType(Period.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "usePeriod",
                    ArrayType(Period.get_schema(recursion_depth + 1)), True
                ),
                StructField("text", StringType(), True),
                StructField("linkId", ArrayType(StringType()), True),
                StructField(
                    "answer",
                    ArrayType(Contract_Answer.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "securityLabelNumber",
                    ArrayType(unsignedInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "valuedItem",
                    ArrayType(
                        Contract_ValuedItem.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
