from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class BodyStructure:
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
        from spark_fhir_schemas.r4.complex_types.attachment import Attachment
        from spark_fhir_schemas.r4.complex_types.reference import Reference
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
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("active", BooleanType(), True),
                StructField(
                    "morphology",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "location",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "locationQualifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "image",
                    ArrayType(Attachment.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
