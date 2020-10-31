from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class Composition:
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
        from spark_fhir_schemas.r4.complex_types.composition_attester import Composition_Attester
        from spark_fhir_schemas.r4.complex_types.composition_relatesto import Composition_RelatesTo
        from spark_fhir_schemas.r4.complex_types.composition_event import Composition_Event
        from spark_fhir_schemas.r4.complex_types.composition_section import Composition_Section
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
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "category",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "date", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "author",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("title", StringType(), True),
                StructField(
                    "confidentiality", code.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "attester",
                    ArrayType(
                        Composition_Attester.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "custodian", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "relatesTo",
                    ArrayType(
                        Composition_RelatesTo.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "event",
                    ArrayType(
                        Composition_Event.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "section",
                    ArrayType(
                        Composition_Section.get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
