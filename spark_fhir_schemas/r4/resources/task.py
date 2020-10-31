from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.canonical import canonical
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.annotation import Annotation
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.task_restriction import Task_Restriction
from spark_fhir_schemas.r4.complex_types.task_input import Task_Input
from spark_fhir_schemas.r4.complex_types.task_output import Task_Output


class Task:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(), True),
                StructField("meta", Meta.get_schema(), True),
                StructField("implicitRules", uri.get_schema(), True),
                StructField("language", code.get_schema(), True),
                StructField("text", Narrative.get_schema(), True),
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("instantiatesCanonical", canonical.get_schema(), True),
                StructField("instantiatesUri", uri.get_schema(), True),
                StructField("basedOn",ArrayType(Reference.get_schema()), True),
                StructField("groupIdentifier", Identifier.get_schema(), True),
                StructField("partOf",ArrayType(Reference.get_schema()), True),
                StructField("status", StringType(), True),
                StructField("statusReason", CodeableConcept.get_schema(), True),
                StructField("businessStatus", CodeableConcept.get_schema(), True),
                StructField("intent", StringType(), True),
                StructField("priority", code.get_schema(), True),
                StructField("code", CodeableConcept.get_schema(), True),
                StructField("description", StringType(), True),
                StructField("focus", Reference.get_schema(), True),
                StructField("for", Reference.get_schema(), True),
                StructField("encounter", Reference.get_schema(), True),
                StructField("executionPeriod", Period.get_schema(), True),
                StructField("authoredOn", dateTime.get_schema(), True),
                StructField("lastModified", dateTime.get_schema(), True),
                StructField("requester", Reference.get_schema(), True),
                StructField("performerType",ArrayType(CodeableConcept.get_schema()), True),
                StructField("owner", Reference.get_schema(), True),
                StructField("location", Reference.get_schema(), True),
                StructField("reasonCode", CodeableConcept.get_schema(), True),
                StructField("reasonReference", Reference.get_schema(), True),
                StructField("insurance",ArrayType(Reference.get_schema()), True),
                StructField("note",ArrayType(Annotation.get_schema()), True),
                StructField("relevantHistory",ArrayType(Reference.get_schema()), True),
                StructField("restriction", Task_Restriction.get_schema(), True),
                StructField("input",ArrayType(Task_Input.get_schema()), True),
                StructField("output",ArrayType(Task_Output.get_schema()), True),
            ]
        )

        return schema
