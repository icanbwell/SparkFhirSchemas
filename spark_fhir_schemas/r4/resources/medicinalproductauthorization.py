from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.identifier import Identifier
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.medicinalproductauthorization_jurisdictionalauthorization import MedicinalProductAuthorization_JurisdictionalAuthorization
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.medicinalproductauthorization_procedure import MedicinalProductAuthorization_Procedure


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
                StructField("contained",ArrayType(ResourceList.get_schema()), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("identifier",ArrayType(Identifier.get_schema()), True),
                StructField("subject", Reference.get_schema(), True),
                StructField("country",ArrayType(CodeableConcept.get_schema()), True),
                StructField("jurisdiction",ArrayType(CodeableConcept.get_schema()), True),
                StructField("status", CodeableConcept.get_schema(), True),
                StructField("statusDate", dateTime.get_schema(), True),
                StructField("restoreDate", dateTime.get_schema(), True),
                StructField("validityPeriod", Period.get_schema(), True),
                StructField("dataExclusivityPeriod", Period.get_schema(), True),
                StructField("dateOfFirstAuthorization", dateTime.get_schema(), True),
                StructField("internationalBirthDate", dateTime.get_schema(), True),
                StructField("legalBasis", CodeableConcept.get_schema(), True),
                StructField("jurisdictionalAuthorization",ArrayType(MedicinalProductAuthorization_JurisdictionalAuthorization.get_schema()), True),
                StructField("holder", Reference.get_schema(), True),
                StructField("regulator", Reference.get_schema(), True),
                StructField("procedure", MedicinalProductAuthorization_Procedure.get_schema(), True),]
        )

        return schema
