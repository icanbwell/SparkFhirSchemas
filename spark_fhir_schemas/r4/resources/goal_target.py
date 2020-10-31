from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType
from spark_fhir_schemas.r4.resources.string import string
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.extension import Extension
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.quantity import Quantity
from spark_fhir_schemas.r4.resources.range import Range
from spark_fhir_schemas.r4.resources.codeableconcept import CodeableConcept
from spark_fhir_schemas.r4.resources.ratio import Ratio
from spark_fhir_schemas.r4.resources.duration import Duration


class Goal_Target:
    @staticmethod
    def get_schema() -> StructType:
        # from https://hl7.org/FHIR/patient.html
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("extension",ArrayType(Extension.get_schema()), True),
                StructField("modifierExtension",ArrayType(Extension.get_schema()), True),
                StructField("measure", CodeableConcept.get_schema(), True),
                StructField("detailQuantity", Quantity.get_schema(), True),
                StructField("detailRange", Range.get_schema(), True),
                StructField("detailCodeableConcept", CodeableConcept.get_schema(), True),
                StructField("detailString", StringType(), True),
                StructField("detailBoolean", BooleanType(), True),
                StructField("detailInteger", IntegerType(), True),
                StructField("detailRatio", Ratio.get_schema(), True),
                StructField("dueDate", StringType(), True),
                StructField("dueDuration", Duration.get_schema(), True),]
        )

        return schema
