from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class BiologicallyDerivedProduct:
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
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.biologicallyderivedproduct_collection import BiologicallyDerivedProduct_Collection
        from spark_fhir_schemas.r4.complex_types.biologicallyderivedproduct_processing import BiologicallyDerivedProduct_Processing
        from spark_fhir_schemas.r4.complex_types.biologicallyderivedproduct_manipulation import BiologicallyDerivedProduct_Manipulation
        from spark_fhir_schemas.r4.complex_types.biologicallyderivedproduct_storage import BiologicallyDerivedProduct_Storage
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
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField("productCategory", StringType(), True),
                StructField(
                    "productCode",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("status", StringType(), True),
                StructField(
                    "request",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "quantity", integer.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "parent",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "collection",
                    BiologicallyDerivedProduct_Collection.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "processing",
                    ArrayType(
                        BiologicallyDerivedProduct_Processing.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "manipulation",
                    BiologicallyDerivedProduct_Manipulation.
                    get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "storage",
                    ArrayType(
                        BiologicallyDerivedProduct_Storage.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
