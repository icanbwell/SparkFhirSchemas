from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.quantity import Quantity


class Dosage_DoseAndRate:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("type", CodeableConcept.get_schema(), True),
                StructField("doseRange", Range.get_schema(), True),
                StructField("doseQuantity", Quantity.get_schema(), True),
                StructField("rateRatio", Ratio.get_schema(), True),
                StructField("rateRange", Range.get_schema(), True),
                StructField("rateQuantity", Quantity.get_schema(), True),]
        )

        return schema
