from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Contract:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.contract_contentdefinition import Contract_ContentDefinition
        from spark_fhir_schemas.r4.complex_types.contract_term import Contract_Term
        from spark_fhir_schemas.r4.complex_types.contract_signer import Contract_Signer
        from spark_fhir_schemas.r4.complex_types.contract_friendly import Contract_Friendly
        from spark_fhir_schemas.r4.complex_types.contract_legal import Contract_Legal
        from spark_fhir_schemas.r4.complex_types.contract_rule import Contract_Rule
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
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
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField("version", StringType(), True),
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "legalState",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "instantiatesCanonical",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "instantiatesUri", uri.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "contentDerivative",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "issued", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "applies", Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "expirationType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "subject",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "authority",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "domain",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "site",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("subtitle", StringType(), True),
                StructField("alias", ArrayType(StringType()), True),
                StructField(
                    "author", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "scope", CodeableConcept.get_schema(recursion_depth + 1),
                    True
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
                    "subType",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "contentDefinition",
                    Contract_ContentDefinition.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "term",
                    ArrayType(Contract_Term.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "supportingInfo",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "relevantHistory",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "signer",
                    ArrayType(Contract_Signer.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "friendly",
                    ArrayType(
                        Contract_Friendly.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "legal",
                    ArrayType(Contract_Legal.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "rule",
                    ArrayType(Contract_Rule.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "legallyBindingAttachment",
                    Attachment.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "legallyBindingReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
