from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.testreport_participant import TestReport_Participant
from spark_fhir_schemas.r4.resources.testreport_setup import TestReport_Setup
from spark_fhir_schemas.r4.resources.testreport_test import TestReport_Test
from spark_fhir_schemas.r4.resources.testreport_teardown import TestReport_Teardown


class TestReport:
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
                StructField("identifier", Identifier.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("status", StringType(), True),
                StructField("testScript", Reference.get_schema(), True),
                StructField("result", StringType(), True),
                StructField("score", decimal.get_schema(), True),
                StructField("tester", StringType(), True),
                StructField("issued", dateTime.get_schema(), True),
                StructField("participant",ArrayType(TestReport_Participant.get_schema()), True),
                StructField("setup", TestReport_Setup.get_schema(), True),
                StructField("test",ArrayType(TestReport_Test.get_schema()), True),
                StructField("teardown", TestReport_Teardown.get_schema(), True),]
        )

        return schema
