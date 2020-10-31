from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class OperationDefinition:
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
        from spark_fhir_schemas.r4.complex_types.operationdefinition_parameter import OperationDefinition_Parameter
        from spark_fhir_schemas.r4.complex_types.operationdefinition_overload import OperationDefinition_Overload
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
                StructField("kind", StringType(), True),
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
                StructField("affectsState", BooleanType(), True),
                StructField(
                    "code", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "comment", markdown.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "base", canonical.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resource",
                    ArrayType(code.get_schema(recursion_depth + 1)), True
                ),
                StructField("system", BooleanType(), True),
                StructField("type", BooleanType(), True),
                StructField("instance", BooleanType(), True),
                StructField(
                    "inputProfile", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "outputProfile", canonical.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "parameter",
                    ArrayType(
                        OperationDefinition_Parameter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "overload",
                    ArrayType(
                        OperationDefinition_Overload.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )
        return schema
