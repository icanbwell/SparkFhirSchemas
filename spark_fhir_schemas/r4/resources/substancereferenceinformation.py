from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class SubstanceReferenceInformation:
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
        from spark_fhir_schemas.r4.complex_types.substancereferenceinformation_gene import SubstanceReferenceInformation_Gene
        from spark_fhir_schemas.r4.complex_types.substancereferenceinformation_geneelement import SubstanceReferenceInformation_GeneElement
        from spark_fhir_schemas.r4.complex_types.substancereferenceinformation_classification import SubstanceReferenceInformation_Classification
        from spark_fhir_schemas.r4.complex_types.substancereferenceinformation_target import SubstanceReferenceInformation_Target
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
                StructField("comment", StringType(), True),
                StructField(
                    "gene",
                    ArrayType(
                        SubstanceReferenceInformation_Gene.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "geneElement",
                    ArrayType(
                        SubstanceReferenceInformation_GeneElement.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "classification",
                    ArrayType(
                        SubstanceReferenceInformation_Classification.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "target",
                    ArrayType(
                        SubstanceReferenceInformation_Target.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
