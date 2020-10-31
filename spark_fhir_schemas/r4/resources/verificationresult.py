from pyspark.sql.types import ArrayType, DateType, StringType, StructField, StructType


# noinspection PyPep8Naming
class VerificationResult:
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
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.verificationresult_primarysource import VerificationResult_PrimarySource
        from spark_fhir_schemas.r4.complex_types.verificationresult_attestation import VerificationResult_Attestation
        from spark_fhir_schemas.r4.complex_types.verificationresult_validator import VerificationResult_Validator
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
                    "target",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("targetLocation", ArrayType(StringType()), True),
                StructField(
                    "need", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "statusDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "validationType",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "validationProcess",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "frequency", Timing.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "lastPerformed", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("nextScheduled", DateType(), True),
                StructField(
                    "failureAction",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "primarySource",
                    ArrayType(
                        VerificationResult_PrimarySource.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "attestation",
                    VerificationResult_Attestation.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "validator",
                    ArrayType(
                        VerificationResult_Validator.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
