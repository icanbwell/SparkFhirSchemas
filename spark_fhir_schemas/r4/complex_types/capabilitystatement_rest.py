from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class CapabilityStatement_Rest:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.markdown import markdown
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_security import CapabilityStatement_Security
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_resource import CapabilityStatement_Resource
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_interaction1 import CapabilityStatement_Interaction1
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_searchparam import CapabilityStatement_SearchParam
        from spark_fhir_schemas.r4.complex_types.capabilitystatement_operation import CapabilityStatement_Operation
        from spark_fhir_schemas.r4.complex_types.canonical import canonical
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
                StructField("mode", StringType(), True),
                StructField(
                    "documentation", markdown.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "security",
                    CapabilityStatement_Security.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "resource",
                    ArrayType(
                        CapabilityStatement_Resource.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "interaction",
                    ArrayType(
                        CapabilityStatement_Interaction1.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "searchParam",
                    ArrayType(
                        CapabilityStatement_SearchParam.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "operation",
                    ArrayType(
                        CapabilityStatement_Operation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "compartment",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
            ]
        )

        return schema
