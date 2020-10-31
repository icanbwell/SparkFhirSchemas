from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.consent_actor import Consent_Actor
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.coding import Coding
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.consent_data import Consent_Data
from spark_fhir_schemas.r4.complex_types.consent_provision import Consent_Provision


class Consent_Provision:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", StringType(), True),
                StructField("period", Period.get_schema(), True),
                StructField("actor",ArrayType(Consent_Actor.get_schema()), True),
                StructField("action",ArrayType(CodeableConcept.get_schema()), True),
                StructField("securityLabel",ArrayType(Coding.get_schema()), True),
                StructField("purpose",ArrayType(Coding.get_schema()), True),
                StructField("class",ArrayType(Coding.get_schema()), True),
                StructField("code",ArrayType(CodeableConcept.get_schema()), True),
                StructField("dataPeriod", Period.get_schema(), True),
                StructField("data",ArrayType(Consent_Data.get_schema()), True),
                StructField("provision",ArrayType(Consent_Provision.get_schema()), True),
            ]
        )

        return schema
