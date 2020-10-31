from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.boolean import boolean
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.explanationofbenefit_financial import ExplanationOfBenefit_Financial


class ExplanationOfBenefit_BenefitBalance:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("category", CodeableConcept.get_schema(), True),
                StructField("excluded", BooleanType(), True),
                StructField("name", StringType(), True),
                StructField("description", StringType(), True),
                StructField("network", CodeableConcept.get_schema(), True),
                StructField("unit", CodeableConcept.get_schema(), True),
                StructField("term", CodeableConcept.get_schema(), True),
                StructField("financial",ArrayType(ExplanationOfBenefit_Financial.get_schema()), True),]
        )

        return schema
