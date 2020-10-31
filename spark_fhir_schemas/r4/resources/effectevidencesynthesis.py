from pyspark.sql.types import ArrayType, DateType, StringType, StructField, StructType


# noinspection PyPep8Naming
class EffectEvidenceSynthesis:
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
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.complex_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.relatedartifact import RelatedArtifact
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_samplesize import EffectEvidenceSynthesis_SampleSize
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_resultsbyexposure import EffectEvidenceSynthesis_ResultsByExposure
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_effectestimate import EffectEvidenceSynthesis_EffectEstimate
        from spark_fhir_schemas.r4.complex_types.effectevidencesynthesis_certainty import EffectEvidenceSynthesis_Certainty
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
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("version", StringType(), True),
                StructField("name", StringType(), True),
                StructField("title", StringType(), True),
                StructField("status", StringType(), True),
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
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
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
                    "copyright", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField("approvalDate", DateType(), True),
                StructField("lastReviewDate", DateType(), True),
                StructField(
                    "effectivePeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "topic",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "author",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "editor",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "reviewer",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "endorser",
                    ArrayType(ContactDetail.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "relatedArtifact",
                    ArrayType(RelatedArtifact.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "synthesisType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "studyType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "population", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "exposure", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "exposureAlternative",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "outcome", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "sampleSize",
                    EffectEvidenceSynthesis_SampleSize.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resultsByExposure",
                    ArrayType(
                        EffectEvidenceSynthesis_ResultsByExposure.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "effectEstimate",
                    ArrayType(
                        EffectEvidenceSynthesis_EffectEstimate.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "certainty",
                    ArrayType(
                        EffectEvidenceSynthesis_Certainty.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
