from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.id import id
from spark_fhir_schemas.r4.complex_types.meta import Meta
from spark_fhir_schemas.r4.complex_types.uri import uri
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.narrative import Narrative
from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.code import code
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.datetime import dateTime
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_insurance import CoverageEligibilityResponse_Insurance
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_error import CoverageEligibilityResponse_Error


class CoverageEligibilityResponse:
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
                StructField("status", code.get_schema(), True),
                StructField("purpose",ArrayType(None.get_schema()), True),
                StructField("patient", Reference.get_schema(), True),
                StructField("servicedDate", StringType(), True),
                StructField("servicedPeriod", Period.get_schema(), True),
                StructField("created", dateTime.get_schema(), True),
                StructField("requestor", Reference.get_schema(), True),
                StructField("request", Reference.get_schema(), True),
                StructField("outcome", StringType(), True),
                StructField("disposition", StringType(), True),
                StructField("insurer", Reference.get_schema(), True),
                StructField("insurance",ArrayType(CoverageEligibilityResponse_Insurance.get_schema()), True),
                StructField("preAuthRef", StringType(), True),
                StructField("form", CodeableConcept.get_schema(), True),
                StructField("error",ArrayType(CoverageEligibilityResponse_Error.get_schema()), True),
            ]
        )

        return schema
