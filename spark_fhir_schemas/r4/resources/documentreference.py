from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class DocumentReference:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.instant import instant
        from spark_fhir_schemas.r4.complex_types.documentreference_relatesto import DocumentReference_RelatesTo
        from spark_fhir_schemas.r4.complex_types.documentreference_content import DocumentReference_Content
        from spark_fhir_schemas.r4.complex_types.documentreference_context import DocumentReference_Context
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    "masterIdentifier",
                    Identifier.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "docStatus", code.get_schema(recursion_depth + 1), True
                ),
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
                    "date", instant.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "author",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "authenticator", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "custodian", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "relatesTo",
                    ArrayType(
                        DocumentReference_RelatesTo.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "securityLabel",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "content",
                    ArrayType(
                        DocumentReference_Content.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "context",
                    DocumentReference_Context.get_schema(recursion_depth + 1),
                    True
                ),
            ]
        )
        return schema
