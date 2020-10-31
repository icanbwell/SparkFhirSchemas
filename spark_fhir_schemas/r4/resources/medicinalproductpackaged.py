from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicinalProductPackaged:
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
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.marketingstatus import MarketingStatus
        from spark_fhir_schemas.r4.complex_types.medicinalproductpackaged_batchidentifier import MedicinalProductPackaged_BatchIdentifier
        from spark_fhir_schemas.r4.complex_types.medicinalproductpackaged_packageitem import MedicinalProductPackaged_PackageItem
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
                StructField(
                    "subject",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField("description", StringType(), True),
                StructField(
                    "legalStatusOfSupply",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "marketingStatus",
                    ArrayType(MarketingStatus.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "marketingAuthorization",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "manufacturer",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "batchIdentifier",
                    ArrayType(
                        MedicinalProductPackaged_BatchIdentifier.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "packageItem",
                    ArrayType(
                        MedicinalProductPackaged_PackageItem.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
