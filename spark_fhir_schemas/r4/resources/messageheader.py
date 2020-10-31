from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MessageHeader:
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
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.messageheader_destination import MessageHeader_Destination
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.messageheader_source import MessageHeader_Source
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.messageheader_response import MessageHeader_Response
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
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
                    "eventCoding", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField("eventUri", StringType(), True),
                StructField(
                    "destination",
                    ArrayType(
                        MessageHeader_Destination.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "sender", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "enterer", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "author", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "source",
                    MessageHeader_Source.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "responsible", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "reason", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "response",
                    MessageHeader_Response.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "focus",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "definition", canonical.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )

        return schema
