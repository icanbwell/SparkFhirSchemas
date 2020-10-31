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
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.medicinalproductauthorization_jurisdictionalauthorization import MedicinalProductAuthorization_JurisdictionalAuthorization
from spark_fhir_schemas.r4.complex_types.medicinalproductauthorization_procedure import MedicinalProductAuthorization_Procedure


# noinspection PyPep8Naming
class MedicinalProductAuthorization:
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
                StructField(
                    "identifier", ArrayType(Identifier.get_schema()), True
                ),
                StructField("subject", Reference.get_schema(), True),
                StructField(
                    "country", ArrayType(CodeableConcept.get_schema()), True
                ),
                StructField(
                    "jurisdiction", ArrayType(CodeableConcept.get_schema()),
                    True
                ),
                StructField("status", CodeableConcept.get_schema(), True),
                StructField("statusDate", dateTime.get_schema(), True),
                StructField("restoreDate", dateTime.get_schema(), True),
                StructField("validityPeriod", Period.get_schema(), True),
                StructField(
                    "dataExclusivityPeriod", Period.get_schema(), True
                ),
                StructField(
                    "dateOfFirstAuthorization", dateTime.get_schema(), True
                ),
                StructField(
                    "internationalBirthDate", dateTime.get_schema(), True
                ),
                StructField("legalBasis", CodeableConcept.get_schema(), True),
                StructField(
                    "jurisdictionalAuthorization",
                    ArrayType(
                        MedicinalProductAuthorization_JurisdictionalAuthorization
                        .get_schema()
                    ), True
                ),
                StructField("holder", Reference.get_schema(), True),
                StructField("regulator", Reference.get_schema(), True),
                StructField(
                    "procedure",
                    MedicinalProductAuthorization_Procedure.get_schema(), True
                ),
            ]
        )

        return schema
