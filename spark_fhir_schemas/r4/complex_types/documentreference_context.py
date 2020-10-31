from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType


from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.extension import Extension
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.period import Period
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.complex_types.reference import Reference
from spark_fhir_schemas.r4.complex_types.reference import Reference


class DocumentReference_Context:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("encounter",ArrayType(Reference.get_schema()), True),
                StructField("event",ArrayType(CodeableConcept.get_schema()), True),
                StructField("period", Period.get_schema(), True),
                StructField("facilityType", CodeableConcept.get_schema(), True),
                StructField("practiceSetting", CodeableConcept.get_schema(), True),
                StructField("sourcePatientInfo", Reference.get_schema(), True),
                StructField("related",ArrayType(Reference.get_schema()), True),
            ]
        )

        return schema
