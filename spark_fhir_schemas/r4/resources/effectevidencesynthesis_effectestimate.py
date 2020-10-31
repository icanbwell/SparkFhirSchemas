from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.decimal import decimal
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.effectevidencesynthesis_precisionestimate import EffectEvidenceSynthesis_PrecisionEstimate


class EffectEvidenceSynthesis_EffectEstimate:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("description", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("variantState", CodeableConcept.get_schema(), True),
                StructField("value", decimal.get_schema(), True),
                StructField("unitOfMeasure", CodeableConcept.get_schema(), True),
                StructField("precisionEstimate",ArrayType(EffectEvidenceSynthesis_PrecisionEstimate.get_schema()), True),]
        )

        return schema
