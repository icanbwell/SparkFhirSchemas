from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.reference import Reference
from spark_fhir_schemas.r4.resources.period import Period
from spark_fhir_schemas.r4.resources.duration import Duration
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.duration import Duration


class Specimen_Collection:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("collector", Reference.get_schema(), True),
                StructField("collectedDateTime", StringType(), True),
                StructField("collectedPeriod", Period.get_schema(), True),
                StructField("duration", Duration.get_schema(), True),
                StructField("quantity", Quantity.get_schema(), True),
                StructField("method", CodeableConcept.get_schema(), True),
                StructField("bodySite", CodeableConcept.get_schema(), True),
                StructField("fastingStatusCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("fastingStatusDuration", Duration.get_schema(), True),]
        )

        return schema
