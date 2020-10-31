from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.id import id
from spark_fhir_schemas.r4.resources.meta import Meta
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.narrative import Narrative
from spark_fhir_schemas.r4.resources.resourcelist import ResourceList
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.code import code
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.timing import Timing
from spark_fhir_schemas.r4.resources.datetime import dateTime
from spark_fhir_schemas.r4.resources.date import date
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.verificationresult_primarysource import VerificationResult_PrimarySource
from spark_fhir_schemas.r4.resources.verificationresult_attestation import VerificationResult_Attestation
from spark_fhir_schemas.r4.resources.verificationresult_validator import VerificationResult_Validator


class VerificationResult:
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
                StructField("target",ArrayType(Reference.get_schema()), True),
                StructField("targetLocation",ArrayType(string.get_schema()), True),
                StructField("need", CodeableConcept.get_schema(), True),
                StructField("status", code.get_schema(), True),
                StructField("statusDate", dateTime.get_schema(), True),
                StructField("validationType", CodeableConcept.get_schema(), True),
                StructField("validationProcess",ArrayType(CodeableConcept.get_schema()), True),
                StructField("frequency", Timing.get_schema(), True),
                StructField("lastPerformed", dateTime.get_schema(), True),
                StructField("nextScheduled", DateType(), True),
                StructField("failureAction", CodeableConcept.get_schema(), True),
                StructField("primarySource",ArrayType(VerificationResult_PrimarySource.get_schema()), True),
                StructField("attestation", VerificationResult_Attestation.get_schema(), True),
                StructField("validator",ArrayType(VerificationResult_Validator.get_schema()), True),]
        )

        return schema
