from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class MedicinalProductAuthorization:
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
        from spark_fhir_schemas.r4.complex_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.period import Period
        from spark_fhir_schemas.r4.complex_types.medicinalproductauthorization_jurisdictionalauthorization import MedicinalProductAuthorization_JurisdictionalAuthorization
        from spark_fhir_schemas.r4.complex_types.medicinalproductauthorization_procedure import MedicinalProductAuthorization_Procedure
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
                    "subject", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "country",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "jurisdiction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "status", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "statusDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "restoreDate", dateTime.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "validityPeriod", Period.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "dataExclusivityPeriod",
                    Period.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "dateOfFirstAuthorization",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "internationalBirthDate",
                    dateTime.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "legalBasis",
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "jurisdictionalAuthorization",
                    ArrayType(
                        MedicinalProductAuthorization_JurisdictionalAuthorization
                        .get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "holder", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "regulator", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "procedure",
                    MedicinalProductAuthorization_Procedure.
                    get_schema(recursion_depth + 1), True
                ),
            ]
        )

        return schema
