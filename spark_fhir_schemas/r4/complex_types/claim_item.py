from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Claim_Item:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.positiveint import positiveInt
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.address import Address
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.money import Money
        from spark_fhir_schemas.r4.complex_types.decimal import decimal
        from spark_fhir_schemas.r4.complex_types.claim_detail import Claim_Detail
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
                    "sequence", positiveInt.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "careTeamSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "diagnosisSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "procedureSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "informationSequence",
                    ArrayType(positiveInt.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "revenue", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "category",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "productOrService",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "modifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "programCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("servicedDate", StringType(), True),
                StructField(
                    "servicedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "locationCodeableConcept",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "locationAddress", Address.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "locationReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "unitPrice", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "factor", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "net", Money.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "udi",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "bodySite",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subSite",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "encounter",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "detail",
                    ArrayType(Claim_Detail.get_schema(recursion_depth + 1)),
                    True
                ),
            ]
        )

        return schema
