from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.string import string


class ObservationDefinition_QualifiedInterval:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("category", StringType(), True),
                StructField("range", Range.get_schema(), True),
                StructField("context", CodeableConcept.get_schema(), True),
                StructField("appliesTo",ArrayType(CodeableConcept.get_schema()), True),
                StructField("gender", StringType(), True),
                StructField("age", Range.get_schema(), True),
                StructField("gestationalAge", Range.get_schema(), True),
                StructField("condition", StringType(), True),]
        )

        return schema
