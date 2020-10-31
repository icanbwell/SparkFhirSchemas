from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept


class Encounter_Hospitalization:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("preAdmissionIdentifier", Identifier.get_schema(), True),
                StructField("origin", Reference.get_schema(), True),
                StructField("admitSource", CodeableConcept.get_schema(), True),
                StructField("reAdmission", CodeableConcept.get_schema(), True),
                StructField("dietPreference",ArrayType(CodeableConcept.get_schema()), True),
                StructField("specialCourtesy",ArrayType(CodeableConcept.get_schema()), True),
                StructField("specialArrangement",ArrayType(CodeableConcept.get_schema()), True),
                StructField("destination", Reference.get_schema(), True),
                StructField("dischargeDisposition", CodeableConcept.get_schema(), True),
            ]
        )

        return schema
