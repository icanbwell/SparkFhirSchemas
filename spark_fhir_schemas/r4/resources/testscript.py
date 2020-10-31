from pyspark.sql.types import ArrayType, BooleanType, StringType, StructField, StructType


# noinspection PyPep8Naming
class TestScript:
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
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.contactdetail import ContactDetail
        from spark_fhir_schemas.r4.complex_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.usagecontext import UsageContext
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.testscript_origin import TestScript_Origin
        from spark_fhir_schemas.r4.complex_types.testscript_destination import TestScript_Destination
        from spark_fhir_schemas.r4.complex_types.testscript_metadata import TestScript_Metadata
        from spark_fhir_schemas.r4.complex_types.testscript_fixture import TestScript_Fixture
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.testscript_variable import TestScript_Variable
        from spark_fhir_schemas.r4.complex_types.testscript_setup import TestScript_Setup
        from spark_fhir_schemas.r4.complex_types.testscript_test import TestScript_Test
        from spark_fhir_schemas.r4.complex_types.testscript_teardown import TestScript_Teardown
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
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField(
                    "identifier", Identifier.get_schema(recursion_depth + 1),
                    True
                ),
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
                StructField(
                    "origin",
                    ArrayType(
                        TestScript_Origin.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "destination",
                    ArrayType(
                        TestScript_Destination.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "metadata",
                    TestScript_Metadata.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "fixture",
                    ArrayType(
                        TestScript_Fixture.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "profile",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "variable",
                    ArrayType(
                        TestScript_Variable.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "setup", TestScript_Setup.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "test",
                    ArrayType(TestScript_Test.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "teardown",
                    TestScript_Teardown.get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
