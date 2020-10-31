from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class CapabilityStatement:
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
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.simple_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_software import CapabilityStatement_Software
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_implementation import CapabilityStatement_Implementation
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_rest import CapabilityStatement_Rest
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_messaging import CapabilityStatement_Messaging
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_document import CapabilityStatement_Document
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
                StructField("kind", StringType(), True),
                StructField(
                    "instantiates",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "imports",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "software",
                    CapabilityStatement_Software.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implementation",
                    CapabilityStatement_Implementation.
                    get_schema(recursion_depth + 1), True
                ),
                StructField("fhirVersion", StringType(), True),
                StructField(
                    "format", ArrayType(code.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "patchFormat",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "implementationGuide",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "rest",
                    ArrayType(
                        CapabilityStatement_Rest.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "messaging",
                    ArrayType(
                        CapabilityStatement_Messaging.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "document",
                    ArrayType(
                        CapabilityStatement_Document.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
