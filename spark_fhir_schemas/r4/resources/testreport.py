from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class TestReport:
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
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.decimal import decimal
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.testreport_participant import TestReport_Participant
        from spark_fhir_schemas.r4.complex_types.testreport_setup import TestReport_Setup
        from spark_fhir_schemas.r4.complex_types.testreport_test import TestReport_Test
        from spark_fhir_schemas.r4.complex_types.testreport_teardown import TestReport_Teardown
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
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("name", StringType(), True),
                StructField("status", StringType(), True),
                StructField(
                    "testScript", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField("result", StringType(), True),
                StructField(
                    "score", decimal.get_schema(recursion_depth + 1), True
                ),
                StructField("tester", StringType(), True),
                StructField(
                    "issued", dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "participant",
                    ArrayType(
                        TestReport_Participant.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "setup", TestReport_Setup.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "test",
                    ArrayType(TestReport_Test.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "teardown",
                    TestReport_Teardown.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
