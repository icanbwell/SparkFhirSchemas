from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Provenance:
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
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.provenance_agent import Provenance_Agent
        from spark_fhir_schemas.r4.complex_types.provenance_entity import Provenance_Entity
        from spark_fhir_schemas.r4.complex_types.signature import Signature
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
                StructField(
                    "occurredPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("occurredDateTime", StringType(), True),
                StructField(
                    "recorded", instant.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "policy", ArrayType(uri.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "location", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "reason",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "activity",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "agent",
                    ArrayType(
                        Provenance_Agent.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "entity",
                    ArrayType(
                        Provenance_Entity.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "signature",
                    ArrayType(Signature.get_schema(recursion_depth + 1)), True
                ),
            ]
        )

        return schema
