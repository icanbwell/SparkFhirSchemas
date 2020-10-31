from pyspark.sql.types import ArrayType, StringType, StructField, StructType

from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.decimal import decimal
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.testreport_participant import TestReport_Participant
from spark_fhir_schemas.r4.complex_types.testreport_setup import TestReport_Setup
from spark_fhir_schemas.r4.complex_types.testreport_test import TestReport_Test
from spark_fhir_schemas.r4.complex_types.testreport_teardown import TestReport_Teardown


# noinspection PyPep8Naming
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
                StructField(
                    "contained", ArrayType(ResourceList.get_schema()), True
                ),
                StructField(
                    "extension", ArrayType(Extension.get_schema()), True
                ),
                StructField(
                    "modifierExtension", ArrayType(Extension.get_schema()),
                    True
                ),
                StructField("identifier", Identifier.get_schema(), True),
                StructField("name", StringType(), True),
                StructField("status", StringType(), True),
                StructField("testScript", Reference.get_schema(), True),
                StructField("result", StringType(), True),
                StructField("score", decimal.get_schema(), True),
                StructField("tester", StringType(), True),
                StructField("issued", dateTime.get_schema(), True),
                StructField(
                    "participant",
                    ArrayType(TestReport_Participant.get_schema()), True
                ),
                StructField("setup", TestReport_Setup.get_schema(), True),
                StructField(
                    "test", ArrayType(TestReport_Test.get_schema()), True
                ),
                StructField(
                    "teardown", TestReport_Teardown.get_schema(), True
                ),
            ]
        )

        return schema
