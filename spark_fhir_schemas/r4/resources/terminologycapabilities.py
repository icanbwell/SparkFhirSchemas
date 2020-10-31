from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TerminologyCapabilities:
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
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.complex_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_software import TerminologyCapabilities_Software
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_implementation import TerminologyCapabilities_Implementation
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_codesystem import TerminologyCapabilities_CodeSystem
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_expansion import TerminologyCapabilities_Expansion
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_validatecode import TerminologyCapabilities_ValidateCode
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_translation import TerminologyCapabilities_Translation
        from spark_fhir_schemas.r4.complex_types.terminologycapabilities_closure import TerminologyCapabilities_Closure
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
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField("version", StringType(), True),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("status", StringType(), True),
                StructField("experimental", BooleanType(), True),
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField("publisher", StringType(), True),
                StructField(
                    "contact",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "description", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "useContext",
                    ArrayType(UsageContext.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "purpose", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "kind", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "software",
                    TerminologyCapabilities_Software.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implementation",
                    TerminologyCapabilities_Implementation.
                    get_schema(recursion_depth + 1), True
                ),
                StructField("lockedDate", BooleanType(), True),
                StructField(
                    "codeSystem",
                    ArrayType(
                        TerminologyCapabilities_CodeSystem.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "expansion",
                    TerminologyCapabilities_Expansion.
                    get_schema(recursion_depth + 1), True
                ),
                StructField("codeSearch", StringType(), True),
                StructField(
                    "validateCode",
                    TerminologyCapabilities_ValidateCode.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "translation",
                    TerminologyCapabilities_Translation.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "closure",
                    TerminologyCapabilities_Closure.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
