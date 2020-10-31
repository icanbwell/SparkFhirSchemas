from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.uri import uri
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.reference import Reference


class Identifier:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("use", StringType(), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("system", uri.get_schema(), True),
                StructField("value", StringType(), True),
                StructField("period", Period.get_schema(), True),
                StructField("assigner", Reference.get_schema(), True),]
        )

        return schema
