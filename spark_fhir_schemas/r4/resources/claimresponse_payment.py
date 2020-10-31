from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.money import Money
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.date import date
from spark_fhir_schemas.r4.resources.money import Money
from spark_fhir_schemas.r4.resources.identifier import Identifier


class ClaimResponse_Payment:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("adjustment", Money.get_schema(), True),
                StructField("adjustmentReason", CodeableConcept.get_schema(), True),
                StructField("date", DateType(), True),
                StructField("amount", Money.get_schema(), True),
                StructField("identifier", Identifier.get_schema(), True),]
        )

        return schema
