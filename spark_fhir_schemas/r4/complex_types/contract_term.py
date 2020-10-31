from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Contract_Term:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.contract_securitylabel import Contract_SecurityLabel
        from spark_fhir_schemas.r4.complex_types.contract_offer import Contract_Offer
        from spark_fhir_schemas.r4.complex_types.contract_asset import Contract_Asset
        from spark_fhir_schemas.r4.complex_types.contract_action import Contract_Action
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
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "issued", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "applies", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "topicCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "topicReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "subType", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("text", StringType(), True),
                StructField(
                    "securityLabel",
                    ArrayType(
                        Contract_SecurityLabel.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "offer", Contract_Offer.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "asset",
                    ArrayType(Contract_Asset.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "action",
                    ArrayType(Contract_Action.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "group",
                    ArrayType(Contract_Term.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )

        return schema
