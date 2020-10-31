from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.coverageeligibilityresponse_benefit import CoverageEligibilityResponse_Benefit
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.uri import uri


class CoverageEligibilityResponse_Item:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("productOrService", CodeableConcept.get_schema(), True),
                StructField("modifier",ArrayType(CodeableConcept.get_schema()), True),
                StructField("provider", Reference.get_schema(), True),
                StructField("excluded", BooleanType(), True),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField("network", CodeableConcept.get_schema(), True),
                StructField("unit", CodeableConcept.get_schema(), True),
                StructField("term", CodeableConcept.get_schema(), True),
                StructField("benefit",ArrayType(CoverageEligibilityResponse_Benefit.get_schema()), True),
                StructField("authorizationRequired", BooleanType(), True),
                StructField("authorizationSupporting",ArrayType(CodeableConcept.get_schema()), True),
                StructField("authorizationUrl", uri.get_schema(), True),
            ]
        )

        return schema
