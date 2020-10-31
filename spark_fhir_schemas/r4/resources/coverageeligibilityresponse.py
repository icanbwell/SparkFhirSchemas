from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class CoverageEligibilityResponse:
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
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_insurance import CoverageEligibilityResponse_Insurance
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_error import CoverageEligibilityResponse_Error
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
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("servicedDate", StringType(), True),
                StructField(
                    "servicedPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "created", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "requestor", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "request", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField("outcome", StringType(), True),
                StructField("disposition", StringType(), True),
                StructField(
                    "insurer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "insurance",
                    ArrayType(
                        CoverageEligibilityResponse_Insurance.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("preAuthRef", StringType(), True),
                StructField(
                    "form", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "error",
                    ArrayType(
                        CoverageEligibilityResponse_Error.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
