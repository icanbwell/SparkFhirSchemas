from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.string import string


class RiskAssessment_Prediction:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("outcome", CodeableConcept.get_schema(), True),
                StructField("probabilityDecimal", IntegerType(), True),
                StructField("probabilityRange", Range.get_schema(), True),
                StructField("qualitativeRisk", CodeableConcept.get_schema(), True),
                StructField("relativeRisk", decimal.get_schema(), True),
                StructField("whenPeriod", Period.get_schema(), True),
                StructField("whenRange", Range.get_schema(), True),
                StructField("rationale", StringType(), True),]
        )

        return schema
