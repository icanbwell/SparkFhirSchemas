from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class ImplementationGuide_Definition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.implementationguide_grouping import ImplementationGuide_Grouping
        from spark_fhir_schemas.r4.complex_types.implementationguide_resource import ImplementationGuide_Resource
        from spark_fhir_schemas.r4.complex_types.implementationguide_page import ImplementationGuide_Page
        from spark_fhir_schemas.r4.complex_types.implementationguide_parameter import ImplementationGuide_Parameter
        from spark_fhir_schemas.r4.complex_types.implementationguide_template import ImplementationGuide_Template
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "grouping",
                    ArrayType(
                        ImplementationGuide_Grouping.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "resource",
                    ArrayType(
                        ImplementationGuide_Resource.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "page",
                    ImplementationGuide_Page.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "parameter",
                    ArrayType(
                        ImplementationGuide_Parameter.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "template",
                    ArrayType(
                        ImplementationGuide_Template.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
