from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicinalProduct:
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
        from spark_fhir_schemas.r4.complex_types.coding import Coding
        from spark_fhir_schemas.r4.complex_types.marketingstatus import MarketingStatus
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.medicinalproduct_name import MedicinalProduct_Name
        from spark_fhir_schemas.r4.complex_types.medicinalproduct_manufacturingbusinessoperation import MedicinalProduct_ManufacturingBusinessOperation
        from spark_fhir_schemas.r4.complex_types.medicinalproduct_specialdesignation import MedicinalProduct_SpecialDesignation
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
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "domain", Coding.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "combinedPharmaceuticalDoseForm",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "legalStatusOfSupply",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "additionalMonitoringIndicator",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField("specialMeasures", ArrayType(StringType()), True),
                StructField(
                    "paediatricUseIndicator",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "productClassification",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "marketingStatus",
                    ArrayType(MarketingStatus.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "pharmaceuticalProduct",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "packagedMedicinalProduct",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "attachedDocument",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "masterFile",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "contact",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "clinicalTrial",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "name",
                    ArrayType(
                        MedicinalProduct_Name.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "crossReference",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "manufacturingBusinessOperation",
                    ArrayType(
                        MedicinalProduct_ManufacturingBusinessOperation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "specialDesignation",
                    ArrayType(
                        MedicinalProduct_SpecialDesignation.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
